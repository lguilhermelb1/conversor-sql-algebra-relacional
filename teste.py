#  Funcionalidades principais: 
#  a. Parser (Análise) de uma consulta SQL; 
#  b. Geração do grafo de operadores da consulta; 
#  c. Ordem de execução da consulta; 
#  d. Exibição dos resultados na interface gráfica; 

# Operadores permitidos:
# i. Select, From, Where, Join (duas ou mais tabelas); 
# ii. Operadores (=, >, <, <=, >=, <>, And, In, Not In); 


# Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >=235 and uf ='ce' and cep <> '62930000';

import re

#txt = input("Type something to test this out: ")
txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario2 = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = 'ce' and cep <> 62930000"
txt = txt.lower()
txt2 = txt2.lower()

validate = re.fullmatch(r'\s*select\s+(?P<select>(\w+\s*\,\s*)*(\w+)+)\s+from\s+(?P<from>(\w+){1}(\s+join\s+\w+\s+on\s+\w+\.\w+\s=\s*\w+\.\w+)*)\s+where\s+(?P<where>(\w+\s*(>|<|=|<>|<=|>=)\s*(\w+|(\'\w+\'|\"\w+\")))(\s+(and|in|not\s{1}in){1}\s+(\w+\s*(>|<|=|<>|<=|>=)\s*(\w+|(\'\w+\s?\w+\'|\"\w+\s?\w+\"))))*)', txt)
validate2 = re.fullmatch(r'\s*select\s+(?P<select>(\w+\s*\,\s*)*(\w+)+)\s+from\s+(?P<from>(\w+){1}(\s+join\s+\w+\s+on\s+\w+\.\w+\s=\s*\w+\.\w+)*)\s+where\s+(?P<where>(\w+\s*(>|<|=|<>|<=|>=)\s*(\w+|(\'\w+\'|\"\w+\")))(\s+(and|in|not\s{1}in){1}\s+(\w+\s*(>|<|=|<>|<=|>=)\s*(\w+|(\'\w+\s?\w+\'|\"\w+\s?\w+\"))))*)', txt2)

print(validate.groupdict())

if validate:
  print("YES! We have a match!")
  print(validate.groupdict())
else:
  print("No match")

if validate2:
  print("YES! We have a match!")
  print(validate2.groupdict())
else:
  print("No match")