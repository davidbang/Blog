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
        global id
        posting.post_blog(id, blogtitle, blogtext)
        id = id + 1
        return getblog(id-1)
    else:
        return render_template("index.html")

@app.route("/blog/<id>")
def getblog(id):
    post = posting.get_blog(id)
    ti = post[0]
    te = post[1]
    coms = posting.get_comment(id)
    return render_template("title.html", title=ti, text=te, comments=coms)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
