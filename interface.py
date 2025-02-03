# COMMAND LINE INTERFACE
# SEARCH --> CONTROLLER --> SCRAPPER

test_data =[
    {"name":"Diario do Vale", "url":"diariodovale.com.br", "scrapper_id":0, "cleaner_id":0},
    {"name":"dia", "url":"www.odia.ig.com.br/", "scrapper_id":1, "cleaner_id":1}
]

test_search = ["eletrificacao sindicato metalurgicos",
               "eletrificacao"
               ]

def file_name_input():
    name = input("Type file name: ")
    return name