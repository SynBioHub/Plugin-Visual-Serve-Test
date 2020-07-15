# Plugin-Visualisation-Test
A small test plugin to test the serving of files. Could be the basis for python based serving visualisation plugins.

# Install
## Using docker
Run `docker run --publish 8088:5000 --detach --name python-test-plug synbiohub/plugin-visualisation-test:snapshot`
Check it is up using localhost:8088.

## Using Python
Run `pip install -r requirements.txt` to install the requirements. Then run `FLASK_APP=app python -m flask run`. A flask module will run at localhost:5000/.
