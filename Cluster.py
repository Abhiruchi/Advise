import math

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
  def kmeans(data=None, k=None):
    """
    Applies the L2 distance for every facebook page and the mean of each cluster
    @param data: dictionary containing the facebook pages that we want to group
    @param k: the number of clusters
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    clusters = [[]]
    if data is None:
      return clusters
    if k is None:
      k = Cluster._find_k(data)

    return clusters

  @staticmethod
  def dbscan(data=None):
    """
    Applies the DBSCAN algorithm
    @param data: dictionary containing the facebook pages that we want to group
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    clusters = [[]]
    return clusters

  @staticmethod
  def optics(data=None):
    """
    Applies the OPTICS algorithm
    @param data: dictionary containing the facebook pages that we want to group
    @return A matrix of clusters where each row represents a grouping of facebook IDs
    """
    clusters = [[]]
    return clusters
