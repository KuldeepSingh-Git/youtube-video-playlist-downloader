*** YouTube Playlist & Video Downloader ***

This web application allows users to easily download YouTube videos and playlists. It's created using HTML, CSS, Python, and the Django framework.
The backend utilizes the `pytube` library to fetch video data from YouTube, including video titles, thumbnails, and available resolutions.

*** Prerequisites ***

Before you can use this project, you'll need to have the following prerequisites installed:
- Python 3.x
- Django==4.2.3
- pytube==15.0.0

*** Installation ***

1. Clone the repository to your local machine.
2. Navigate to the project directory on terminal.
3. Install the required Python packages.

*** Usage ***

1. Start the Django development server in the project directory on terminal:
      python manage.py runserver
2. Open your web browser and go to http://localhost:8000 to access the application.
3. Enter a valid YouTube video or playlist URL in the input field.
4. Click the "Download" button to retrieve information about the video or playlist.
5. Once the information is displayed, you can click on the desired video quality or format (if available) to initiate the download process.
6. The downloaded video(s) will be saved in the download folder of project directory.
