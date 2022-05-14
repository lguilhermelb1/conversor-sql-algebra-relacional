
import dicionario


def camposSelect(txt):
    campos = txt.split("from")[0]
    campos = campos.replace(
        "select", "").replace(" ", "").split(",")
    return campos


def tabelaFrom(txt):
    campo = txt.split("from")[1]

    if(campo.__contains__("join")):
        campo = campo.replace(" ", "").split("join")[0]
        
    elif(campo.__contains__("where")):
        campo = campo.replace(" ", "").split("where")[0]

    else:
        campo = campo.replace(" ", "")

    return campo


def tabelasJoin(txt):
    campos = txt.split("join")
    
    camposAux = []
    for i in range(len(campos)):
        if i > 0:
            camposAux.append(campos[i].split(" on ")[0].replace(" ",""))
    return camposAux


def camposJoin(txt):
    campos = txt.split("where")[0].split("join")
    campos.pop(0)
    camposAux = []
    for c in campos:
        campos2 = c.split(" ")
        for i in campos2:
            if i.find('.') != -1:
                camposAux.append(i)

    return camposAux


def camposWhere(txt):
    
    camposAux = []
    if txt.__contains__("where"):
        campos = txt.split("where")[1].split(" ")
        for i in range(len(campos)):
            if checkOperators(campos[i]):
                aux = 1
                while campos[i-aux] == '':
                    aux = aux + 1
                camposAux.append(campos[i-aux])

    return camposAux


def checkOperators(campo):
    if (campo.__contains__("=") |
            campo.__contains__("<") |
            campo.__contains__(">") |
            campo.__contains__("<>") |
            campo.__contains__(">=") |
            campo.__contains__("<=")):
        return True
    return False

def contains(items,value):
    for i in items:
        if i.lower() == value.lower():
            return True
    return False


def validar(txt):
    banco = dicionario.tabelas
    tabelasSql = []
    camposSelectWhere = []
    tabelasBanco = []
    camposSelectWhere.extend(camposWhere(txt))
    camposSelectWhere.extend(camposSelect(txt))

    tabelasSql.append(tabelaFrom(txt))
    tabelasSql.extend(tabelasJoin(txt))
    for i in camposJoin(txt):
        camposSelectWhere.append(i.split(".")[1])
        
    # verifica se as tabelas do banco batem com a do SQL
    for i in tabelasSql:
       if(contains(banco.keys(), i) == False):
           print("Tabelas do SQL não batem com as do banco: " + i)
           return False
    
    for key in banco:
        if(contains(tabelasSql, key)):
            tabelasBanco.extend(banco[key]['atributos'])

    for i in camposSelectWhere:
        if contains(tabelasBanco, i) == False:
            print("Campos do SQL não batem com as do banco: "+ i)
            return False

    return True
    
    
