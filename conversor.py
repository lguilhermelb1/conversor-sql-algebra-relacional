from validarCampos import camposJoin, camposSelect, tabelaFrom, tabelasJoin, camposWhere
from validarFormatoSQL import validar_sql

def converteTudo(txt):
    return conversorSelect(txt) + " " + conversorCamposWhere(txt) + " " + conversorFrom(txt) + conversorJoinTabelas(txt)

def conversorSelect(txt):
    return "π " + validar_sql(txt).get('campos').get('select')

def conversorFrom(txt):    
    return "(" + validar_sql(txt).get('campos').get('from')

def conversorJoinTabelas(txt):
    tabelas = tabelasJoin(txt)
    tabelaJoin = ""

    for i in range(len(tabelas)):
        #Se for ultimo da lista tabelas adiciona o )
        if i == len(tabelas)-1:
            tabelaJoin += str(tabelas[i]) + ")"
        #Se não for adiciona o |x|
        else:
            tabelaJoin += str(tabelas[i]) + " |x| "

    return " |x| " + tabelaJoin

def conversorJoinCampos(txt):
    campos = camposJoin(txt)
    campoJoin = ""

    for i in range(len(campos)):
        campoJoin += str(campos[i]) + " "
    
    return campoJoin

def conversorCamposWhere(txt):
    return "σ " + validar_sql(txt).get('campos').get('where')