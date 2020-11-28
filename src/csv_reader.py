import csv
from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path="")

@app.route("/", methods=["GET"])
def read_csv():
    employee_list = []

    with open('data/employees.csv', 'r') as file_csv:
        content = csv.DictReader(file_csv)

        for employee in content:
            employee_list.append(employee)

    return jsonify(employee_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 5050)

