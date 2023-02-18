'''
Date: 2023-01-28 18:39:17
LastEditors: Bigorrila
LastEditTime: 2023-01-28 20:18:59
FilePath: \PythonProjects\doggo_roulette.py
'''
from flask import Flask
from flask_mail import Mail, Message
import config
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.exmail.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="2609260594@qq.com",
    MAIL_PASSWORD="1234567890000000",
)
mail = Mail(app)


@app.route("/")
def index():
    msg = Message("Hello",sender="2609260594@qq.com",body="testing",recipients=["penilag831@breazeim.com"])
    mail.send(msg)
    return 'heiheihei'

if __name__ == "__main__":
    app.run(debug=True)