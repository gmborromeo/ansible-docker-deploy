from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1> Deployed with Ansible!</h1>
    <p> This app was automatically deployed using Ansible + Docker </p>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)