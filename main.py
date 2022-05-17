#"main"

from arvore import arvore_inicial
import validarCampos, validarFormatoSQL, conversor

txt = "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descrição from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario join tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta where saldoinicial < 3000 and uf = 'ce' and Descrição <> 'Conta Corrente' and idusuario > 3"
txt2 = "Select nome, datanascimento, descricao, saldoinicial from usuario join contas on usuario.idUsuario = contas.Usuario_idUsuario where saldoinicial >= 235 and uf = ce and cep <> 62930000"
txt = txt.lower()
txt2 = txt2.lower()

sql_valido = validarFormatoSQL.validar_sql(txt2)
campos_valido  = validarCampos.validar(txt2)
if sql_valido and campos_valido:
    print(conversor.priest(txt))
    arvore_inicial(txt)