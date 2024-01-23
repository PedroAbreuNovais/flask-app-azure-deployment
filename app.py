from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    # Extracting data from the form
    customer_id = request.form.get('customer_id')
    tx_amount = request.form.get('tx_amount')

    # Static data (as per your API requirement)
    date = "2021-02-04T19:48:17.000Z"
    terminal_id = "7"
    tx_id = "4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062"
    tx_payment = "POS"

    # Construct the API URL with the data
    api_url = f"https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run?customer_id={customer_id}&date={date}&terminal_id={terminal_id}&tx_amount={tx_amount}&tx_id={tx_id}&tx_payment={tx_payment}"

    # Make a GET request to the external API
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return jsonify(response.json())  # Return the JSON response from the API
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
