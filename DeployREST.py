from flask import Flask, jsonify, escape
import hashlib

# Create the main Flask app object
app = Flask(__name__)

# Set '/md5' app route
@app.route('/md5')
# Set '/md5/' app route
@app.route('/md5/')
# Build function 
def default_md5():
# Encode 'Hello World' as md5
  hello_md5 = hashlib.md5('Hello World'.encode('utf-8')).hexdigest() 
  # Return JSON payload consisting of input value and output value
  return {"input": 'Hello World', "output": hello_md5}

# Set '/md5/<string>' app route
@app.route('/md5/<string>/')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):  
  # Encode default_string as md5
  string_to_md5 = hashlib.md5(escape(string).encode('utf-8')).hexdigest()
 
  # Return JSON payload consisting of input value and output value
  return {"input": string, "output": string_to_md5}

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
    
#This endpoint is the only one that has a side-effect. Your API should attempt to post the value of the input into a Slack channel in our class Slack team, then return a boolean value that indicates whether the message was successfully posted to the channel. 
#instaall slack client
pip install slackclient
import slack
#connect slack token
SLACK_TOKEN="<xoxb-4176399459060-4173888784227-TEB1KPyN1XJzJB5EL4JasfrV>”
#apptext
client = slack.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='#justtest',text='>^..^<')
#install flask and event
$ pip install flask

$ pip install slackeventsapi
#create flask app
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
 
SLACK_TOKEN="<xoxb-4176399459060-4173888784227-TEB1KPyN1XJzJB5EL4JasfrV>"
SIGNING_SECRET="<c1adeb5ae4fea9963fc9939accf460f2>"
 
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
 
client = slack.WebClient(token=SLACK_TOKEN)
 
@ slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
 
    if text == "Hi":
        client.chat_postMessage(channel=channel_id,text=">^..^<")
 
if __name__ == "__main__":
    app.run(debug=True)
