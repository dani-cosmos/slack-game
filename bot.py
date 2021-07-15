import slack
import os
import slack_game
from pathlib import Path
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter
from flask import Flask, Request, Response

#better to load it from the .env file because it's sensitive info
env_path = Path(',') / '.env'
load_dotenv() #give env_path as a variable and then remove it if this module bugs

app = Flask(__name__) # __name__ - python variable containing the name of the file
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
slack_events_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'],'/slack/events', app)

BOT_ID = client.api_call('auth.test')['user_id']

# Listen to all messages
@slack_events_adapter.on('message')
def message(payload):

    channel_type = payload.get('event').get('channel_type')

    if channel_type == 'channel':
        pass
    if channel_type == 'im':
        pass

# Slash command
@app.route('/start-game', methods=['POST'])
def start_game():
    data = Request.form
    channel_id = data.get('channel-id')
    return Response(), 200


if __name__ == "__main__": # if we ran this file directly (not with include), run the web server
    app.run(debug=True, port=5000)
