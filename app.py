from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

names = []
assigned_recipients = {}

def reset_game():
    global names, assigned_recipients
    names = []
    assigned_recipients = {}

@app.route('/')
def home():
    return render_template('index.html', names=names, assigned_recipients=assigned_recipients)

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.form.get('name').strip()
    if name and name not in names:
        names.append(name)
    return redirect(url_for('home'))

@app.route('/assign_recipient', methods=['POST'])
def assign_recipient():
    giver = request.form.get('giver').strip()
    if giver in names and giver not in assigned_recipients:
        available_recipients = [name for name in names if name != giver and name not in assigned_recipients.values()]
        if available_recipients:
            recipient = random.choice(available_recipients)
            assigned_recipients[giver] = recipient
    return redirect(url_for('home'))

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
