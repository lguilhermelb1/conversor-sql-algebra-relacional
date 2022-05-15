#"main"

import validarCampos, validarFormatoSQL, conversor

txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = ce and cep <> 62930000"
txt = txt.lower()

resultado = validarFormatoSQL.validar_sql(txt)
validarCampos.validar(txt)

print(conversor.converteTudo(txt))
print("\n")
print(resultado.get('campos'))