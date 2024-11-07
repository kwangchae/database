from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('restaurant_menu.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    conn = get_db_connection()
    cursor = conn.cursor()
    items = cursor.execute('SELECT name FROM restaurant').fetchall()
    conn.close()
    mydoc = "<h1>All Restaurants</h1>"
    mydoc += "<ul>"
    for item in items:
        mydoc += f"<li>{item['name']}</li>"
    mydoc += "</ul>"
    return mydoc

@app.route('/restaurant/new/')
def newRestaurant():
    return "This page will be for making a new restaurant"

@app.route('/restaurant/delete/<int:restaurant_id>/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting restaurant {restaurant_id}"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)