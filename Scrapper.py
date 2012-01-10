import urllib, simplejson
import sys, pickle

class Scrapper(object):
  """
  Scrapper.py
  @author Efe Karakus
  """

  URL_CORE = "https://graph.facebook.com/"
  URL_QUERY = "search?q="
  URL_TYPE = "&type="

  def __init__(self):
    """
    Constructs an empty Scrapper with no queries.
    """
    self._QUERY = None
    self._OBJECT_TYPE = None
    self._content = []
    self._results = {}
    self._results['post'] = {}
    self._results['user'] = {}
    self._results['page'] = {}
    self._results['event'] = {}
    self._results['group'] = {}
    self._results['place'] = {}
    self._results['checkin'] = {}

  def query(self, QUERY, OBJECT_TYPE, **args):
    """
    Issues the query to Facebook.  
    @param QUERY: A key word that we want to look for on Facebook
    @param OBJECT_TYPE: A string describing type of the Facebook page
    """
    self._QUERY = QUERY
    self._OBJECT_TYPE = OBJECT_TYPE
    self._content = []

    URL_QUERY = self.URL_QUERY + QUERY
    URL_TYPE = self.URL_TYPE + OBJECT_TYPE
    URL = self.URL_CORE + URL_QUERY + URL_TYPE

    self._find_data(URL, self._content)
    self._results[OBJECT_TYPE][QUERY] = self._content


  def _find_data(self, URL, content):
    """
    Crawls recursively and gathers all the 'data' fields for the given query.
    @param URL: the url that we want to get data from
    @return A string of .json format that contains all the data for the query
    """
    json = simplejson.load(urllib.urlopen(URL))

    if not json['paging'] or not json['data'] or not json['paging']['next']:
      return []
    else:
      URL = json['paging']['next']
      print "processing %s"%(URL)
      content.append(json['data'])
      self._find_data(URL, content)


  def get_pages(self, QUERY, OBJECT_TYPE, **args):
    """
    Creates a dictionary of facebook pages containing their informations
    @param QUERY: A key word that we want to look for on Facebook
    @param OBJECT_TYPE: A string describing type of the Facebook page
    @return A dictionary of facebook pages containing their informations
    """
    count = 0
    if not self._results[OBJECT_TYPE] or not self._results[OBJECT_TYPE][QUERY]:
      return None
    else:
      pages = {}
      for data in self._results[OBJECT_TYPE][QUERY]:
        for item in data:
          id = item['id']
          URL = self.URL_CORE + str(id)
          print "processing %s, url: %s"%(item['name'], URL)
          print "count: %d"%count
          count = count + 1
          data = simplejson.load(urllib.urlopen(URL))
          name = None
          picture = None
          link = None
          likes = None
          category = None
          website = None
          username = None
          founded = None
          location = None
          checkins = None
          talking_about_count = None

          if data.has_key('name'):
            name = data['name']
          if data.has_key('picture'):
            picture = data['picture']
          if data.has_key('link'):
            link = data['link']
          if data.has_key('likes'):
            likes = data['likes']
          if data.has_key('category'):
            category = data['category']
          if data.has_key('website'):
            website = data['website']
          if data.has_key('username'):
            username = data['username']
          if data.has_key('founded'):
            founded = data['founded']
          if data.has_key('location'):
            location = data['location']
          if data.has_key('checkins'):
            checkins = data['checkins']
          if data.has_key('talking_about_count'):
            talking_about_count = data['talking_about_count']

          pages[id] = {'id' : id, 'name' : name, 'picture' : picture, 'link' : link, 'likes' : likes, 
                       'category' : category, 'website' : website, 'username' : username, 'founded' : founded,
                       'location' : location, 'checkins' : checkins, 'talking_about_count' : talking_about_count}
        # endfor item
      # endfor data
      return pages

  def dump(self, filename):
    """
    Dumps the current Scrapper object into a file.
    @param filename: name of the file to write the object to
    """
    file = open(filename, "w")
    pickle.dump(self, file)
    file.close()

  def load(self, filename):
    """
    Loads a scrapper object from a file.
    @param filename: name of the file to read the object from
    """
    file = open(filename, "r")
    scrap = pickle.load(file)
    self._QUERY = scrap.get_query()
    self._OBJECT_TYPE = scrap.get_type()
    self._content = scrap.get_content()
    self._results = scrap.get_results()
    file.close()

  def get_query(self):
    """@return A string describing the query for Facebook"""
    return self._QUERY

  def get_type(self):
    """@return A string describing the type of the Facebook page"""
    return self._OBJECT_TYPE

  def get_content(self):
    """@return The json data for the query"""
    return self._content

  def get_results(self):
    """@return A dictionary containing all the search"""
    return self._results
