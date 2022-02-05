from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Automatico - Jenkins CI/CD - GKE'

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)