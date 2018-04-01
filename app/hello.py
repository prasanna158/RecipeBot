from flask import Flask,request
import json

app = Flask(__name__)
    
@app.route('/',methods =['POST'])

def home():
    
    #response = requests.get("https://api.edamam.com/search?q="+ rec +"&app_id=609ddfda&app_key=3b418fd7c775e74b7bf933b67b8b645f&from=0&to=3")
    ##res = response.json()

    req = request.get_json(silent=True,force=True)
    print("hello")
    print(json.dumps(req,indent =4))

    speech="testdata"
    

    res = json.dumps({
        "speech":speech,
        "displayText":speech,
        "source":"dialogflowResponse"
            }, indent=4)
    r = make_response(res)


if __name__ == '__main__':
    app.run(debug=True)
