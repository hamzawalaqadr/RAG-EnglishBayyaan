from pytube import Playlist
import os

def download_playlist_videos(playlist_url, format_type):
    try:
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            if format_type == 'mp3':
                audio_stream = video.streams.filter(only_audio=True).first()
                output_file = audio_stream.download()
                base, ext = os.path.splitext(output_file)
                new_file = base + '.mp3'
                os.rename(output_file, new_file)
                print(f"Audio downloaded successfully: {new_file}")
            else:
                video_stream = video.streams.get_highest_resolution()
                output_file = video_stream.download()
                print(f"Video downloaded successfully: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

playlist_url = input("Enter the YouTube playlist URL: ")
format_choice = input("Enter 'mp4' for video or 'mp3' for audio: ").lower()
if format_choice not in ['mp4', 'mp3']:
    print("Invalid format choice.")
else:
    download_playlist_videos(playlist_url, format_choice)