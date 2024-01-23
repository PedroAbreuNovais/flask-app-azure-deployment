document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('ccForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Fetch form data
        var formData = new FormData(form);

        // Send data to Flask backend
        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('API Response: ' + JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error: ' + error);
        });
    });
});
