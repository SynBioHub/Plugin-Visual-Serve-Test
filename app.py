from flask import Flask, request, abort, jsonify
import os, flask

app = Flask(__name__)

@app.route("/status")
def status():
    return("The Server Test Plugin Flask Server is up and running")

@app.route("/evaluate", methods=["POST", "GET"])
def evaluate():
    data = request.get_json(force=True)
    rdf_type = data['type']
    
    ########## REPLACE THIS SECTION WITH OWN RUN CODE #################
    #uses rdf types
    accepted_types = {'Activity', 'Agent', 'Association', 'Attachment', 'Collection',
                      'CombinatorialDerivation', 'Component', 'ComponentDefinition',
                      'Cut', 'Experiment', 'ExperimentalData',
                      'FunctionalComponent','GenericLocation',
                      'Implementation', 'Interaction', 'Location',
                      'MapsTo', 'Measure', 'Model', 'Module', 'ModuleDefinition'
                      'Participation', 'Plan', 'Range', 'Sequence',
                      'SequenceAnnotation', 'SequenceConstraint',
                      'Usage', 'VariableComponent'}
    
    acceptable = rdf_type in accepted_types
    
    # #to ensure it shows up on all pages
    # acceptable = True
    ################## END SECTION ####################################
    
    if acceptable:
        return f'The type sent ({rdf_type}) is an accepted type', 200
    else:
        return f'The type sent ({rdf_type}) is NOT an accepted type', 415

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)
    
    top_level_url = data['top_level']
    complete_sbol = data['complete_sbol']
    instance_url = data['instanceUrl']
    size = data['size']
    rdf_type = data['type']
    shallow_sbol = data['shallow_sbol']
    
    url = complete_sbol.replace('/sbol','')
    
    cwd = os.getcwd()
    filename = os.path.join(cwd, "Test.html")
    
    try:
        hostAddr = request.headers.get('host')
        
        #this works if you can access the plugin via an exposed port on the internet.
        #Note that for synbiohub it must be https
        #<img src="http://${hostAddr}/public/success.jpg" alt="Success">
        html_file = f"""<!doctype html>
                    	<html>
                    	<head><title>sequence view</title></head>
                    	<body>
                    	<div id="reactele"></div>
                    	<img src="http://localhost:8088/public/success.jpg" alt="Success">
                    	<p>Host address: {hostAddr}</p>
                    	</body>
                    	</html>
                    	"""    
            
        return html_file
    except Exception as e:
        print(e)
        abort(400)

@app.route("/public/<file_name>")
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
        
