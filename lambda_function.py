# If slack_chatbot_type is 'webhook',
# needs information is 'Slack Webhook Url' only.
# If slack_chatbot_type is 'bot_token',
# need information are 'Bot Token' and 'Channel Id'.

import json
import requests

def lambda_handler(event, context):
    data_from_sns = json.loads(event['Records'][0]['Sns']['Message'])
    slack_chatbot_type = data_from_sns['responsePayload']['slack_chatbot_type']
    message = data_from_sns['responsePayload']['message']
    
    if (slack_chatbot_type == 'webhook'):
        post_url = data_from_sns['responsePayload']['slack_webhook_url']
        headers = {
            'Content-type':'application/json'
        }
        body = {
            'text': message
        }
        requests.post(url=post_url, headers=headers, json=body)
    elif (slack_chatbot_type == 'bot_token'):
        post_url = 'https://slack.com/api/chat.postMessage'
        bot_token = data_from_sns['responsePayload']['bot_token']
        channel_id = data_from_sns['responsePayload']['channel_id']
        data = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'token': bot_token,
            'channel': channel_id, 
            'text': message
        }
        requests.post(url=post_url, data=data)