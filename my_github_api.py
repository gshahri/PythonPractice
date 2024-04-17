from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/github/user/<username>', methods=['GET'])
def get_github_user_route(username):
    user_data = get_github_user(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
