import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# Define os escopos que você vai precisar (permite acessar vídeos não listados)
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# Especifica o arquivo com as credenciais
CLIENT_SECRETS_FILE = "client_secret_youtube.json"

def youtube_auto():
    # Criando o fluxo OAuth
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)

    # Executando o fluxo de autenticação
    credentials = flow.run_local_server(port=8080)

    # Criando o cliente da API do YouTube
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    return youtube

def get_videos_from_channel(youtube):
    request = youtube.search().list(
        part="snippet",
        forMine=True,
        type="video",
        maxResults=50
    )
    response = request.execute()

    # Processa os resultados
    videos = []
    for item in response['items']:
        video_name = item['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append((video_name, video_url))

    return videos

def get_files(root):
    f = []
    f_names = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.mp4') or name.endswith('.mov'):
                f.append(os.path.join(path, name))
                f_names.append(name)
    
    return f, f_names

def compare_videos(files, yt_videos):
    return

if __name__ == "__main__":
    youtube_client = youtube_auto()
    video_links = get_videos_from_channel(youtube_client)
    root = '..\\FOTOS MARI BACKUP'
    files, filenames = get_files(root)
    yt_names = ['_'.join(name.split(' ')) + '.mp4' for name, link in video_links]
    print(f'Youtube Names : {yt_names}')
    for file, filename in zip(files, filenames):
        if filename not in yt_names:
             print(f'{filename} : {file}')
        else:
            print('------------------- ', filename)

    """for name, link in video_links:
        nm = name.split(' ')
        nm = '_'.join(nm) + '.mp4'
        if nm not in filenames:
            print(f'{name} : {link}')
        else:
            print('------------------- ', name)"""
