from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import io
import os

# Escopo de permissão
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def autenticar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def baixar_arquivo(file_id, nome_saida):
    creds = autenticar()
    service = build('drive', 'v3', credentials=creds)

    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Progresso: {int(status.progress() * 100)}%")

    # Salvar arquivo no disco
    fh.seek(0)
    with open(nome_saida, 'wb') as f:
        f.write(fh.read())
    print(f"Arquivo salvo como {nome_saida}")

# Exemplo de uso
# baixar_arquivo('1aBcD_eFgHiJkLmNoPqRsTuVwXyZ', 'meu_arquivo.pdf')   
