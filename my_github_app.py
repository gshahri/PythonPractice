from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form submission
        username = request.form['username']
        user_data = get_github_user(username)
        if user_data:
            # Render template with user information
            return render_template('user_info.html', user_data=user_data)
        else:
            error_message = "User not found or API request failed."
            return render_template('error.html', message=error_message)
    else:
        # Render the index.html template for GET requests
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
