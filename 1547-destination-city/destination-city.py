class  Solution:
  def destCity(self,paths):
    outdegree = {}

    for path in paths:
        from_city = path[0]
        outdegree[from_city] = 1

    for path in paths:
        to_city = path[1]

        if to_city not in outdegree:
            return to_city