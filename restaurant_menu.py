from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    db = sqlite3.connect('./restaurant_menu.db')
    cursor = db.cursor()
    items = cursor.execute('SELECT id, name FROM restaurant').fetchall()
    db.close()
    return render_template('restaurant.html', restaurants = items)

@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        db = sqlite3.connect('./restaurant_menu.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO restaurant (name) VALUES (?)', (request.form['name'],))
        db.commit()
        db.close()
        return redirect('/restaurants/')
    return render_template('restaurant_new.html')

@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return f"This page is the menu for restaurant {restaurant_id}"

@app.route('/restaurant/delete/<int:restaurant_id>/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting restaurant {restaurant_id}"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)