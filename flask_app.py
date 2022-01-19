from flask import Flask, jsonify, request
import random

app = Flask(__name__)
tasks = [
    {
        'id' : 1,
        'Name' : 'Aman',
        'contact' : random.randint(9000000000, 9999999999),
        'done' : False
    },

    {
        'id' : 2,
        'Name' : 'Ram',
        'contact' : random.randint(9000000000, 9999999999),
        'done' : False
    }
]

@app.route('/add-data', methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message':'Please Provide the data',
        },400)
    task = {
        'id' : tasks[-1]['id']+1,
        'Name' : request.json['Name'],
        'contact' : request.json.get('contact', ''),
        'done' : False
    }
    tasks.append(task)
    return jsonify({
        'status' : 'done',
        'message' : 'Task is done',
    })

@app.route('/get_task')
def get_task():
    return jsonify({
        'data' : tasks,
    })


if(__name__ == '__main__'):
    app.run(debug=True)