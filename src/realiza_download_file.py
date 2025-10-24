import pandas as pd
import requests
import time
from src.logger_config import log


# ---------- BAIXAR PLANILHA ----------
def download_file(session):

    try:

        url_download_file = (
            "https://desafio-rpa-946177071851.us-central1.run.app/challenger/download"
        )

        for tentativa in range(1,3):

            log.info(f"Iniciando download da planilha de cadastro de tentativa {tentativa}.")
            response_file = session.get(url_download_file, verify=False)
            if response_file.status_code == 200:
                with open("employees.xlsx", "wb") as f:
                    f.write(response_file.content)
                log.info("Planilha de cadadtro baixada com sucesso!")
                # ---------- realiza a leitura da planilha baixada----------
                time.sleep(5)
                df = pd.read_excel("employees.xlsx", engine="openpyxl")
                return df
            log.error("Falha ao baixar planilha de cadastro.")
            

        raise Exception("Falha ao realizar download da planilha")

    except Exception as exc:
        log.error(f"Erro ao fazer download da planilha: {exc}")
        raise
