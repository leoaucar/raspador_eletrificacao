# COMMAND LINE INTERFACE
# SEARCH --> CONTROLLER --> SCRAPPER

test_data =[
    #{"name":"Diario do Vale", "url":"diariodovale.com.br", "scrapper_id":0, "cleaner_id":0},
    #{"name":"AutoData", "url":"www.autodata.com.br", "scrapper_id":1, "cleaner_id":1},
    #{"name":"Diario Grande ABC", "url":"www.dgabc.com.br", "scrapper_id":2, "cleaner_id":2},
    {"name":"SIMEC", "url":"www.simec.com.br/", "scrapper_id":3, "cleaner_id":3}
]

test_search = ["carro eletrico"]
"""test_search = ["eletrificação sindicato",
               "veículo eletrico sindicato",
               "veículo híbrido sindicato",
               "carro elétrico sindicato",
               "carro híbrido sindicato"
               ]"""
"""test_search = ["transição energética sindicato",
               "biocombustível sindicato"
               ]"""

def file_name_input():
    name = input("Type file name: ")
    return name