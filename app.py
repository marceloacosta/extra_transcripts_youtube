import sys
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from youtube_transcript_api.formatters import TextFormatter
from pytube import YouTube

def get_video_title(url):
    """Fetch the video title using pytube."""
    try:
        yt = YouTube(url)
        return yt.title
    except Exception as e:
        print(f"Failed to fetch video title for URL: {url}. Reason: {str(e)}", file=sys.stderr)
        return None

def fetch_and_save_transcripts(urls, filename='transcripts.txt'):
    """Fetch transcripts for given YouTube URLs and save them to a file."""
    formatter = TextFormatter()
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            video_title = get_video_title(url)  # Fetch title using pytube
            if video_title is None:
                continue  # Skip if the title cannot be fetched

            try:
                video_id = YouTube(url).video_id
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                formatted_transcript = formatter.format_transcript(transcript)
                file.write(f"{video_title}\n{formatted_transcript}\n\n")
            except TranscriptsDisabled:
                print(f"Transcripts are disabled for URL: {url}", file=sys.stderr)
                continue
            except NoTranscriptFound:
                print(f"No transcript available for URL: {url}", file=sys.stderr)
                continue
            except Exception as e:
                print(f"Failed to download transcript for URL: {url}. Reason: {str(e)}", file=sys.stderr)
                continue


if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=iBa9EoEbb38&t=19s",
        "https://www.youtube.com/watch?v=yuy9yQlFZAU",
        "https://www.youtube.com/watch?v=Wasnm1xBmgI",
        "https://www.youtube.com/watch?v=yp-RvemofI4",
        "https://www.youtube.com/watch?v=thzDy5A-KfE",
        "https://www.youtube.com/watch?v=uvG0aCbuG60",
        "https://www.youtube.com/watch?v=9kj-FtX6Rv8",
        "https://www.youtube.com/watch?v=-Di_F87btMQ",
        "https://www.youtube.com/watch?v=a4XapXQdHhE",
        "https://www.youtube.com/watch?v=FZiuKziFI5w",
        "https://www.youtube.com/watch?v=Oxl3cDr0p9M",
        "https://www.youtube.com/watch?v=1kIYFIMzbZA",
        "https://www.youtube.com/watch?v=vJvXeJ0pf7o",
        "https://www.youtube.com/watch?v=80bymIwYrlI",
        "https://www.youtube.com/watch?v=RLLafx9xQgs",
        "https://www.youtube.com/watch?v=iBzHesG9j8M",
        "https://www.youtube.com/watch?v=oM4N9PZTaVM",
        "https://www.youtube.com/watch?v=OV6D6rrkMIw",
        "https://www.youtube.com/watch?v=o3e1lnixKBM",
        "https://www.youtube.com/watch?v=YoSKGchmBd8",
        "https://www.youtube.com/watch?v=7eTUq2QmWLI",
        "https://www.youtube.com/watch?v=EZ0fN0k4VfU",
        "https://www.youtube.com/watch?v=XCReTgSu884",
        "https://www.youtube.com/watch?v=BImww_TEMq8",
        "https://www.youtube.com/watch?v=1HSj8290iI4",
        "https://www.youtube.com/watch?v=MEJBnoTtsF4",
        "https://www.youtube.com/watch?v=3mEcdxYuD7M",
        "https://www.youtube.com/watch?v=7oKpFHPMjUU",

    
    ]

    fetch_and_save_transcripts(urls)
