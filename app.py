from flask import Flask, render_template, request
import random
from twilio.rest import TwilioRestClient

account = "<enter account sid here>"
token = "<enter auth token here>"
client = TwilioRestClient(account, token)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process')
def process():
    # write any python code here.

    amount = random.choice(range(3, 8))
    order  = request.args['order']
    message = client.messages.create(to="+17327252998", from_="+1 7328527245", body="Someone ordered %s " % (order))
    return render_template('thanks.html', amount=amount, order=order)


if __name__ == '__main__':
    app.run(debug=True)
