# COMMAND LINE INTERFACE
# SEARCH --> CONTROLLER --> SCRAPPER

test_data =[
    #{"name":"Diario do Vale", "url":"diariodovale.com.br", "scrapper_id":0, "cleaner_id":0},
    {"name":"AutoData", "url":"www.autodata.com.br", "scrapper_id":1, "cleaner_id":1}
]

"""test_search = ["eletrificação sindicato metalúrgicos",
               "veículo eletrico sindicato metalúrgicos",
               "veículo híbrido sindicato metalúrgicos",
               "carro elétrico sindicato metalúrgicos",
               "carro híbrido sindicato metalúrgicos",
               "eletrificação sindicato",
               "veículo eletrico sindicato",
               "veículo híbrido sindicato",
               "carro elétrico sindicato",
               "carro híbrido sindicato"
               ]"""
test_search = ["eletrificação sindicato",
               #"veículo eletrico sindicato",
               #"veículo híbrido sindicato",
               #"carro elétrico sindicato",
               "carro híbrido sindicato"
               ]
"""test_search = ["transição energética sindicato",
               "biocombustível sindicato"
               ]"""

def file_name_input():
    name = input("Type file name: ")
    return name