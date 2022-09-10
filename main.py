import datetime as dt
import os

import slack
from dotenv import load_dotenv

load_dotenv(os.path.join(".env"))


def send_slack_alert(message, urgent=False, test=False):
    client = slack.WebClient(token=os.environ.get("SLACK_TOKEN"))
    if test:
        channel = "test-slack-bot"
    else:
        channel = "script-logs-bot"

    if urgent:
        client.chat_postMessage(channel=channel, text=message + " <!channel>")
    else:
        client.chat_postMessage(channel=channel, text=message)


send_slack_alert(f"test-slack-bot script executed\n datetime: {str(dt.datetime.now())}")
