from flask import Flask, render_template, request

import posting

app = Flask(__name__)
id=0

#homepage
@app.route("/")
def index():
    blogtitle = request.args.get("blogtitle")
    blogtext = request.args.get("blogtext")
    submit = request.args.get("submit")
    if (submit == "Submit" and blogtext != ""):
        if (blogtitle == ""):
            blogtitle = "Untitled Post"
        #submit sqlite
        #getblog id=id of post
        return render_template("title.html", title=blogtitle, text=blogtext, comments = "wE NEED COMMENTS")
    else:
        return render_template("index.html")

@app.route("/blog/<id>")
def getblog(id=None):
    post = posting.get_blog(id)
    return render_template("title.html", text=post, comments="WE NEED OMMENTS HERE")
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
