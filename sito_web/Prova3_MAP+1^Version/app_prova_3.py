from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def landing_page():

    return render_template("index.html")

@app.route("/launch-campaign")
def launch_campaign():

    return render_template("launch_campaign.html")


if __name__ == "__main__":
    app.run(debug=True)