document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    // You can use Fetch API or XMLHttpRequest to send data to the backend
    // Here's a simple example using Fetch API
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        window.location.href = '/dashboard'; // Redirect to dashboard on successful login
      } else {
        document.getElementById('message').innerText = data.message;
      }
    })
    .catch(error => console.error('Error:', error));
  });
  