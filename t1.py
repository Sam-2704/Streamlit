import streamlit as st
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up Streamlit app
st.title('Daily Email Activity Tracker')
email = st.text_input('Enter your email ID:')
start_date = st.date_input('Select start date:')
end_date = st.date_input('Select end date:')

# Connect to Gmail API and fetch data
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('gmail', 'v1', credentials=creds)

def fetch_emails(start_date, end_date):
    query = f'after:{start_date} before:{end_date}'
    result = service.users().messages().list(userId='me', q=query).execute()
    return result['messages']

# Display data using Streamlit
if email:
    st.write(f'Daily email activity for {email}:')
    st.write(f'Number of emails received: {len(fetch_emails(start_date, end_date))}')
    # Add more visualizations as needed
