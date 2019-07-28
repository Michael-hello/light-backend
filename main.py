from flask import Flask
#from tinydb import TinyDB, Query
from leds import leds_fade, leds_off

#app = Flask(__name__)
#
#
#@app.route("/")
#def home():
leds_fade(5)
leds_off()

#    return "Hello, World!"
#
#
##alarmDB = TinyDB('alarmDB.json');
##weekDB = TinyDB('weekDB.json');
#
#
#
#    
#if __name__ == "__main__":
#    app.run(debug=True)