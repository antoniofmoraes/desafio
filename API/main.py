from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import uvicorn

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import errors

tags_metadata = [
    {
        "name": "Criar card",
        "description": "Criação de card. Campos esperados: text, tags. O campo 'tags' deve ser dividido por vírgulas (,)",
    },
    {
        "name": "Mostrar card",
        "description": "Mostrar card usando seu id (card_id).",
    },
    {
        "name": "Deletar card",
        "description": "Deletar o card através do seu id (card_id).",
    },
    {
        "name": "Atualizar card",
        "description": "Atualizar o card através do seu id (card_id). Campos esperados: 'text'.",
    },
    {
        "name": "Listar cards",
        "description": "Listar os cards podendo filtrar por tags, ordenado pela data da última atualização, da mais recente ao menos recente. Campos opcionais: tags, para filtrar por tags. O campo 'tags' deve ser dividido por vírgulas (,)",
    },
    {
        "name": "Incluir novas tags",
        "description": "Incluir novas tags (new_tags) em um card através do id (card_id). O campo 'new_tags' deve ser dividido por vírgulas (,)",
    },
    {
        "name": "Listar tags",
        "description": "Listar tags de um card através do id (card_id)",
    },
    {
        "name": "Deletar tags",
        "description": "Deletar tags de um card através do id (card_id), podendo filtrar pelo índice das tags (tags_indexes) ou pelos nome das tags (tags_names). Campos opcionais: tags_indexes, tags_names. Tando os índices quanto os nomes devem estar separados por vírgula (,). ",
    },
    {
        "name": "Atualizar tag",
        "description": "Atualizar o nome de um card (tag_new_name), através do id do card (card_id) e do índice da tag (tag_index).",
    },

]

app = FastAPI(
    title="Insights API",
    description="Esta é a API do desafio proposto, do projeto chamado Insights. Feito por: Antonio Felype F. Moraes",
    openapi_tags=tags_metadata,
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cred = credentials.Certificate("../firebasecredentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.post('/card/create', tags=['Criar card'])
def create_card(request: Request):
    data = request.query_params._dict
    
    if 'text' not in data:
        return errors.fields_are_required('text')
    
    card = {
        u'text': data['text'],
        u'crate_date': firestore.SERVER_TIMESTAMP,
        u'update_date': firestore.SERVER_TIMESTAMP
    }

    result = db.collection(u'cards').add(card)

    if 'tags' in data:
        for tag in data['tags'].split(','):
            db.collection(u'cards').document(result[1].id).collection(u'tags').add({ u'name': tag})

    return result[1].id

@app.get('/card/{card_id}', tags=['Mostrar card'])
def show_card(card_id: str):
    card = db.collection(u'cards').document(card_id).get()

    if not card.exists:
        return errors.card_not_found(card_id)

    return card._data

@app.delete('/card/{card_id}', tags=['Deletar card'])
def remove_card(card_id: str):
    card_ref = db.collection(u'cards').document(card_id)
    
    if not card_ref.get().exists:
        return errors.card_not_found(card_id)
    
    return card_ref.delete()

@app.put('/card/{card_id}', tags=['Atualizar card'])
def update_card(card_id: str, request: Request):
    data = request.query_params._dict
    
    if 'text' not in data:
        return errors.fields_are_required('text')

    card_ref = db.collection(u'cards').document(card_id)

    if not card_ref.get().exists:
        return errors.card_not_found(card_id)

    card_ref.update({
        u'text': data['text'],
        u'update_date': firestore.SERVER_TIMESTAMP
    })

    return { 'result': True }

@app.get('/cards', tags=['Listar cards'])
def list_cards(tags: Optional[str] = None):
    if (tags):
        tags = tags.split(',')

        cards = []
        for tag in tags:
            cards.extend(db.collection(u'cards').where('tags', 'array_contains', tag).get())
        cards = list(dict.fromkeys(cards))
    else:
        cards = db.collection(u'cards').get()

    results = []
    for card in cards:
        results.append(card._data)

    results = sorted(results, key=lambda x: x['update_date'], reverse=True)

    return results

@app.post('/tags/{card_id}/{new_tags}', tags=['Incluir novas tags'])
def crate_tag(card_id: str, new_tags: str):
    card_ref = db.collection(u'cards').document(card_id)
    card = card_ref.get()

    if not card.exists:
        return errors.card_not_found(card_id)
    
    tags = card._data['tags'] if 'tags' in card._data else []
    new_tags = new_tags.split(',')
    tags.extend(new_tags)
    
    card_ref.update({u'tags': tags})

    return tags

@app.get('/tags/{card_id}', tags=['Listar tags'])
def get_tags(card_id: str):
    card_ref = db.collection(u'cards').document(card_id)
    card = card_ref.get()

    if not card.exists:
        return errors.card_not_found(card_id)
    
    return card._data['tags'] if 'tags' in card._data else []
    

@app.delete('/tags/{card_id}', tags=['Deletar tags'])
def remove_tag(card_id: str, tags_indexes: Optional[str], tags_names: Optional[str]):
    card_ref = db.collection(u'cards').document(card_id)
    card = card_ref.get()

    if not card.exists:
        return errors.card_not_found(card_id)
    
    if not tags_indexes and not tags_names:
        tags = []
    else:
        tags = card._data['tags'] if 'tags' in card._data else []
        
        if tags_indexes:
            tags_indexes = [ int(tag) for tag in tags_indexes.split(',') ]
            tags_indexes = sorted(tags_indexes, reverse=True)

            for tag_index in tags_indexes:
                del tags[tag_index]

        if tags_names:
            tags = list(filter(lambda tag: not tag in tags_names.split(','), tags))

    card_ref.update({u'tags': tags})

    return tags

@app.put('/tags/{card_id}/{tag_index}/{tag_new_name}', tags=['Atualizar tag'])
def update_tag(card_id: str, tag_index: int, tag_new_name: str):
    card_ref = db.collection(u'cards').document(card_id)
    card = card_ref.get()

    if not card.exists:
        return errors.card_not_found(card_id)

    tags = card._data['tags'] if 'tags' in card._data else []

    try:
        tags[tag_index] = tag_new_name
    except:
        return errors.tag_not_found(card_id, tag_index)

    card_ref.update({ 'tags': tags })
    
    return { 'result': True }

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)