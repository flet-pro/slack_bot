import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

def printout_to_slack(text):
    client.chat_postMessage(channel='#random', text=text)

def printout_mention_message(user_id, text):
    client.chat_postMessage(channel='#random', text="<@{}> {}".format(user_id, text))

users_list = client.users_list()['members']

for user in users_list:
    user_id = user['id']
    user_name = user['name']

    if not user['is_email_confirmed']:
        continue

    printout_mention_message(user_id=user_id, text=user_name)
    