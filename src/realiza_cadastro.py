from bs4 import BeautifulSoup
from src.logger_config import log 


def cria_cadastro(df, session):
    url_form = "https://desafio-rpa-946177071851.us-central1.run.app/challenger/register-form-only"
    url_save = "https://desafio-rpa-946177071851.us-central1.run.app/challenger/save"

    mapa_campos = {
        "nome": "Nome",
        "sobrenome": "Sobrenome",
        "email": "Email",
        "telefone": "Telefone",
        "endereço": "Endereço",
        "cargo": "Cargo",
        "empresa": "Empresa",
    }

    for _, row in df.iterrows():
        try:
            log.info(f"Iniciando cadastro do funcionário: {row['Nome']}")

            # Pega o HTML do formulário
            response_form = session.get(url_form, verify=False)
            soup = BeautifulSoup(response_form.text, "html.parser")

            payload = {}
            for campo in soup.find_all(["input", "textarea"]):
                name = campo.get("name")
                valor = campo.get("value", "")
                campo_id = campo.get("id")

                label = soup.find("label", {"for": campo_id})
                nome_label = label.text.strip()
                texto_label = nome_label.replace("*", "").replace(" ", "").lower()

                for chave, coluna in mapa_campos.items():
                    if chave == texto_label:
                        valor = str(row[coluna])
                        break

                payload[name] = valor

            # Tenta salvar o cadastro até 3 vezes
            for tentativa in range(1, 4):
                response = session.post(url_save, data=payload, allow_redirects=False, verify=False)

                if response.status_code in (200, 303):
                    log.info(f"Funcionário {row['Nome']} cadastrado com sucesso!")
                    break
                log.warning(f"Erro ao cadastrar {row['Nome']} (Tentativa {tentativa}")
            else:
                # Esse else executa se o for terminar sem break ou seja, sem sucesso
                raise Exception(f"Falha ao cadastrar o funcionário {row['Nome']} após 3 tentativas.")

        except Exception as exc:
            log.error(f"Houveram erros na criação de cdastros.")
            raise
