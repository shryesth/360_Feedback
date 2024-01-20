from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

try:
    # Get the YouTube video URL from the user
    video_url = input("Enter the URL of the YouTube video you want to download: ")

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution stream
    video_stream = yt.streams.get_highest_resolution()

    # Download the video
    video_stream.download()

    # Get the video ID from the URL
    video_id = video_url.split("v=")[1]

    # Get the video transcript
    transcripts = YouTubeTranscriptApi.get_transcript(video_id)

    if transcripts:
        # Extract the transcripts as text
        subtitle_text = " ".join([entry["text"] for entry in transcripts])

        print("Transcripts:")
        print(subtitle_text)
    else:
        print("Transcripts not available for this video.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
