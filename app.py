from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Connector System'

if __name__ == '__main__':
    app.run()