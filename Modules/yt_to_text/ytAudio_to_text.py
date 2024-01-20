import os
import whisper
from langdetect import detect
from pytube import YouTube

def startfile(fn):
    os.system('open %s' % fn)

def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)
    startfile(filename)

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)
#for age restricted -> yt = YouTube(url,use_oauth=True, allow_oauth_cache=True)

audio_stream = yt.streams.filter(only_audio=True).first()

output_path = "YoutubeAudios"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

model = whisper.load_model("base")
result = model.transcribe("YoutubeAudios/audio.mp3")
transcribed_text = result["text"]
print(transcribed_text)

language = detect(transcribed_text)
print(f"Detected language: {language}")

create_and_open_txt(transcribed_text, f"output_{language}.txt")