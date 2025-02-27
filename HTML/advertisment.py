from flask import Flask, render_template
import csv

app = Flask(__name__)

# Данные для отображения в таблице

with open('Advertising_modified.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    marketing_data = []  # Lista per contenere i dati puliti

    for row in reader:
        try:
            # Convertire le colonne in float e pulire i dati
            row['TV'] = float(row['TV']) if row['TV'].strip() else None
            row['radio'] = float(row['radio']) if row['radio'].strip() else None
            row['newspaper'] = float(row['newspaper']) if row['newspaper'].strip() else None
            row['sales'] = float(row['sales']) if row['sales'].strip() else None

            marketing_data.append(row)  # Aggiungere il dizionario pulito alla lista
            #cursor.execute(f"""INSERT INTO `marketing_adv`(`tv`, `radio`, `newspaper`, `sales`) VALUES
                #('{row['TV']}','{row['radio']}','{row['newspaper']}','{row['sales']}')""")

        except ValueError as e:
            print(f"Riga ignorata a causa di errore di conversione: {row}. Errore: {e}")
    print("Dati inseriti con successo")

#conn.commit()
#conn.close()


@app.route('/')
def index():
    return render_template('index.html', data=marketing_data)

if __name__ == '__main__':
    app.run(debug=True)