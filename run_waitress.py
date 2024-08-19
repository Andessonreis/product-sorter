import sys
import os
from waitress import serve

# Altere o diretório de trabalho para o diretório do projeto
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Importar o app
from backend.app import app

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
