"""Request something from Google sheets."""
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_RANGE_NAME = 'A1:A4'


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    links_list = []
    if not values:
        print('No data found.')
    else:
        for link in values:
            links_list.append(link[0])
    return links_list


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.
    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    youtube_service = build("youtube", "v3", developerKey=developer_key)
    request = youtube_service.playlistItems().list(
        part="contentDetails",
        playlistId="PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK",
        maxResults=50
    )
    result = request.execute()
    all_videos = result["items"]
    all_video_links = []
    for video in all_videos:
        video_id = video["contentDetails"]["videoId"]
        all_video_links.append(f"https://youtube.com/watch?v={video_id}")
    return all_video_links
