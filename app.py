import os
import json
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = "data/spotify"
YEAR = os.environ.get("YEAR")


def get_listening_time(filepath: str) -> int:
    """
    Get the total time listened to music in a year from the Spotify streaming history data file provided.

    Args:
        filepath (str): The name of the file containing the Spotify streaming history data.

    Returns:
        int: The total time listened to music in milliseconds.
    """
    total_ms_played = 0
    with open(f"{DATA_DIR}/{filepath}", "r") as file:
        file_data = json.load(file)

    for song in file_data:
        if song["endTime"].startswith(str(YEAR)):
            total_ms_played += song["msPlayed"]

    return total_ms_played


def get_time_in_minutes_and_seconds(time_in_seconds: int) -> str:
    """Get the time in minutes and seconds from the time in seconds provided.

    Args:
        time_in_seconds (int): The time in seconds.

    Returns:
        str: The time in minutes and seconds.
    """
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    return f"{minutes} mins and {seconds} secs"


def get_time_in_hours_mins_and_secs(time_in_seconds: int) -> str:
    """Get the time in hours, minutes and seconds from the time in seconds provided.

    Args:
        time_in_seconds (int): The time in seconds.

    Returns:
        str: The time in hours, minutes and seconds.
    """
    hours = time_in_seconds // 3600
    remaining_seconds = time_in_seconds % 3600
    mins_and_secs = get_time_in_minutes_and_seconds(remaining_seconds)
    return f"{hours} hours and {mins_and_secs}"


def main():
    if not YEAR:
        print(
            "Please provide the year for which you want to calculate the total time listened to music."
        )
        return
    if not os.path.exists(DATA_DIR):
        print("The data directory does not exist.")
        return

    all_spotify_files = os.listdir(DATA_DIR)
    streaming_history_files = [
        file for file in all_spotify_files if "streaminghistory_music" in file.lower()
    ]

    total_ms_played = 0
    for streaming_data_file in streaming_history_files:
        total_ms_played += get_listening_time(streaming_data_file)

    time_in_seconds = total_ms_played // 1000
    time_in_minutes_and_seconds = get_time_in_minutes_and_seconds(
        time_in_seconds=time_in_seconds
    )
    time_in_hours_minutes_and_seconds = get_time_in_hours_mins_and_secs(
        time_in_seconds=time_in_seconds
    )

    print(f"Time in seconds - {time_in_seconds}")
    print(f"Time in minutes and seconds - {time_in_minutes_and_seconds}")
    print(f"Time in hours, minutes and seconds - {time_in_hours_minutes_and_seconds}")


if __name__ == "__main__":
    main()
