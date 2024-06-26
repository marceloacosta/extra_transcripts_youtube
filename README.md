# YouTube Transcript Fetcher

This Python script fetches and saves transcripts for a list of YouTube video URLs. It uses the `youtube_transcript_api` to retrieve transcripts and `pytube` to fetch video titles.

## Project Aim

The aim of this project is to provide a simple and efficient way to download and save transcripts of multiple YouTube videos into a text file. This can be particularly useful for creating study materials, research, or content analysis.

## Features

- Fetches video titles using `pytube`.
- Retrieves transcripts using `youtube_transcript_api`.
- Formats and saves transcripts into a single text file.

## Installation

To use this script, you'll need to have Python installed along with the required packages. You can install the necessary packages using pip:

```sh
pip install youtube_transcript_api pytube
```

## Usage

1. Prepare a list of YouTube URLs for which you want to fetch transcripts.
2. Run the script with the URLs list to fetch and save the transcripts.

### Example

```python
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
```

## Error Handling

The script includes error handling for various scenarios:

- **Video Title Fetching Errors**: Prints an error message if the video title cannot be fetched.
- **Transcript Disabled**: Skips the video and prints a message if transcripts are disabled.
- **No Transcript Found**: Skips the video and prints a message if no transcript is available.
- **General Errors**: Prints a message for any other errors encountered.

## License

This project is licensed under the MIT License.

