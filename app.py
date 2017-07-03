# coding: utf-8


import os
import requests
from flask import  Flask, request, jsonify, render_template, redirect, url_for

app = Flask('__name__')
app.config.from_object('config.Development')


SLACK_GROUP = os.environ.get('SLACK_GROUP', 'YOUR_GROUP_NAME')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', 'TOKEN_GROUP')
SLACK_URL = 'https://%s.slack.com' % SLACK_GROUP

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/invite', methods=['GET', 'POST', ])
def invite():
    if request.method == 'POST':
        data = {'email': request.values['email'],'token': SLACK_TOKEN,
                'set_active': 'true'}
        c = requests.post('{}/api/users.admin.invite'.format(SLACK_URL),
                          params=data).json()
        return render_template('invite.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
