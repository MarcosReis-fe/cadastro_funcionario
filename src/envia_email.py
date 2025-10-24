import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.logger_config import log


#Insira seu e‑mail e a senha de app gerada especificamente para envio/integração. Essa senha é diferente da senha de login da sua conta de e‑mail.

def dispara_email(titulo, mensagem):

    try:
    
        email_remetente = "marcosraves2@gmail.com"
        senha = ""  
        email_destino = "marcosreisdev@hotmail.com"
        
        # Monta a menssagem com base no corpo nos parametros
        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = email_destino
        msg['Subject'] = titulo
        msg.attach(MIMEText(mensagem, 'plain'))

        # Abre conexao com o servidor SMTP/gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # ativa criptografia
            server.login(email_remetente, senha)
            server.send_message(msg)
            log.info("E-mnail enviado com sucesso!!!")

    except Exception as exc:
        log.error("Erro ao enviar e-mail") 
