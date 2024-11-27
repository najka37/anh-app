function get_data(event){
    // Prevent form from submitting
    event.preventDefault();

    // Getting data from DOM
    var email = document.getElementById('my_email').value.trim();
    var password = document.getElementById('my_password').value.trim();

    // Get the error message container
    var error_message = document.getElementById('err_message');

    // Hide and clear previous error message
    error_message.style.display = 'none';
    error_message.innerHTML = '';

    // Validate if both fields are filled
    if (!email || !password) {
        error_message.style.display = 'block';
        error_message.innerHTML = 'Fadlan soo geli email-ka iyo password-ka labadaba.';
        return;
    }

    // Prepare data to be sent
    var data = {
        email: email,
        password: password
    };

    console.log("Waa tan Xogta lasoo helay:", data);

    // Send the data using fetch API
    fetch('/getData', {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(data),
        cache: 'no-cache',
        headers: new Headers({
            'content-type': 'application/json'
        })
    })
    .then(function(response) {
        if (response.status !== 200) {
            console.log("Waxaa cillad ka jirta marka xogta la diraayo.");
            error_message.style.display = 'block';
            error_message.innerHTML = 'Waan ka xunnahay, waxbaa qaldamay!';  // Error message in Somali
            return;
        }

        return response.json();  // Parse JSON response
    })
    .then(function(data) {
        console.log("Fiiri xogta lasoo celiyay:", data);

        if (data['status'] === 'success') {
            // Success: Redirect to dashboard
            window.location.href = '/users/dashboard';
        } else {
            // Error: Display error message
            error_message.style.display = 'block';
            error_message.innerHTML = data['message'];
        }
    })
    .catch(function(error) {
        console.log("Waxaa error ka jira fetch operation:", error);
        error_message.style.display = 'block';
        error_message.innerHTML = 'Waxbaa qaldamay! Fadlan markale isku day.';
    });
}
