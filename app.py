from flask import Flask, render_template, request

app = Flask(__name__)

#homepage
@app.route("/", methods=["GET","POST"])
def index(txt = None):
    if request.method == "GET":
        return render_template("home.html", txt = None)
    else:
        txtbox = request.form["input"]
        button = request.form["enter"]
        if button == None:
            return render_template("index.html", txt = None)
        else:
            return render_template("home.html", txt = txtbox)
        
#main
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2014)
