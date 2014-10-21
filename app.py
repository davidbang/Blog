from flask import Flask, render_template, request

app = Flask(__name__)

#homepage
@app.route("/")
def index(txt = None):
    render_template("index.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
