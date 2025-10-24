
import logging as log
import os
from datetime import datetime

# Cria pasta de logs se não existir
if not os.path.exists("logs"):
    os.makedirs("logs")

# Nome do arquivo com data e hora
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arquivo = f"logs/log_{data_hora}.log"

# Configuração global do log
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        log.FileHandler(nome_arquivo),
        log.StreamHandler()
    ]
)