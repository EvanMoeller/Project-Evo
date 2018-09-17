from flask import Flask, render_template

app = Flask(__name__)

#frontpage
@app.route("/")
def main():
    return render_template('index.html')

#login system
@app.route("/login")
def login():
    return render_template('login.html')

#user home page
@app.route("/home")
def home():
    return render_template('home.html')


#port setup for server initialization
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)