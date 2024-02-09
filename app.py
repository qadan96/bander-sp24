from flask import Flask, send_from_directory
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='static/', 
                          prefix='static/',
                          index_file='index.htm',
                          autorefresh=True)  

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.htm')  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
