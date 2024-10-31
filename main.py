from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def main():
    return render_template("index.html")

@app.route("/discography/")
def discography():
    return render_template("discography.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()