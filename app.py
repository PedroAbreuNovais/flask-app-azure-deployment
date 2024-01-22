<!DOCTYPE html>
<html>
<head>
    <title>Credit Card Data Submission</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h2>Submit Credit Card Data</h2>
    <form id="ccForm">
        Customer ID: <input type="text" name="customer_id"><br>
        Transaction Amount: <input type="text" name="tx_amount"><br>
        <button type="submit">Submit</button>
    </form>

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
