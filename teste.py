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

import re
import validarCampos

txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario2 = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = 'ce' and cep <> 62930000"
txt = txt.lower()
txt2 = txt2.lower()
# validate = re.search("^(?=.*select.*from.)", txt)


print(validarCampos.validar(txt))


# if validate:
#   print("YES! We have a match!")
# else:
#   print("No match")
