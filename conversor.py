from validarCampos import camposJoin, camposSelect, tabelaFrom, tabelasJoin, camposWhere
from validarFormatoSQL import validar_sql
import re


# Converte tudo
def priest(txt):
    return converter_select(txt) + " " + converter_where(txt) + " " + converter_from(txt)


def converter_select(txt):
    return "π " + validar_sql(txt).get('campos').get('select')

def converter_join(txt):
    tabelas = []
    tabJoin = tabelasJoin(txt)
    campos = campos_join(txt)
    for i in range(len(tabJoin)):
        if i == 0:
            tabelas.append(tabelaFrom(txt))
        tabelas.append(tabJoin[i])

    aux = "("
    for i in range(len(tabelas) - 1):
        aux = f"{aux} {tabelas[i]} |x| {campos[i]}"
    aux = f'{aux} {tabelas[len(tabelas) - 1]} )'

    return aux

def campos_join(txt):
    string_from = validar_sql(txt).get('campos').get('from')
    campos = re.findall(r'\w+\.\w+\s*=\s*\w+\.\w+', string_from)
    return campos


def converter_from(txt):
    if txt.__contains__('join'):
        return converter_join(txt)
    else:
        return tabelaFrom(txt)

def converter_where(txt):
    return "σ " + validar_sql(txt).get('campos').get('where')
