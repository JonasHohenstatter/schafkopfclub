from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/events")
def events():
	return render_template("events.html")

@app.route("/news")
def news():
	return render_template("news.html")

@app.route("/ranking")
def ranking():
	return render_template("ranking.html")

@app.route("/participate")
def participate():
	return render_template("participate.html")



if __name__ == "__main__":
	app.run(debug=True)
