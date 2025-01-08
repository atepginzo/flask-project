from flask import Flask, render_template, request
import os
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/confirmation', methods=['POST'])
def confirmation():
    # Data dari form bisa diambil menggunakan request.form
    return render_template('confirmation.html')

# Entry point
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Default ke port 5000 jika PORT kosong
    app.run(debug=False, host='0.0.0.0', port=port)
