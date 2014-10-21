from flask import Flask, render_template, request

app = Flask(__name__)

#homepage
@app.route("/")
def index(txt = None):
    return render_template("index.html")

@app.route("/blog/<title>")
def title(title=None):
    blogtitle = request.args.get(blogtitle)
    blogtext = request.args.get(blogtext)
    submit = request.args.get(submit)
    if (submit == "Submit" and blogtext != ""):
        if (blogtitle == ""):
            blogtitle = "Untitled Post"
        return render_template("title.html", title = title)
    else:
        return render_template("title.html", title=title)
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
