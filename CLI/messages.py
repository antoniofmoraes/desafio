def firebasecredentials_error():
    return """
# Perdão,
# Houve um problema ao acessar o banco de dados.
# Possívelmente há um problema com suas credenciais de acesso.
# Verifique se seu arquivo de credenciais está no lugar certo e nomeado corretamente e reinicie o aplicativo.
# Seu arquivo deve estar na pasta raiz do desafio (.\\desafio) e nomeado como 'firebasecredentials.json'.

# Se você ja verificou e tudo aparenta estar correto você pode me contatar e eu te ajudarei ou lhe darei um novo arquivo.
# Se você ainda não tem o arquivo você deve me contatar e eu lhe enviarei um.
# Contato: Antonio Moraes
# Fone: 41 99662-4022
# E-mail: antonio.f.f.moraes@gmail.com
    """

def welcome():
    return """
# Olá, seja bem vindo ao CLI do Insights! Aqui você pode usar um arquivo CSV para adicionar cards ao Insights

# Vale destacar que essa CLI funciona independente da API do Insights, então você não precisa estar rodando a API para importar o seu CSV.

# O CSV deve estar no seguinte formato: Texto,tag;tag2;tag3
# Exemplos: Lorem ipsum dolor sit amet., tag1;tag2;tag3
# Mauris fringilla non quam vel lacinia,tag3
# Cras in tempus libero,
    """

def file_path_orientations():
    return """
# Preciso que você informe o caminho do arquivo.
# Você pode informar o caminho completo para o arquivo, ex: C:\\Caminho\\para\\o\\seu\\arquivo.csv
# Você tampo pode colocar o arquivo dentro da pasta raiz da CLI (.\\desafio\\CLI) e informar o nome do arquivo no formato 'arquivo.csv' sem as aspas.
    """

def file_path_error(path):
    return """
# Houve um erro ao tentar abrir o arquivo: {}
# Verifique o nome/caminho do arquivo e tente novamente
    """.format(path)

def card_import_start():
    return '# Iniciando a importação dos cards:'

def card_import_count(count, id):
    return '# Card {} adicionado. Id: {}'.format(count, id)

def card_import_concluded(count):
    return "# A importação de {} cards foi concluída.".format(count)