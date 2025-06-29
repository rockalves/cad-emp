# Use uma imagem Python oficial como imagem base
FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /usr/src/app

# Copia o conteúdo do diretório atual para o container em /usr/src/app
COPY . .

# Instala as dependências necessárias.
# "textual[dev]" inclui ferramentas úteis para desenvolvimento.
RUN pip install "textual[dev]"

# Executa app.py quando o container for iniciado
CMD ["python", "app.py"]