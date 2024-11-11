import sqlite3

from flask import Flask, render_template, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/table')
def table():
    states = [
        {'id': 1, 'name': 'Alabama'},
        {'id': 2, 'name': 'Alaska'},
        {'id': 3, 'name': 'Arizona'},
        {'id': 4, 'name': 'Arkansas'},
        {'id': 5, 'name': 'California'},
        {'id': 6, 'name': 'Colorado'},
        {'id': 7, 'name': 'Connecticut'},
        {'id': 8, 'name': 'DC'},
        {'id': 9, 'name': 'Delaware'},
        {'id': 10, 'name': 'Florida'},
        {'id': 11, 'name': 'Georgia'},
        {'id': 12, 'name': 'Hawaii'},
        {'id': 13, 'name': 'Idaho'},
        {'id': 14, 'name': 'Illinois'},
        {'id': 15, 'name': 'Indiana'},
        {'id': 16, 'name': 'Iowa'},
        {'id': 17, 'name': 'Kansas'},
        {'id': 18, 'name': 'Kentucky'},
        {'id': 19, 'name': 'Louisiana'},
        {'id': 20, 'name': 'Maine'},
        {'id': 21, 'name': 'Maryland'},
        {'id': 22, 'name': 'Massachusetts'},
        {'id': 23, 'name': 'Michigan'},
        {'id': 24, 'name': 'Minnesota'},
        {'id': 25, 'name': 'Mississippi'},
        {'id': 26, 'name': 'Missouri'},
        {'id': 27, 'name': 'Montana'},
        {'id': 28, 'name': 'Nebraska'},
        {'id': 29, 'name': 'Nevada'},
        {'id': 30, 'name': 'New Hampshire'},
        {'id': 31, 'name': 'New Jersey'},
        {'id': 32, 'name': 'New Mexico'},
        {'id': 33, 'name': 'New York'},
        {'id': 34, 'name': 'North Carolina'},
        {'id': 35, 'name': 'North Dakota'},
        {'id': 36, 'name': 'Ohio'},
        {'id': 37, 'name': 'Oklahoma'},
        {'id': 38, 'name': 'Oregon'},
        {'id': 39, 'name': 'Pennsylvania'},
        {'id': 40, 'name': 'Rhode Island'},
        {'id': 41, 'name': 'South Carolina'},
        {'id': 42, 'name': 'South Dakota'},
        {'id': 43, 'name': 'Tennessee'},
        {'id': 44, 'name': 'Texas'},
        {'id': 45, 'name': 'Utah'},
        {'id': 46, 'name': 'Vermont'},
        {'id': 47, 'name': 'Virginia'},
        {'id': 48, 'name': 'Washington'},
        {'id': 49, 'name': 'West Virginia'},
        {'id': 50, 'name': 'Wisconsin'},
        {'id': 51, 'name': 'Wyoming'},
        # Add more states as needed
     ]
    return render_template('table.html', states=states)


@app.route('/breaches/<int:state_id>')
def get_breaches(state_id):
    conn = get_db_connection()
    breaches = conn.execute('SELECT * FROM breaches WHERE state_id = ?', (state_id,)).fetchall()
    conn.close()
    return jsonify([dict(breach) for breach in breaches])  # Return breaches as JSON


@app.route('/breach-details/<int:breach_id>')
def breach_details(breach_id):
    conn = get_db_connection()
    breach = conn.execute('SELECT * FROM breach_details WHERE breach_id = ?', (breach_id,)).fetchone()
    conn.close()

    if breach:
        return jsonify(dict(breach))
    else:
        return jsonify({"error": "Breach not found"}), 404


@app.route('/alabama')
def alabama():
    return render_template('Alabama.html')


@app.route('/Alaska')
def alaska():
    return render_template('Alaska.html')


@app.route('/Arizona')
def arizona():
    return render_template('Arizona.html')


@app.route('/Arkansas')
def arkansas():
    return render_template('Arkansas.html')


@app.route('/California')
def california():
    return render_template('California.html')


@app.route('/Colorado')
def colorado():
    return render_template('Colorado.html')


@app.route('/Connecticut')
def connecticut():
    return render_template('Connecticut.html')


@app.route('/DC')
def dc():
    return render_template('DC.html')


@app.route('/Delaware')
def delaware():
    return render_template('Delaware.html')


@app.route('/Florida')
def florida():
    return render_template('Florida.html')


@app.route('/Georgia')
def georgia():
    return render_template('Georgia.html')


@app.route('/Hawaii')
def hawaii():
    return render_template('Hawaii.html')


@app.route('/Idaho')
def idaho():
    return render_template('Idaho.html')


@app.route('/Illinois')
def illinois():
    return render_template('Illinois.html')


@app.route('/Indiana')
def indiana():
    return render_template('Indiana.html')


@app.route('/Iowa')
def iowa():
    return render_template('Iowa.html')


@app.route('/Kansas')
def kansas():
    return render_template('Kansas.html')


@app.route('/Kentucky')
def kentucky():
    return render_template('Kentucky.html')


@app.route('/Louisiana')
def louisiana():
    return render_template('Louisiana.html')


@app.route('/Maine')
def maine():
    return render_template('Maine.html')


@app.route('/Maryland')
def maryland():
    return render_template('Maryland.html')


@app.route('/Massachusetts')
def massachusetts():
    return render_template('Massachusetts.html')


@app.route('/Michigan')
def michigan():
    return render_template('Michigan.html')


@app.route('/Minnesota')
def minnesota():
    return render_template('Minnesota.html')


@app.route('/Mississippi')
def mississippi():
    return render_template('Mississippi.html')


@app.route('/Missouri')
def missouri():
    return render_template('Missouri.html')


@app.route('/Montana')
def montana():
    return render_template('Montana.html')


@app.route('/Nebraska')
def nebraska():
    return render_template('Nebraska.html')


@app.route('/Nevada')
def nevada():
    return render_template('Nevada.html')


@app.route('/NewHampshire')
def newhampshire():
    return render_template('NewHampshire.html')


@app.route('/NewJersey')
def newjersey():
    return render_template('NewJersey.html')


@app.route('/NewMexico')
def newmexico():
    return render_template('NewMexico.html')


@app.route('/NewYork')
def newyork():
    return render_template('NewYork.html')


@app.route('/NorthCarolina')
def northcarolina():
    return render_template('NorthCarolina.html')


@app.route('/NorthDakota')
def northdakota():
    return render_template('NorthDakota.html')


@app.route('/Ohio')
def ohio():
    return render_template('Ohio.html')


@app.route('/Oklahoma')
def oklahoma():
    return render_template('Oklahoma.html')


@app.route('/Oregon')
def oregon():
    return render_template('Oregon.html')


@app.route('/Pennsylvania')
def pennsylvania():
    return render_template('Pennsylvania.html')


@app.route('/RhodeIsland')
def rhodeisland():
    return render_template('RhodeIsland.html')


@app.route('/SouthCarolina')
def southcarolina():
    return render_template('SouthCarolina.html')


@app.route('/SouthDakota')
def southdakota():
    return render_template('SouthDakota.html')


@app.route('/Tennessee')
def tennessee():
    return render_template('Tennessee.html')


@app.route('/Texas')
def texas():
    return render_template('Texas.html')


@app.route('/Utah')
def utah():
    return render_template('Utah.html')


@app.route('/Vermont')
def vermont():
    return render_template('Vermont.html')


@app.route('/Virginia')
def virginia():
    return render_template('Virginia.html')


@app.route('/Washington')
def washington():
    return render_template('Washington.html')


@app.route('/WestVirginia')
def westvirginia():
    return render_template('WestVirginia.html')


@app.route('/Wisconsin')
def wisconsin():
    return render_template('Wisconsin.html')


@app.route('/Wyoming')
def wyoming():
    return render_template('Wyoming.html')


if __name__ == '__main__':
    app.run(debug=True)
