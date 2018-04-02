import requests
from flask import Flask,request,make_response
import json

app = Flask(__name__)
    
@app.route('/',methods =['POST'])

def home():
    req = request.get_json(silent=True,force=True)
    recipe = req.get("result").get("parameters").get("recipe")
    response = requests.get("https://api.edamam.com/search?q="+ recipe+"&app_id=609ddfda&app_key=3b418fd7c775e74b7bf933b67b8b645f&from=0&to=3")
    res = response.json()
    for x in range (0,3)
        speech=res.get("hits")[x].get("recipe").get("url")
        
    resul = json.dumps({
        "speech":speech,
        "displayText":speech,
        "source":"dialogflowResponse"
            }, indent=4)

    r = make_response(resul)
    return r

if __name__ == '__main__':
    app.run(debug=True)
