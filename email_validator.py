from flask import Flask
from validate_email import validate_email


app = Flask(__name__)


@app.route('/email/api/v1.0/verify/<string:email_address>', methods=['GET'])
def verify_email(email_address):
    is_valid = validate_email(email_address,verify=True)
    return str(is_valid)


if __name__ == '__main__':
    app.run(debug=True)