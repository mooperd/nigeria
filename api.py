from flask import Flask, jsonify
import csv
app = Flask(__name__)





@app.route('/')
def hello_world():
    return_list = []
    with open('nga_pop_sendist_2016.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if int(row["Population2016"]) < 1000000:
                return_list.append(row)
                # print(row["admin1Name_en"], row ['Population2016'])
    return jsonify(return_list)

@app.route('/post-code/<search_term>')
def postcode(search_term):
    return_list = []
    with open('nga_pop_sendist_2016.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row["SenDistPcode"] == search_term:
                return_list.append(row)
                # print(row["admin1Name_en"], row ['Population2016'])
    return jsonify(return_list)

if __name__ == '__main__':
    app.run(debug=True)