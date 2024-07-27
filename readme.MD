# Spotify Listening Time Analyzer

This repository allows you to analyze your Spotify listening time for a specific year.

## Prerequisites

1. Request and download your Spotify user data from [Spotify's Privacy Page](https://www.spotify.com/us/account/privacy/).
2. Ensure you have Python and `pip` installed on your system.

## Setup

Follow these steps to set up and run the project:

1. **Clone the Repository**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Prepare Your Data**
    - Extract your downloaded Spotify data.
    - Move the extracted data directory into the `data` directory in the root of this project.
    - Rename this directory to `spotify`.

3. **Install Dependencies**
    ```sh
    pip install python-dotenv
    ```
    Alternatively, you can install all required packages using:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the Environment**
    - Create a `.env` file in the root directory of the project.
    - Specify the `YEAR` you want to analyze in the `.env` file.
    ```env
    YEAR=2023
    ```

5. **Run the Application**
    ```sh
    python app.py
    ```

## Notes

- The data you receive will cover a one-year period ending on the date you requested the data. For example, if you request data on June 1, 2024, the data will cover from June 1, 2023, to June 1, 2024.

For any issues or questions, please refer to the [Issues](https://github.com/srtk-Negi/SpotifyListeningTime/issues) section of the repository.