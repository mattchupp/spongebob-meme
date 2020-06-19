import flask
import random
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
  
  def mock(text): 
    newStr = []
    output = ''

    for c in text: 
      num = randomNum()
      if num == 1: 
        newStr.append(c.capitalize())
      else: 
        newStr.append(c)
    
    return output.join(newStr)

  def randomNum(): 
    number = random.randint(0,1)
    return number
  
  return mock('Hello world!')


app.run()