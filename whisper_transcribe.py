import yt_dlp
import whisper
import os
import argparse
import torch
import warnings as w

w.simplefilter("ignore")

def download_audio_from_youtube(url, output_path="audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_path

def whisper_transcript(video_url):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Ses dosyasını indir
    audio_path = download_audio_from_youtube(video_url, "audio") + ".mp3"
    
    # Whisper modelini yükle
    model = whisper.load_model("small", device=device)
    
    # Ses dosyasını transkript yap
    result = model.transcribe(audio_path)
    
    # Geçici dosyayı temizle
    os.remove(audio_path)
    
    return result['text']

if __name__ == "__main__":
    # Argümanları alma
    parser = argparse.ArgumentParser(description="YouTube videosunu transkripte çevir.")
    parser.add_argument('url', type=str, help="YouTube video linki")
    
    args = parser.parse_args()
    
    # Transkript işlemi
    transcript = whisper_transcript(args.url)
    print(transcript)
