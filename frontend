from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from the form
    customer_id = request.form['customer_id']
    tx_amount = request.form['tx_amount']

    # Static data (as per your API requirement)
    date = "2021-02-04T19:48:17.000Z"
    terminal_id = "7"
    tx_id = "4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062"
    tx_payment = "POS"

    # Construct the API URL
    api_url = f"https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run?customer_id={customer_id}&date={date}&terminal_id={terminal_id}&tx_amount={tx_amount}&tx_id={tx_id}&tx_payment={tx_payment}"

    # Send request to the external API
    response = requests.get(api_url)

    # You can add error handling here based on the response

    return jsonify(response.json())  # or render a template with the response

if __name__ == '__main__':
    app.run()
