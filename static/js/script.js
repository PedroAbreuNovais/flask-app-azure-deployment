document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('ccForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(form);

        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('apiResponse').textContent = 'Error: ' + error;
        });
    });
});
