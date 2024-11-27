function register_user(event) {
    // Prevent form from submitting
    event.preventDefault();

    // Getting data from DOM
    var name = document.getElementById('my_name').value.trim();
    var email = document.getElementById('my_email').value.trim();
    var password = document.getElementById('my_password').value;
    var confirm_password = document.getElementById('confirm_password').value;
    var error_message = document.getElementById('err_message'); // Error message container

    // Reset error message display
    error_message.style.display = 'none';
    error_message.innerHTML = ''; // Clear previous error messages

    // Email validation regex (simple version)
    var email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Check if all fields are filled
    if (!name || !email || !password || !confirm_password) {
        error_message.style.display = 'block';
        error_message.innerHTML = "Fadlan buuxi dhammaan field-yada!";
        return;
    }

    // Check if the email format is valid
    if (!email_regex.test(email)) {
        error_message.style.display = 'block';
        error_message.innerHTML = "Fadlan soo geli email sax ah!";
        return;
    }

    // Check if password meets complexity (at least 6 characters)
    if (password.length < 6) {
        error_message.style.display = 'block';
        error_message.innerHTML = "Password-ka waa inuu ka koobnaadaa ugu yaraan 6 god!";
        return;
    }

    // Check if passwords match
    if (password !== confirm_password) {
        error_message.style.display = 'block';
        error_message.innerHTML = "Labada password isma lahan!";
        return;
    }

    // If all validations pass, send data to the server
    var data = {
        name: name,
        email: email,
        password: password,
        confirm_password: confirm_password
    }

    // Sending the data using fetch API
    fetch('/getSignupData', {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(data),
        cache: 'no-cache',
        headers: new Headers({
            'content-type': 'application/json'
        })
    })
    .then(function(response) {
        return response.json();  // Parse the JSON response
    })
    .then(function(data) {
        if (data['status'] === 'success') {
            // Success message
            alert(data['message']);
            // Redirect to the sign-in page after successful registration
            window.location.href = '/signin';
        } else {
            // Show error message from server
            error_message.style.display = 'block';
            error_message.innerHTML = data['message'];
        }
    })
    .catch(function(error) {
        console.log("Waxaa error ka jira fetch operation:", error);
        error_message.style.display = 'block';
        error_message.innerHTML = "Waxbaa qaldamay! Fadlan markale isku day.";
    });
}
