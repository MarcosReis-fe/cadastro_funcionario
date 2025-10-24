from src import login, realiza_download_file, realiza_cadastro, envia_email


# Selecione a opção abaixo:
# 1 - Caso queira ver o cadastro em tempo real. Nesse caso, será necessário fazer login e obter o cookie da sessão, e inserir na variavel abaixo.
# 2 - Caso não queira ver o cadastro em tempo real. Se a sua base de dados já possui um banco, poderá ver o cadastro feito, passando abaixo usuário e senha.
# Deixa um ou outro vazio

# --------------------
cookie_session = ""
user = "marcos.silva"
password = "OySQCac1tEAXIfvztlVm"

def main():
    try:
        session = login.realiza_login(cookie_session, user, password)

        df = realiza_download_file.download_file(session)

        realiza_cadastro.cria_cadastro(df, session)

        # se chegou até aqui, deu certo
        envia_email.dispara_email(
            titulo="Processo finalizado com sucesso.",
            mensagem="O Cadastro foi realizado sem erros!"
        )

    except Exception as exc:
        
        envia_email.dispara_email(
            titulo="Falha ao realizar cadastro",
            mensagem=f"O processo encontrou um erro:\n\n{exc}"
        )
    
if __name__ == "__main__":
    main()
