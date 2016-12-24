# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd


art = pd.read_csv('/Users/meghajain/Desktop/artsy_cleaned.csv', encoding='latin-1', index_col = 0)
sim_matrix = pd.read_csv('/Users/meghajain/Desktop/final_sim.csv', encoding='latin-1', index_col = 0, tupleize_cols = True)

art['title_venue'] = tuple(zip(art['title'], art['venue']))

art['title'] = art['title'].apply(lambda x: x.encode('ascii','ignore').decode('unicode_escape').replace('_', ''))

art['venue'] = art['venue'].apply(lambda x: x.encode('ascii','ignore').decode('unicode_escape').replace('_', ''))

images = [item for item in art['image']]



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

class Pref(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)  
      
db.create_all()



@app.route('/')
def hello_world():
    
    return render_template('index.html', data=images)
    

    
@app.route('/exhibit/<data_pos>')
def exhibit(data_pos):
    
    url = images[int(data_pos)]
    
    for item in art[art['image'] == url]['title_venue']:
        title_venue = item 
    
    for find_venue in art[art['image'] == url]['venue']:
        venue = find_venue 
    
    for find_title in art[art['image'] == url]['title']:
        title = find_title
    
    for item in art[art['image'] == url]['end_date']:
        end = item
    
    top_three_shows = []
    
    for index,item in enumerate(sim_matrix[str(title_venue)].sort_values(ascending=False).head(4).index):
        if index > 0:
            item = item.split('\', ')[0].replace('(', '').replace('\'', '')
            item = item.encode('ascii','ignore')
            item_final = item.decode('utf-8').replace('_', '').replace('\\x8d', '').replace('\x9d', '').replace('\x81N', '').replace('\x8f', '').replace('\\x8f', '').replace('\\x9d', '')
            top_three_shows.append(item_final)

        
    top_three_images = []
    top_three_venues = []
    
    for item in art[art['title'].isin(top_three_shows)]['image']:
        top_three_images.append(item)
        
    for item in art[art['title'].isin(top_three_shows)]['venue']:
        top_three_venues.append(item)
        
    print(top_three_images, top_three_venues)
    
    return render_template('exhibit.html', url = url, venue = venue, title = title, end = end, url1 = top_three_images[0], url2 = top_three_images[1], url3 = top_three_images[2], venue1 = top_three_venues[0], venue2 = top_three_venues[1], venue3 = top_three_venues[2])
    


app.run(debug = True)
