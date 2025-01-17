"""from flask import Flask

app = Flask('app')

@app.route('/command', methods = ['POST'])
def command():
    return 'tomate'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=13000)
"""
from flask import Flask, request
from slack_sdk import WebClient
import requests, json
from requests.auth import HTTPBasicAuth
import ie_slack_bot.sidequests as sq

client = WebClient ('xoxb-8280340257729-8267651468434-01niGleGfwnuXdu2NDpStwc1' )
app = Flask('app')

@app.route('/command', methods = ['POST'])
def command():
    return sq.sidequests()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=13000)