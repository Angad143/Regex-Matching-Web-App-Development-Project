from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Regex Results Page
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error:
        matches = ['Invalid regular expression!']

    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

# Email Validation Page
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(regex, email):
        result = "Valid Email!"
    else:
        result = "Invalid Email!"
    
    return render_template('email_validate.html', email=email, result=result)

if __name__ == '__main__':
    app.run(debug=True)
