import re
from app import app
from flask import redirect, render_template, request, make_response, jsonify, session

@app.route('/signin')
def signin():
    return render_template('user/signin.html')

# Create an API endpoint to handle login data
@app.route("/getData", methods=['POST'])
def get_login_data():
    # Get the data from the request
    data = request.get_json()

    # Display the received data in the server console for debugging
    print("Xogtaada waa lasoo helay:", data)

    # Extract the email and password
    email = data.get('email')
    password = data.get('password')

    # Simple validation for demonstration purposes
    if email == 'najka@gmail.com' and password == '123':
        print("Xogtaadu way saxan tahay")  # This means "Your data is correct"

        # Store user data into the session
        session['email'] = email

        # Return success response
        my_response = {
            'message': 'Xogtaada xisaabtu way saxan tahay. Mahadsanid.',  # Message in Somali
            'status': 'success',
            'data': {}
        }
        return make_response(jsonify(my_response), 200)

    else:
        print("Maya, maya, maya, xogtaadu ma saxna!")  # This means "No, no, no, your data is incorrect"

        # Return error response
        my_response = {
            'message': 'Xogtaada xisaabtu way qaldan tahay fadlan iska hubi. Mahadsanid.',  # Incorrect data message in Somali
            'status': 'error',
            'data': {}
        }
        return make_response(jsonify(my_response), 200)


@app.route('/users/dashboard')
def open_user_dashboard():
    # return f"Kusoo dhawoow looxaaga, emailkaagu waa: {session.get('email')}"
    # Check if user is logged in
    if 'email' in session:
        return render_template('user/dashboard.html', email=session.get('email'))
    return redirect('/signin')

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

@app.route('/signup')
def signup():
    return render_template('user/signup.html')

# Create an API endpoint to handle signup data
@app.route("/getSignupData", methods=['POST'])
def get_signup_data():
    # Get the data from the request
    data = request.get_json()

    # Display the received data in the server console for debugging
    print(data)

    # Extract fields from data
    name = data.get('name').strip()
    email = data.get('email').strip()
    password = data.get('password').strip()
    confirm_password = data.get('confirm_password').strip()

    # Validate that all fields are filled
    if not name or not email or not password or not confirm_password:
        return make_response(jsonify({
            'message': 'Fadlan buuxi dhammaan field-yada!',
            'status': 'error'
        }), 200)

    # Validate email format
    if not is_valid_email(email):
        return make_response(jsonify({
            'message': 'Fadlan soo geli email sax ah!.',
            'status': 'error'
        }), 200)

    # Check if password length is valid
    if len(password) < 6:
        return make_response(jsonify({
            'message': 'Password-ka waa inuu ka koobnaadaa ugu yaraan 6 god!',
            'status': 'error'
        }), 200)

    # Check if passwords match
    if password != confirm_password:
        return make_response(jsonify({
            'message': 'Labada password isma lahan',
            'status': 'error'
        }), 200)

    # If all checks pass, respond with success
    print("Waa lagu diiwaan geliyay!")
    return make_response(jsonify({
        'message': 'Waa lagu diiwaan geliayay.',
        'status': 'success'
    }), 200)


@app.route('/profile')
def profile():
    # Assuming the user data is fetched from session or database
    user = {
        'name': 'Najka',  # Replace with actual user data
        'email': 'najka@gmail.com',
        'bio': 'A passionate software developer.',
        'phone': '+252615374914',
        'location': 'Wanlaweyn, Somalia'
    }
    return render_template('user/profile.html', user=user)

@app.route('/settings')
def settings():
    # Assuming the user data is fetched from the session or database
    user = {
        'email': 'najka@gmail.com',
        'notifications': 'enabled'  # This can be 'enabled' or 'disabled'
    }
    return render_template('user/settings.html', user=user)

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()

    # Redirect to the sign-in page
    return redirect('/signin')
