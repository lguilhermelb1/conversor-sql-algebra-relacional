tabelas = {
    "Usuario": {
        "atributos": [
            "idUsuario",
            "Nome",
            "Logradouro",
            "Número",
            "Bairro",
            "Cep",
            "UF",
            "DataNascimento"
        ]
    },
    "TipoConta": {
        "atributos": [
            "idTipoConta",
            "Descrição"
        ]
    }, "Contas": {
        "atributos": [
            "idConta",
            "Descricao",
            "TipoConta_idTipoConta",
            "Usuario_idUsuario",
            "SaldoInicial"
        ]
    },
    "Movimentacao": {
        "atributos": [
            "idMovimentacao",
            "DataMovimentacao",
            "Descricao",
            "TipoMovimento_idTipoMovimento",
            "Categoria_idCategoria",
            "Contas_idConta",
            "valor"
        ]
    }, "TipoMovimento": {
        "atributos": [
            "idTipoMovimentacao",
            "DescMovimentacao"
        ]
    }, "Categoria": {
        "atributos": [
            "idCategoria",
            "DescCategoria"
        ]
    }

}
