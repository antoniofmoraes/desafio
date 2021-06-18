import os
import sys
import csv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import messages

try:
    cred = credentials.Certificate("../firebasecredentials.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

except:
    print(messages.firebasecredentials_error())
    input('Pressione ENTER para sair.')
    exit()

print(messages.welcome())

input("Pressione ENTER para continuar")

while True:
    os.system('cls')
    print(messages.file_path_orientations())

    path = input('Informe o nome/caminho do arquivo: ')
    os.system('cls')

    try:
        file = open(path, 'r')
    except:
        print(messages.file_path_error(path))
        if input('Pressione ENTER para tentar denovo ou digite S para sair do aplicativo: ').lower() ==  's':
            exit()
        continue

    with file as csv_file:
        csv_reader = csv.reader(csv_file)

        print(messages.card_import_start())

        count = 0
        for line in csv_reader:
            card = {
                u'text': line[0],
                u'tags': line[1].split(';') if line[1] != '' else [],
                u'crate_date': firestore.SERVER_TIMESTAMP,
                u'update_date': firestore.SERVER_TIMESTAMP
            }
            add_data = db.collection(u'cards').add(card)
            count += 1
            print(messages.card_import_count(count, add_data[1].id))

    print(messages.card_import_concluded(count))
    if input("\nDeseja importar mais arquivos CSV? Caso sim digite 'S': ").lower() != 's':
        exit()
    
exit()