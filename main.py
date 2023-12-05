from googleapiclient.discovery import build

# Your API key
api_key = "AIzaSyBuo_Nll9xnkyRS08Yl6PBapYHS6LV1tLI"

# YouTube service
youtube = build("youtube", "v3", developerKey=api_key)

# Read the URLs from the file
with open("urls.txt", "r") as file:
    url_strings = file.readlines()
    # Remove newline characters from the end of each URL
    video_urls = [url.strip() for url in url_strings]

# Extract video IDs from URLs
video_ids = [url.split("v=")[-1] for url in video_urls]


# Function to add videos to a playlist
def add_videos_to_playlist(playlist_id, video_ids):
    try:
        for video_id in video_ids:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": 0,
                        "resourceId": {"kind": "youtube#video", "videoId": video_id},
                    }
                },
            )
            request.execute()
        print("Videos added successfully!")
    except Exception as e:
        print("An error occurred:", e)


# Example: Playlist ID where you want to add the videos
target_playlist_id = "PLk4MZCtqx56k6AQkb5pjkxdyzZ0Xyj_l"

# Add videos to the specified playlist
add_videos_to_playlist(target_playlist_id, video_ids)
