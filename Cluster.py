import math, random

class Cluster:
  """
  Cluster.py
  @author Efe Karakus
  """

  @staticmethod
  def _find_k(data):
    """@return the optimal number of clusters""" 
    n = len(data)
    return int(math.sqrt(n/2))

  @staticmethod
  def _find_means(data, clusters):
    """@return List of pairs (likes_mean,talking_mean) for every cluster"""
    means = []
    for x in range(0, len(clusters)):
      likes_mean = 0
      talking_mean = 0
      for y in range(0, len(clusters[x])):
        id = clusters[x][y]
        likes = data[id]['likes']
        talking = data[id]['talking_about_count']
        likes_mean = likes_mean + likes
        talking_mean = talking_mean + talking
      # endfor y
      likes_mean = likes_mean/len(clusters[x])
      talking_mean = talking_mean/len(clusters[x])
      means.append( (likes_mean, talking_mean) )
    # endfor x
    return means

  @staticmethod
  def kmeans(data=None, k=None):
    """
    Applies the L2 distance for every facebook page and the mean of each cluster
    @param data: dictionary containing the facebook pages that we want to group
    @param k: the number of clusters
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    if data is None:
      return None
    if k is None:
      k = Cluster._find_k(data)

    # Initialize the structures
    old_clusters = []
    clusters = []
    sample = random.sample(data.keys(), k)
    for id in sample:
      clusters.append([id])
    # endfor id
    means = Cluster._find_means(data, clusters)

    while not Cluster._is_converged(old_clusters, clusters):
      old_clusters = clusters
      clusters = [[] for i in range(0,k)]

      for id in data:
        likes = data[id]['likes']
        talking = data[id]['talking_about_count']
        cluster_id = 0
        min_distance = float('inf')
        for index in range(0,k):
           mean = means[index]
           distance = Cluster.EuclidianDistance( (likes,talking), mean)
           if distance < min_distance:
             min_distance = distance
             cluster_id = index
            # endif distance
        # endfor mean
        clusters[cluster_id].append(id)
      # endfor id
      means = Cluster._find_means(data, clusters)
    # endwhile is_converged
    return clusters


  @staticmethod
  def EuclidianDistance(page0, page1):
    """@return The euclidian distance between two facebook pages based on their likes and talking about counts"""
    likes0 = page0[0]
    talking0 = page0[1]
    likes1 = page1[0]
    talking1 = page1[1]

    distance = ( (likes0-likes1)*(likes0-likes1) + (talking0-talking1)*(talking0-talking1) )
    return distance


  @staticmethod
  def _is_converged(old_clusters, new_clusters):
    """@return True if the two lists contain the same IDs in them, False otherwise"""
    if len(old_clusters) != len(new_clusters):
      return False

    for x in range(0, len(new_clusters)):
      if len(old_clusters[x]) != len(new_clusters[x]):
        return False
      for y in range(0, len(new_clusters[x])):
        if old_clusters[x][y] != new_clusters[x][y]:
          return False
      # endfor y
    # endfor x
    return True

  @staticmethod
  def dbscan(data=None):
    """
    Applies the DBSCAN algorithm
    @param data: dictionary containing the facebook pages that we want to group
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    if data is None:
      return None
    clusters = []
    return clusters

  @staticmethod
  def optics(data=None):
    """
    Applies the OPTICS algorithm
    @param data: dictionary containing the facebook pages that we want to group
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    if data is None:
      return None
    clusters = []
    return clusters
