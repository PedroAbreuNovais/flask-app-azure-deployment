document.getElementById('ccForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('API Response: ' + JSON.stringify(data));
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
});
