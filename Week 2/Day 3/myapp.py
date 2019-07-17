from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello GlobalCode!!!!"

@app.route('/numberofpeople')
def people():
    return "There are 14 people in the class today"



@app.route('/numberofpeople/girls')
def girls():
    return ("There are 4 girls in the room today")

@app.route('/numberofpeople/boys')
def boys():
    return ("There are 10 boys in the room today excluding our lecturers")

@app.route('/htmlpage')
def page():
    return render_template('basepage.html')

@app.route('/htmlpage/<name>')
def myName(name):
    return render_template('basepage.html', to = name)

@app.route('/forms')
def forms():
    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')