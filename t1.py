import streamlit as st
pip install google.oauth2.credentials
pip install google_auth_oauthlib.flow 
pip install googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

# Set up Streamlit app
st.title('Gmail UI Integration')
st.write('Please authenticate your Gmail account to proceed.')

# Set up authentication
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CLIENT_SECRETS_FILE = 'client_secrets.json'
flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
auth_url, _ = flow.authorization_url(access_type='offline')
auth_code = st.text_input('Enter the authorization code:')
if auth_code:
    flow.fetch_token(authorization_response=auth_code)

# Connect to Gmail API and fetch data
creds = Credentials.from_authorized_user_info(info=flow.credentials.to_json())
service = build('gmail', 'v1', credentials=creds)

# Example: Fetch all emails from inbox
results = service.users().messages().list(userId='me', q='in:inbox').execute()
messages = results.get('messages', [])

# Display data using Streamlit
if messages:
    st.write('Your inbox contains the following messages:')
    for message in messages:
        message_data = service.users().messages().get(userId='me', id=message['id']).execute()
        st.write(message_data['snippet'])
else:
    st.write('Your inbox is empty.')
