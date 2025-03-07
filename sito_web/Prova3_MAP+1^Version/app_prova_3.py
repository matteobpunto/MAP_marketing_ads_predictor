from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def landing_page():

    return render_template("index.html")

@app.route("/launch_campaign", methods=['GET', 'POST'])
def launch_campaign():
    if request.method == 'POST':
        company = request.form.get("company")
        tv = request.form.get("tv")
        radio = request.form.get("radio")
        newspaper = request.form.get("newspaper")

        print(f"Company: {company}, TV: {tv}, Radio: {radio}, Newspaper: {newspaper}")

    return render_template("launch_campaign.html")  # ✅ Mostra sempre l'HTML, sia per GET che POST



if __name__ == "__main__":
    app.run(debug=True)