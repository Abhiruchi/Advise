Advise v1.0
===========

Purpose
-------

Advise allows you to display clusters of facebook pages based on their 'likes' and 
'talking_about_count'. The facebook pages are grouped together using k-means and the 
Euclidian distance.


Requirements
------------

1. Python2.7: http://www.python.org/getit/releases/2.7/
1. Unless you fork the repository on GitHub you will need Highcharts: http://www.highcharts.com/

Running Advise
--------------

Once you fork the repo, here is a way of running Advise:

```python
scrapper = Scrapper()
scrapper.query(QUERY='university', OBJECT_TYPE='page')
university_pages = scrapper.get_pages(QUERY='university', OBJECT_TYPE='page')
scrapper.dump("query_data")
store_data(university_pages, "university_pages")
clusters = Cluster.kmeans(data=university_pages)
visualizer = Visualizer(data=university_pages, clusters=clusters)
visualizer.visualize()
```

If your query is large gathering all this data from facebook might take a while.
This is why we are storing the data using dump()and store_data()
, just in case we might want to run this program multiple times or you might want to reuse the data.

Here is another way of running Advise in case you already have the data stored in a bunch of files:

```python
scrapper = Scrapper()
scrapper.load("query_data")
load_data(university_pages, "university_pages")
clusters = Cluster.kmeans(data=university_pages)
visualizer = Visualizer(data=university_pages, clusters=clusters)
visualizer.visualize()
```

Example Output
--------------

1. see: http://www.efekarakus.com/blog/advise.html
