from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    customer_id = request.form['customer_id']
    tx_amount = request.form['tx_amount']
    terminal_id = 3 #request.form['terminal_id']
    tx_payment = "POS"#request.form['tx_payment']

    # Static data
    date = "2021-02-04T19:48:17.000Z"
    tx_id = "4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062"

    # API endpoint
    api_url = f"https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run?customer_id={customer_id}&date={date}&terminal_id={terminal_id}&tx_amount={tx_amount}&tx_id={tx_id}&tx_payment={tx_payment}"

    response = requests.get(api_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
