import flask
from flask import jsonify, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
  return "<p>Hello!</p>"

# @app.route('/api', methods=['GET'])
# def api():
#   return jsonify(people)

# @app.route('/api/person', methods=['GET'])
# def api_id():
#   if 'id' in request.args:
#     id = int(request.args['id'])
#   else: 
#     return 'No id in request'
  
#   personResponse = []

#   for person in people: 
#     if person['id'] == id: 
#       personResponse.append(person)

#   return jsonify(personResponse)

app.run()