import requests
import sqlite3
import json

banco = sqlite3.connect('sqlite.db')
cursor = banco.cursor()
"""
cursor.execute('''  CREATE TABLE teste_aptidao (
                        id_via_cep INTEGER PRIMARY KEY AUTOINCREMENT,
                        reference varchar(200) NOT NULL,
                        id varchar(200) NOT NULL,
                        section varchar(200),
                        weight varchar(200) NOT NULL,
                        links varchar(200) NOT NULL,
                        database varchar(20) NOT NULL
                        
                    );''')
"""
print("########################")
print("##### Consulta CEP #####")
print("########################")


cep_input = input("Digite o CEP para a consulta: ")

if len(cep_input) != 8:
    print("Quantidade de digitos inválida!")
    exit()

request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

address_data = request.json()
if "erro" not in address_data:
    print("CEP: {}".format(address_data["autnresponse"]))
    print("LOGRADOURO: {}".format(address_data["logradouro"]))
    print("COMPLEMENTO: {}".format(address_data["complemento"]))
    print("BAIRRO: {}".format(address_data["bairro"]))
    print("LOCALIDADE: {}".format(address_data["localidade"]))
    print("UF: {}".format(address_data["uf"]))
    print("IBGE: {}".format(address_data["ibge"]))
    print("GIA: {}".format(address_data["gia"]))
    print("DDD: {}".format(address_data["ddd"]))
    print("SIAFI: {}".format(address_data["siafi"]))
    cursor.execute(f'''INSERT INTO viaCEP(cep , logradouro , complemento , bairro , localidade , uf , ibge , gia , ddd , siafi) 
                            VALUES ('{address_data["cep"]}' , '{address_data["logradouro"]}' , '{address_data["complemento"]}' , '{address_data["bairro"]}' , '{address_data["localidade"]}' , '{address_data["uf"]}' , '{address_data["ibge"]}' , '{address_data["gia"]}' , '{address_data["ddd"]}' , '{address_data["siafi"]}' )''')
    banco.commit()

else:
    print("{}CEP inválido!".format(cep_input))
