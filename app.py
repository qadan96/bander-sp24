from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='static/', 
                          prefix='static/', 
                          index_file='index.htm', 
                          autorefresh=True)
@app.route('/', methods=['GET'])

