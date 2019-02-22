from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rest'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/rest'

mongo = PyMongo(app)

@app.route('/servers', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.servers

    output = []

    for q in framework.find():
        output.append({'name' : q['name'], 'id' : q['id'],'language' : q['language'], 'framework' : q['framework']})

    return jsonify({'result' : output})




@app.route('/servers/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.servers
    q = framework.find_one({'name' : name})
    q1= framework.find_one({'id' : name})

    if q or q1:
        output = {'name' : q['name'], 'id' : q['id'],'language' : q['language'], 'framework' : q['framework']}
    else:
        output = 'No results found'




    return jsonify({'result' : output})





    return jsonify({'result' : output})

@app.route('/servers', methods=['PUT'])
def add_framework():
    framework1= mongo.db.servers

    name = request.json['name']
    id = request.json['id']
    language=request.json['language']
    framework=request.json['framework']

    framework_id = framework1.insert({'name' : name, 'id' : id,'language' : language, 'framework' : framework})
    new_framework = framework1.find_one({'_id' : framework_id})


    output = {'name' : new_framework['name'], 'id' : new_framework['id'],'language' : new_framework['language'], 'framework' : new_framework['framework']}

    return jsonify({'result' : output})
@app.route('/servers/<id>', methods=['DELETE'])
def delete(id):

        criteria = id
        mongo.db.servers.delete_many({"id":criteria})
        return(jsonify('Deletion successful'))



if __name__ == '__main__':
    app.run(debug=True)