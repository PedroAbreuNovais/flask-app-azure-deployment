from flask import Flask, request, render_template, jsonify
import requests, pyodbc, os, uuid
from datetime import datetime
app = Flask(__name__)

# Database configuration from environment variables
#server = os.getenv('ccfdb.database.windows.net')
#database = os.getenv('ccfdb')
#username = os.getenv('adminpedro')
#password = os.getenv('9UAUGKqz=oF;T38wJNKj')
#driver = '{ODBC Driver 17 for SQL Server}'


# SQL commands to create the tables if they don't exist
#create_requests_table = """
#IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Requests' and xtype='U')
#CREATE TABLE Requests (
#    RequestId INT PRIMARY KEY IDENTITY(1,1),
#    CustomerId NVARCHAR(50),
#    TransactionAmount FLOAT,
#    TerminalId NVARCHAR(50),
#    TransactionPayment NVARCHAR(50),
#    RequestTime DATETIME
#);
#"""

#create_responses_table = """
#IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Responses' and xtype='U')
#CREATE TABLE Responses (
#    ResponseId INT PRIMARY KEY IDENTITY(1,1),
#    RequestId INT FOREIGN KEY REFERENCES Requests(RequestId),
#    ApiResponse NVARCHAR(MAX),
#    ResponseTime DATETIME
#);
#"""

# Initialize database connection and create tables if they don't exist
#def init_db():
#    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
#    cursor = conn.cursor()
 #   cursor.execute(create_requests_table)
 #   cursor.execute(create_responses_table)
 #   conn.commit()
 #   cursor.close()
  #  conn.close()

# Run the database initialization
#init_db()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    customer_id = request.form['customer_id']
    tx_amount = request.form['tx_amount']
    tx_payment =  request.form['tx_payment']
    terminal_id = request.form['terminal_id']
    date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    # Static data
    # date = "2021-02-04T19:48:17.000Z"
    #terminal_id = "7"
    
    # Generate a random UUID and convert to a hexadecimal string
    tx_id = uuid.uuid4().hex
    # tx_id = "4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062"
    #tx_payment = "POS"

  # Database connection
#    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
#    cursor = conn.cursor()

    # Insert request data into Requests table
 #   cursor.execute("INSERT INTO Requests (CustomerId, TransactionAmount, TerminalId, TransactionPayment, RequestTime) OUTPUT INSERTED.RequestId VALUES (?, ?, ?, ?, GETUTCDATE())", (customer_id, tx_amount, terminal_id, tx_payment))
 #   request_id = cursor.fetchone()[0]
 #   conn.commit()
    
    # API endpoint
    api_url = f"https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run?customer_id={customer_id}&date={date}&terminal_id={terminal_id}&tx_amount={tx_amount}&tx_id={tx_id}&tx_payment={tx_payment}"

    response = requests.get(api_url)

   # Insert response data into Responses table
  #  cursor.execute("INSERT INTO Responses (RequestId, ApiResponse, ResponseTime) VALUES (?, ?, GETUTCDATE())", (request_id, response.text))
  #  conn.commit()
    # Close the database connection
   # cursor.close()
   # conn.close()
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
