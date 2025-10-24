import requests
from src.logger_config import log


def realiza_login(cookie_session= None, usuario = None, senha = None):
    """
    Login adaptável: usa cookie ou usuário/senha.
    Retorna a sessão autenticada.

    """

    try:
        url_dashboard = "https://desafio-rpa-946177071851.us-central1.run.app/challenger/dashboard"
        url_login =     "https://desafio-rpa-946177071851.us-central1.run.app/auth/authenticate"

        sessao = requests.Session()
        sessao.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Referer": url_dashboard,
        })

        # Login via cookie
        if cookie_session:
            log.info("Iniciando autenticação baseado em cookie da sessão do usuário")
            sessao.cookies.set("ci_session", cookie_session)

            for tentativa in range(1,4):
                log.info(f"Iniciando tentativa de conexão com sessão de numero {tentativa}")
                response_dashboard = sessao.get(url_dashboard, allow_redirects=False, verify=False)
                if response_dashboard.status_code == 200:
                    log.info("Sessão conectada com sucesso")
                    return sessao

            raise Exception(f"Falha ao validar sessão após {tentativa} tentativas.")

        # Login via usuário e senha
        elif usuario and senha:
            log.info("Iniciando Login com autenticação utilizando usuario e senha.")
            payload = {"username": usuario, "password": senha} 
            for tentativa in range(1,4):
                log.info(f"Iniciando tentativa de login de numero {tentativa}")
                response_login = sessao.post(url_login, data=payload, verify=False)
                if response_login.status_code == 200:
                    log.info(f"Login realizado com sucesso.")
                    return sessao
                log.info(f"Falha ao realizar login de tentativa {tentativa}")
                    
            raise Exception(f"Falha ao realizar login após todas tentativas. Total: {tentativa}") 
  
        else:
            raise Exception("Informe cookie ou usuário e senha para login")
        

    except Exception as exc:
        log.error(f"Erro ao realizar login: {exc}")
        raise
