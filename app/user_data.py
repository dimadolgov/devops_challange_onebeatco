import requests
from flask import Flask, jsonify

user_data = Flask(__name__)

@user_data.route('/users', methods=['GET'])
def get_users():
    try:
        # Fetch user data from JSONPlaceholder API
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        users = response.json()

        # Extract name and email from each user
        user_list = [{'name': user['name'], 'email': user['email']} for user in users]

        # Publish users to the specified endpoint
        publish_users(user_list)

        return jsonify(user_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_data.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'container': '<LINK_TO_HUB>',
        'project': 'github.com/onebeatco/ecscale'
    })

def publish_users(user_list):
    # Publish users to the specified endpoint (http://127.0.0.1:5000/users)
    requests.post('http://127.0.0.1:5000/users', json=user_list)

if __name__ == '__main__':
    user_data.run(debug=True, host='0.0.0.0')
