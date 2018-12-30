from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))



    event = {
        'summary': 'I/O 2015 CCC',
        'location': 'مرکز رایانش ابری، دانشکده مهندسی کامپیوتر، دانشگاه علم و صنعت ایران',
        'description': 'اتمام محدوده زمانی مجاز برای استفاده از ماشین مجازی',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() + 'Z', # '2015-05-28T09:00:00-07:00',
            'timeZone': 'Asia/Tehran',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat() + 'Z', #'2015-05-28T17:00:00-07:00',
            'timeZone': 'Asia/Tehran', #'America/Los_Angeles',
        },
        # 'recurrence': [
        #     'RRULE:FREQ=DAILY;COUNT=2'
        # ],
        'attendees': [
            {'email': 'mohsenfarahanchi@outlook.com'},
            # {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + '+3:30' # 'Z' indicates UTC time
    print('Getting the upcoming 20 events')
    events_result = service.events().list(calendarId='primary', #timeMin=now,
                                        maxResults=20, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        try:
            print(start, event['summary'])
        except Exception:
            print("some error")

    # reminder_result = service.reminders().list().execute()
    # reminders = reminder_result.get('items', [])
    # print(reminders)

if __name__ == '__main__':
    main()
