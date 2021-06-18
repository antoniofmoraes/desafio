# Insights by Antonio Moraes

Bem vindo ao Isights.  
Este é um projeto feio com base no desafio proposto, o desafio proposto pode ser lido em: https://github.com/antoniofmoraes/desafio/DesafioProposto.md.  
Ele é divido em 3 partes, a API, a CLI e o Front-End.  
  
### API  
  
Feita em Python usando o framework FastAPI para agilizar processo de criação e documentação.  
A documentação se encontra em http://127.0.0.1:8000/docs.  
  
### CLI  
  
Uma CLI independente da API para efetuar importação de arquivos CSV para inclusão de cards diretamente ao banco de dados.  
  
### Front-End  
  
Uma interface feita em React seguindo o layout disponibilizado. Apesar de funcionar normalmente em destktop, o aplicativo é melhor aproveitado no layout de celulares, recomenda-se utilização das ferramentas de desenvolvedor do navegador para simular uma tela de celular.  
  
### Banco de dados  
  
O banco de dados escolhido foi o Firebase da Google.  
  
## Instruções para rodar o projeto  
  
Primeiramente é necessário ter o NodeJS (https://nodejs.org/en/) e o python (https://www.python.org/downloads/ ou usando a Microsoft Store) caso não tenha instalado.  
Também é necessário ter o pip instalado, caso não tenha use este ou qualquer outro tutorial pra instalar (https://phoenixnap.com/kb/install-pip-windows).  
  
### Banco de dados  
  
O banco de dados utilizado é o Firebase da Google, é necessário ter o arquivo de credenciais, 'firebasecredentials.json', na pasta raiz do desafio.  
Caso ainda não tenha o arquivo entre em contato comigo, as minhas informações para contato estarão no roda-pé.  
  
### API e CLI  
  
O processo para preparar o ambiente e rodar o projeto é o mesmo na API e no CLI então é só fazer em um e repetir o proceso em outro.  
  
1. Vá para a pasta do projeto ('desafio/API' ou 'desafio/CLI')  
  
2. Você pode optar por fazer um ambiente virtual para instalar as dependências, caso não queira é só pular para o próximo passo  
Crie o ambiente virtual:  
```
  python3 -m venv env
```
Ative o ambiente virtual:  
```
  env\Scripts\activate
```
Os próximos comandos você ira rodar com o ambiente virtual ativado mas caso queira desativar a qualquer momento o comando é 'deactivate'  
  
3.Instale os requisitos:  
```
  pip install -r requirements.txt
```
4.Rode o projeto usando o comando:  
```
  python main.py
```
  
A API está configurada para rodar no url http://127.0.0.1:8000 .  
  
### Front-End  
  
Aqui é só entrar na pasta do app ('desafio/Front'), rodar o comando ```npm install``` para instalar as dependencias e rodar o comando ```npm start```.  
O aplicativo esta configurado para rodar no url http://localhost:3000 .  
  
## Informações para contato  
  
### Antonio Felype F. Moraes  
  
E-mail: antonio.f.f.moraes@gmail.com  
Fone: 41 99662-4022  
LinkedIn: https://www.linkedin.com/in/antonio-moraes-78a033151/  
