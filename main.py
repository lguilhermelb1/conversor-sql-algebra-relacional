# "main"

import validarCampos
import validarFormatoSQL
import conversor
import interface

#txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
#txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = ce and cep <> 62930000"
txt = interface.consulta()
txt = txt.lower()

sql_valido = validarFormatoSQL.validar_sql(txt)
campos_valido = validarCampos.validar(txt)
if sql_valido and campos_valido:
    interface.resultado()
