# sending emails though smtp server through an html form with the fields email, subject, and message and the send button

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# configure mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'clintondeveloper6@gmail.com'
app.config['MAIL_PASSWORD'] = 'ahgcmnoykytzpqlm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# initialize mail server
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Perform email validation
        if not email:
         return 'Email address is required'
        # You can perform additional validation if needed

    # Send email
    msg = Message(subject=subject, recipients=[email], body=message)
    try:
        mail.send(msg)
        return 'Email sent successfully'
    except Exception as e:
        return str(e)

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)

