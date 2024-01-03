from googleapiclient.discovery import build
from flask import Flask, render_template

app = Flask(__name__)

api_key = 'AIzaSyAm4fAS4OB4Tvks2I7_CRmseXssmEKVLHA'
playlist_id = 'PL9XxulgDZKuzf6zuPWcuF6anvQOrukMom'
def get_youtube_last_video(api_key, playlist_id):
    ytList=[]
    # Crea una instancia de la API de YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Obtiene la lista de reproducción
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=1,  # Puedes ajustar esto según tus necesidades
    ).execute()

    # Obtiene el ID del último video en la lista de reproducción
    video_id = playlist_items['items'][0]['snippet']['resourceId']['videoId']

    # Obtiene detalles del video
    video_details = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    # Extrae información del último video
    title = video_details['items'][0]['snippet']['title']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['high']['url']
    ytList.append(title)
    ytList.append(video_id)
    ytList.append(video_url)
    ytList.append(thumbnail_url)
    # Imprime información del último video
    print(f"Último video: {title}")
    print(f"ID del video: {video_id}")
    print(f"URL del video: {video_url}")
    print(f"URL de la miniatura: {thumbnail_url}")
    return ytList
def get_all_videos(api_key, playlist_id):
    allVideosList=[]
    # Crea una instancia de la API de YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Obtiene la lista de reproducción
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,  # Puedes ajustar esto según tus necesidades (50 es el máximo permitido)
    ).execute()

    # Itera sobre los videos en la lista de reproducción
    for item in playlist_items['items']:
        videoList=[]
        video_id = item['snippet']['resourceId']['videoId']
        video_details = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        # Extrae información del video
        title = video_details['items'][0]['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['high']['url']

        videoList.append(title)
        videoList.append(video_id)
        videoList.append(video_url)
        videoList.append(thumbnail_url)
        allVideosList.append(videoList)
        # Imprime información del video
        print(f"Video: {title}")
        print(f"ID del video: {video_id}")
        print(f"URL del video: {video_url}")
        print(f"URL de la miniatura: {thumbnail_url}")
        print("\n")
    return allVideosList

@app.route('/lastVideo')
def index1():
    return get_youtube_last_video(api_key, playlist_id)
@app.route('/allVideos')
def index2():
    return get_all_videos(api_key, playlist_id)
#if __name__ == "__main__":
    # Coloca tu clave de API y el ID de la lista de reproducción aquí


    #get_youtube_last_video(api_key, playlist_id)
    #get_all_videos(api_key, playlist_id)
if __name__ == '__main__':
    app.run(debug=True)