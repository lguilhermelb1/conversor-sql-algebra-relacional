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
txt = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >=235 and uf ='ce' and cep <> '62930000"
txt = txt.lower()
validate = re.search("^(?=.*select.*from.)", txt)






if validate:
  print("YES! We have a match!")
else:
  print("No match")




