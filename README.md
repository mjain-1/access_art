# access_art
<h2> Motivation </h2> 
To make art more accessible to those not familiar with the art scene in NYC by helping them find exhibits similar to those that they like.

<h2> Methodology </h2>    

Tools: scrapy, selenium, pandas, textblob, scikit-learn, flask, SQLite    

Given the lack of publicly accessible user feedback on exhibits, I approached this by creating a content-based filtering system, or relying on the exhibit descriptions themselves to make suggestions. One benefit of using this type of filtering, rather than collaborative filtering, is that it allows users to explore a wider variety beyond what their 'taste' might be.     

I scraped several art websites, such as Artbeat and Artsy, to collect venues, dates, images, and press releases or descriptions of exhibits using Scrapy and selenium. I cleaned and processed the data using pandas and Textblob before passing the exhibit descriptions through a tf-idf vectorizer to build a vocabulary. Tf-idf was the best choice in this case because descriptions use many similar, general words that I would want to be weighted less than those that are more specific and therefore less common (e.g. 'art', 'artist', vs. 'video', 'photographer').    

I tested several NLP models-- LSA, LDA, and NMF-- and found that NMF produced the most coherent topics (in part because, unlike with LDA, you can use tf-idf). From the NMF results, I created a similarity matrix which I used to find the 3 most similar exhibits for any one.    

<h2> Final product </h2> 
A flask app with a landing page that allows you to flip through the images of current exhibits. Clicking on an image takes you to a page that shows the venue and dates of the image, as well as 3 similar exhibits also going on.     

<h2> Next steps </h2> 
Next steps include adding further information about the exhibit, creating a map of the venues (and, ideally, letting users create a route of places they're interested in), and allowing users to rate (like/dislike) those that they visit. Collecting user feedback would allow this app to transition from using purely content-based filtering to incorporating collaborative filtering.     
