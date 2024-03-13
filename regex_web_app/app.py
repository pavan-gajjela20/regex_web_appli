# app.py
from flask import Flask, render_template, request
import re  # Add this import for the 're' module
from email_validator import validate_email

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    # Perform regex matching
    matches = re.findall(regex_pattern, test_string)

    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email_route():
    email = request.form['email']
    is_valid = validate_email(email)

    return render_template('index.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
