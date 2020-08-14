# Simple Python Flask App

This image sets up a simple python flask app and exposes it on port 5000. 

To use your own app you can setup a volume to update the app files.


## Credit where credit is due

This is a forked project from jcdemo/flaskapp. Thank him for unknowingly providing a template for this project.


## Simple usage

docker run \
  -v flask_app:/srv \
  dth202/flaskapp


## Advanced Usage

docker run \
  --name myapp \
  -d \
  -v myapp_app:/srv \
  --restart always \
  dth202/flaskapp




