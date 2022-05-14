#"main"

import validarCampos, validarFormatoSQL, conversor

txt = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = ce and cep <> 62930000"
txt = txt.lower()

resultado = validarFormatoSQL.validar_sql(txt)
validarCampos.validar(txt)

print(conversor.conversorSelect(txt))
print(resultado.get('campos'))
