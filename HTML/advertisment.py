from flask import Flask, render_template

app = Flask(__name__)

# Dati
marketing_data = [
    {'tv': 200.5, 'radio': 39.3, 'newspaper': 69.8, 'sales': 22.1},
    {'tv': 150.2, 'radio': 45.1, 'newspaper': 80.5, 'sales': 18.3},
    {'tv': 300.7, 'radio': 20.5, 'newspaper': 50.4, 'sales': 25.6}
]

@app.route('/')
def index():
    return render_template('index.html', data=marketing_data)

if __name__ == '__main__':
    app.run(debug=True)