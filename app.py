import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'       #go to this file
    csv_file = open(csv_path, 'r')                  #open it (i think r means read)
    csv_obj = csv.DictReader(csv_file)              #turn csv into a list of dictionaries. The one with keys and values.
    csv_list = list(csv_obj)                        #convert to a permanent list
    return csv_list                                 #oktq

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()                         #just run what I told you to up there
    return render_template(template, object_list=object_list)   #Lol. Making things complicated.

if __name__ == '__main__':
    #Fire up the Flask test server and run Python script as a program.
    app.run(debug=True, use_reloader=True)      #app.run = Dear Flask, please boot my website up
    
