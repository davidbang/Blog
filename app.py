from flask import Flask, render_template, request

import posting

app = Flask(__name__)

#homepage
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
@app.route("/blog/<title>")
def title(title=None, text=None):
    blogtitle = request.args.get("blogtitle")
    blogtext = request.args.get("blogtext")
    submit = request.args.get("submit")
    if (submit == "Submit" and blogtext != ""):
        if (blogtitle == ""):
            blogtitle = "Untitled Post"
        return render_template("title.html", title=blogtitle, text=blogtext)
    else:
        return render_template("title.html", title=blogtitle, text=blogtext)
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
