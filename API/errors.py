def card_not_found(card_id):
    return { 
        'result': False,
        'msg': 'Card não encontrado',
        'given_card_id' : card_id
    }

def fields_are_required(fields):
    return {
        'result': False,
        'msg': 'Parâmetro(s) obrigatorio(s) não encontrado(s)',
        'missing_params': fields
    }

def tag_not_found(card_id, index):
    return {
        'result': False,
        'msg': 'Tag não encontrado',
        'card_id' : card_id,
        'given_tag_index': index
    }