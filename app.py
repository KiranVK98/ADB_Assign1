from flask import Flask, render_template, request
import pyodbc
import textwrap
server = 'kiran98.database.windows.net'
database = 'Assignment12'
username = 'kiran1998'
password = 'Omsrn@062466'
driver = '{ODBC Driver 18 for SQL Server}'

app = Flask(__name__)

sqlconnection = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                               ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = sqlconnection.cursor()

# connection_string = "DefaultEndpointsProtocol=https;AccountName=assigns1;AccountKey=FjfZ2UGw8oZx9cDaz2PJYqCtqMlyAXVuGt5Dq8TTcN1InDs8yUrgc8PIu48Xq8A7zku1SP0G+1hN+AStHhKtsQ==;EndpointSuffix=core.windows.net"
# img_container = "uniqcontain"


@app.route('/', methods=["POST", "GET"])
def home():
    return render_template('index.html')


@app.route('/display', methods=["POST", "GET"])
def display():
    link = "https://assigns1.blob.core.windows.net/uniqcontain/"
    ds = "SELECT * from [dbo].[people]"
    cursor.execute(ds)
    ftch = cursor.fetchall()
    print(ftch)
    return render_template('display.html', dsp=ftch, link=link)


@app.route('/fetchdata', methods=["POST", "GET"])
def search():
    link = "https://assigns1.blob.core.windows.net/uniqcontain/"
    fh_name = str(request.form.get("name"))
    names = "SELECT Name,Picture from [dbo].[people] WHERE Name='{}'".format(
        fh_name)
    cursor.execute(names)
    ftch = cursor.fetchall()
    print(ftch)
    return render_template('search_name.html', dsp=ftch, link=link)


if __name__ == '__main__':  # only run if you run this file, not if you import other main.py file
    #os.environ['PYTHONPATH'] = os.getcwd()
    app.run(debug=True)

# di


# @app.route('/updatedata', methods=["POST", "GET"])

# def upd_data():
#     name = request.form.get("Name")
# 	state = request.form.get("State")
# 	salary = request.form.get("Salary")
# 	grade = request.form.get("Grade")
#     room = request.form.get("Room")
# 	telnum = request.form.get("Telnum")
# 	keywords = request.form.get("Keywords")
