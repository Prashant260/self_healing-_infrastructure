from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received Alert:", data)

    # Run Ansible playbook
    subprocess.run(["ansible-playbook", "heal.yml"])

    return 'Alert received', 200
@app.route('/',methods=['get'])
def index():
    return "webhook server is running. use POST to send alerts. ", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

