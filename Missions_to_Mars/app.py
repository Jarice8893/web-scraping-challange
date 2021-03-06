from flask import Flask
from flask.templating import redirect
import pymongo
import scrape_mars

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars
mongo = pymongo(app)

app = Flask(__name__)

@app.route('/')
def home():
	mars = collection.find_one()
	return ('index.html', mars=mars)

@app.route('/scrape')
def scrape():
	scrape_mars.scrape()
	return redirect('/', code = 302)

 


if __name__ == "__main__":
    app.run(debug=True)