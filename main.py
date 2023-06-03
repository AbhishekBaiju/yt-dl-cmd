import os
from pytube import Playlist, YouTube
import urllib.parse
from tqdm import tqdm


def download_video(url, folder, number_videos, skip_existing):
    try:
        playlist = Playlist(url)
        videos = playlist.video_urls

        download_path = os.path.join(os.getcwd(), folder)
        os.makedirs(download_path, exist_ok=True)

        for i, video in enumerate(tqdm(videos, desc="Downloading"), start=1):
            youtube = YouTube(video)
            stream = youtube.streams.get_highest_resolution()

            if number_videos:
                title = f'{i:02d} : {youtube.title}'
            else:
                title = youtube.title

            filename = f'{title}.{stream.subtype}'

            file_path = os.path.join(download_path, filename)
            if skip_existing and os.path.exists(file_path):
                tqdm.write(f'Skipping existing file: {filename}')
                continue

            stream.download(output_path=download_path, filename=filename)

            tqdm.write(f'Downloaded video {i}/{len(videos)}: {filename}')

        print('Download complete!')
    except Exception as e:
        print('Error:', str(e))


def main():
    print('beepboop..')

    url = input('Enter the YouTube video or playlist link: ')
    folder = input('Enter the download folder name: ')
    number_videos = input('Should the videos be numbered in the playlist order? (Y/N): ')
    number_videos = number_videos.lower() == 'y'
    skip_existing = input('Should existing files be skipped? (Y/N): ')
    skip_existing = skip_existing.lower() == 'y'

    download_video(url, folder, number_videos, skip_existing)


if __name__ == '__main__':
    main()
