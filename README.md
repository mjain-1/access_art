# access_art
<h2> Motivation </h2> 
To make art more accessible to those not familiar with the art scene in NYC by helping them find exhibits similar to those that they like.

<h2> Methodology </h2>    

Given the lack of publicly accessible user feedback on exhibits, creating a collaborative filtering-based recommendation system was not possible for this iteration. This meant that I would need to rely on information about the exhibits themselves to make suggestions, also known as content-based filtering. One benefit of using this type of filtering, and often a criticism of collaborative filtering, is that it allows users to explore a wider variety beyond what their 'taste' might be.     

I scraped several art websites, such as Artbeat and Artsy, to collect venues, dates, images, and press releases or descriptions of exhibits using Scrapy and selenium. I cleaned the data using pandas and Textblob (for lemmatization) before passing the exhibit descriptions through a TF-IDF vectorizer to build the vocabulary. TF-IDF was the best choice in this case because descriptions use many similar, general words that I would want to be weighted less than those that are more specific and therefore less common (e.g. 'art', 'artist', vs. 'video', 'photographer').    

I tested several NLP models-- LSA, LDA, and NMF-- and found that NMF produced the most coherent topics (in part because, at least compared to LDA, you can use tf-idf). From the NMF results, I created a similarity matrix which I used to find the 3 most similar exhibits for any one.    

<h2> Final product </h2> 
A flask app with a landing page that allows you to flip through the images of current exhibits. If you like one, you can click on it, and it will take you to a page that shows you the venue and dates, as well as 3 similar exhibits also going on.     

<h2> Next steps </h2> 
Next steps for this would include building out the app by adding information about the exhibit, creating a map of the venues (and, ideally, allowing users to create a route of places they're interested in), and allowing users to rate (like/dislike) those that they visit. Collecting user feedback would allow this app to transition from using purely content-based filtering to incorporating collaborative filtering.     
