import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    customer_id = req.form['customer_id']
    tx_amount = req.form['tx_amount']

    # API URL with placeholders
    api_url = f"https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run?customer_id={customer_id}&date=2021-02-04T19:48:17.000Z&terminal_id=7&tx_amount={tx_amount}&tx_id=4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062&tx_payment=POS"

    response = requests.get(api_url)
    return func.HttpResponse(response.text, mimetype="application/json")
