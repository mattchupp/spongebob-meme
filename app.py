import flask
import random
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# path -> / 
@app.route('/', methods=['GET'])
def home():
  
  return mock('Here is ANother string!')


# Capitalize every other letter
# ExPeCtEd OuTpUt
def mock(text): 
  newStr = []
  output = ''
  i = 0

  for c in text: 
    if (i%2) == 0: 
      newStr.append(c.capitalize())
    else: 
      newStr.append(c.lower())
    
    i = i + 1
  
  return output.join(newStr)
  

# Run 
app.run()