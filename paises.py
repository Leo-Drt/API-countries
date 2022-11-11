import json
import sys

import requests

URL_All= "https://restcountries.com/v3.1/all"
URL_Name= "https://restcountries.com/v3.1/name"


def requisao(url):
    try:
        resposta= requests.get(url)
        if resposta.status_code== 200:
            return resposta.text
    except:
        print("Erro ao fazer a requiseção em: ",url)
        
def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro ao fazer o parsing")


def contagem_de_paises():
    resposta= requisao(URL_All)
    if resposta:
        lista_de_paises= parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])

def mostrar_populacao(nome_do_pais):
    resposta= requisao("{}/{}".format(URL_Name, nome_do_pais))
    if resposta:
        lista_de_paises= parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {} habitantes".format(pais["name"], pais["population"]))
    else:
        print("Pais não encontrado!")

def mostrar_moedas(nome_do_pais):
    resposta= requisao("{}/{}".format(URL_Name, nome_do_pais))
    if resposta:
        lista_de_paises= parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("País {}".format(pais["name"]))
                moedas= pais["currencies"]
                for moeda in moedas:
                    print("Moeda: {} ".format(moeda))
    else:
        print("País não encontrado!")

def mostrar_idioma(nome_do_pais):
    reposta= requisao("{}/{}".format(URL_Name, nome_do_pais))
    if reposta:
        lista_paises= parsing(reposta)
        if lista_paises:
            for pais in lista_paises:
                print("País {}".format(pais["name"]))
                idiomas= pais["languages"]
                for idioma in idiomas:
                    print("Seu idioma {}".format(idioma))
    else:
        print("País/idioma não encontrado!")

def ler_nome_do_pais():
    try:
        nome_do_pais= sys.argv[2]
        return nome_do_pais
    except:
        print("Precisa passar o nome do país!")


if __name__== "__main__":
    if len(sys.argv)== 1:

        print("Bem vindo ao sistema de píases do terminal python!")
        print("Modo de uso: países.py <ação> <nome do país>")
        print("Açôes disponíveis:\n contagem, população, moeda e idioma")
        print("OBS -> Não se usa acentos e nem *ç* no terminal !")
    else:
        argumento1= sys.argv[1]
        if argumento1== "contagem":
            numero_de_paises= contagem_de_paises()
            print("Existem {} países no mundo!".format(numero_de_paises))

        elif argumento1== "moeda":
            pais= ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)

        elif argumento1== "populacao":
            pais= ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)

        elif argumento1== "idioma":
            pais= ler_nome_do_pais()
            if pais:
                mostrar_idioma(pais)
        else:
            print("Argumento inválido!")
    

