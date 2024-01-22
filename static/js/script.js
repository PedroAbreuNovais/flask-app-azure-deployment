document.getElementById('ccForm').onsubmit = function(event) {
    event.preventDefault();

    // Fetch form data
    var formData = new FormData(document.getElementById('ccForm'));

    // Send data to Flask backend
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response data
    })
    .catch(error => {
        console.error('Error:', error); // Handle errors
    });
};
