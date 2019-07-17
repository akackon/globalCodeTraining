from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("Why am I typing this?")
    print("Chris also wanted to see what was happening")
    return 'Hello GlobalCode from Adrian'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')