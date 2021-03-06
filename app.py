import flask
import random
from flask import request, render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# for path -> / -- load index.html from templates
@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST": 
    mocked_text = mock(request.form['text_input'])
    return render_template('index.html', mocked_text = mocked_text)
  else: 
    return render_template('index.html')


# Capitalize every other letter
# loop through each character, capitalize every other 
# by incrementing i with each loop, append to an array, 
# join then return --> ExPeCtEd OuTpUt 
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
if __name__ == '__main__':
    app.run()