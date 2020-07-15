from flask import Flask, request, abort, jsonify
import os, flask

app = Flask(__name__)

@app.route("/status")
def status():
    return("The Server Test Plugin Flask Server is up and running")

@app.route("/evaluate", methods=["POST", "GET"])
def evaluate():
    return("The type sent is an accepted type")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)
    
    url = data['complete_sbol'].replace('/sbol','')
    instance = data['instanceUrl']
    uri = data['top_level']
    
    cwd = os.getcwd()
    filename = os.path.join(cwd, "Test.html")
    
    try:
        hostAddr = request.headers.get('host')
        
        #this works if you can access the plugin via an exposed port on the internet.
        #Note that for synbiohub it must be https
        #<img src="http://${hostAddr}/success.jpg" alt="Success">
        html_file = f"""<!doctype html>
                    	<html>
                    	<head><title>sequence view</title></head>
                    	<body>
                    	<div id="reactele"></div>
                    	<img src="http://localhost:8088/success.jpg" alt="Success">
                    	<p>Host address: {hostAddr}</p>
                    	</body>
                    	</html>
                    	"""    
            
        return html_file
    except Exception as e:
        print(e)
        abort(404)

@app.route("/<file_name>")
def success(file_name):
    cwd = os.getcwd()
    path = os.path.join(cwd,'public')
    try:
        return flask.send_from_directory(path,file_name)
    except:
        with open(os.path.join(cwd,"Static_File_Not_Found.html")) as file:
            error_message = file.read()
            
        error_message = error_message.replace('REPLACE_FILENAME',file_name)
        return error_message, 404
        