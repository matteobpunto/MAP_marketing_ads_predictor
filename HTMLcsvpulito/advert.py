from flask import Flask, render_template
import csv

app = Flask(__name__)

marketing_data = []

with open('Advertising_clear.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            marketing_data.append({
                'TV': float(row['TV'].strip()) if row['TV'].strip() else 0,
                'radio': float(row['radio'].strip()) if row['radio'].strip() else 0,
                'newspaper': float(row['newspaper'].strip()) if row['newspaper'].strip() else 0,
                'sales': float(row['sales'].strip()) if row['sales'].strip() else 0
            })
        except ValueError as e:
            print(f"Error in row: {row}, skipped. Error: {e}")

print(f"Loaded {len(marketing_data)} records.")

# conn.commit()
# conn.close()

@app.route('/')
def index():
    return render_template('index.html', data=marketing_data)

if __name__ == '__main__':
    app.run(debug=True)
