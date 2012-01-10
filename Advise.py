from Scrapper import Scrapper
from Cluster import Cluster
import sys,pickle

def store_data(data, filename):
  """
  Creates a file and dumps all the object's information in it.
  @param data: the data structure that we want to store in the file
  @param filename: the name of the file
  """
  file = open(filename, "w")
  pickle.dump(data, file)
  file.close()

def load_data(filename):
  """
  Returns the object stored in the file
  @param filename: the name of the file
  @return the object stored in the file
  """
  file = open(filename, "r")
  data = pickle.load(file)
  file.close()
  return data


"""
Example use of Advise.py

scrapper.query(QUERY='university', OBJECT_TYPE='page')
university_pages = scrapper.get_pages(QUERY='university', OBJECT_TYPE='page')
scrapper.dump("query_data")
store_data(university_pages, "university_pages")
clusters = Cluster.kmeans(data=university_pages, k=20)
"""
if __name__ == "__main__":
  scrapper = Scrapper()
  scrapper.load("query_data")
  university_pages = load_data("university_pages")
  clusters = Cluster.kmeans(data=university_pages)
  print clusters
