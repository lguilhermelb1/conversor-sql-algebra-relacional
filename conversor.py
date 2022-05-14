from validarCampos import camposJoin, camposSelect, tabelaFrom, tabelasJoin, camposWhere, validar

def conversorSelect(txt):
    campos = camposSelect(txt)
    select = ""
    
    for i in range(len(campos)):
        if i == len(campos)-1:
            select += str(campos[i]) + " "
        else:
            select += str(campos[i]) + ", "
    
    #Retorna tudo
    return "π " + select + conversorCamposWhere(txt) + conversorFrom(txt) + conversorJoinTabelas(txt)

def conversorFrom(txt):
    tabela = tabelaFrom(txt)
    tabelaaFrom = str(tabela)
    
    return "(" + tabelaaFrom

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
    #Adiciona os campos a variavel
    campos = camposWhere(txt)
    #Auxiliar para adicionar o texto
    campoWhere = ""

    #Percorre os campos
    for i in range(len(campos)):
        #Adiciona ao auxiliar e trata
        #Se for ultimo da lista campos adiciona espaço
        if i == len(campos)-1:
            campoWhere += str(campos[i]) + " "
        #Se não for adiciona a vírgula
        else:
            campoWhere += str(campos[i]) + " AND "
    
    #Retorna o auxiliar preenchido e tratado
    return "σ " + campoWhere