#  Funcionalidades principais:
#  a. Parser (Análise) de uma consulta SQL;
#  b. Geração do grafo de operadores da consulta;
#  c. Ordem de execução da consulta;
#  d. Exibição dos resultados na interface gráfica;

# Operadores permitidos:
# i. Select, From, Where, Join (duas ou mais tabelas);
# ii. Operadores (=, >, <, <=, >=, <>, And, In, Not In);


# Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >=235 and uf ='ce' and cep <> '62930000';
# "from usuario Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição join contas on usuario.idUsuario = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"

from pickle import TRUE
import re

txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = ce and cep <> 62930000"
txt = txt.lower()
txt2 = txt2.lower()
# validate = re.search("^(?=.*select.*from.)", txt)


def camposSelect(txt):
    campos = txt.split("from")[0]
    campos = campos.replace(
        "select", "").replace(" ", "").split(",")
    return campos


def tabelaFrom(txt):
    campo = txt.split("from")[1].split(" ")[1]
    return campo


def tabelasJoin(txt):
    campos = txt.split("join")
    camposAux = []
    for i in range(len(campos)):
        if i > 0:
            camposAux.append(campos[i].split(" ")[1])
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
    campos = txt.split("where")[1].split(" ")
    camposAux = []
    for i in range(len(campos)):
        if checkOperators(campos[i]):
            camposAux.append(campos[i-1])

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


camposSelect = camposWhere(txt)


print(camposSelect)

# if validate:
#   print("YES! We have a match!")
# else:
#   print("No match")
