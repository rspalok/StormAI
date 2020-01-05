from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from oauth2client import file,client,tools
import argparse
from oauth2client.client import GoogleCredentials
import stormApp

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES1= ['https://www.googleapis.com/auth/calendar']
def googleCalender():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar
    """
    print("Inside open calender")
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

def get_events(n,service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        stormApp.speak('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        stormApp.speak(start + " " +event['summary'])

    return

def setEvent(summary,startTime,endTime):
    stormApp.speak("in side save event" + summary)
    print("in side save event" + summary+"  "+startTime+"  "+endTime)
    try:
        print('in try block')
        flags=argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    #stormApp.speak("in side save event " + summary)
    store=file.Storage('storage.json')
    creds=store.get()
    if not creds or creds.invalid:
        flow=client.flow_from_clientsecrets('credentials.json',SCOPES1)
        creds=tools.run_flow(flow,store,flags)\
            if flags else tools.run(flow,store)
    CAL=build('calendar','v3',http=creds.authorize(Http()))

    EVENT={
        'summary':summary,
         'start': {
            'dateTime': '2020-01-06T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
          },
            'end': {
            'dateTime': '2020-01-06T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
          }
    }
    event=CAL.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute()

    print(event['summary'].encode('utf-8'),
      event['start']['dateTime'], event['end']['dateTime'])
    # stormApp.speak((event['summary'].encde('utf-s'),
    #                event['start']['dateTime'],event['end']['dateTime']))
