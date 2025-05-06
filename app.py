from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
        print(name)
        return render_template('horseshit.html', name = name)
    return render_template("index.html")

@app.route('/dharshini')
def greet():
    name = request.args.get('name')
    return render_template('horseshit.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)