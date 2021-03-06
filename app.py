from flask import Flask, render_template, request, redirect
import posting

app = Flask(__name__)
id=0

#homepage
@app.route("/")
def index():
    blogtitle = request.args.get("blogtitle")
    blogtext = request.args.get("blogtext")
    submit = request.args.get("submit")
    if (submit == "Submit" and blogtext != ""
        and blogtitle not in posting.get_all_blogs()):
        if (blogtitle == ""):
            blogtitle = "Untitled Post"
        global id
        posting.post_blog(id, blogtitle, blogtext)
        id = id + 1
        return redirect("/blog/"+str(id-1))
    else:
        global combine
        combine = 0
        blog =  posting.get_all_blogs()
        ids = posting.get_ids()
        blogs = []
        for a in blog:
            blogs.append([ids[combine], a] )
            combine = combine + 1
        return render_template("index.html", blogs= blogs)

@app.route("/blog/<id>")
def getblog(id):
    comment = request.args.get("comment")
    submitc = request.args.get("submitc")
    cname = request.args.get("cname")
    if (submitc == "Submit" and comment != ""):
        if (cname == ""):
            cname = "Anonymous"
        posting.post_comment (id, cname, comment);
        comment = ""
        return redirect("/blog/"+str(id))
    post = posting.get_blog(id)
    try:
        ti = post[0]
        te = post[1]
    except IndexError:
        return render_template("oops.html")
    coms = posting.get_comment(id)
    return render_template("title.html", title=ti, text=te, comments=coms)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
