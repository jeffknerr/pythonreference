class NBAPlayer(object):
  """class for single NBA player object"""

  def __init__(self, name, number, team):
    """constructor for player object, given name, etc"""
    # any self.whatever variable is DATA for this object,
    # and can be used in any methods in this class
    self.name = name
    self.number = int(number)    # jersey number
    self.team = team
    self.gp  = 0                 # games played
    self.pts = 0                 # points scored

  def __str__(self):
    """pretty-print info about this object"""
    s = "%s #%d -- Team: %s" % (self.name, self.number, self.team)
    s += "\nGP: %d,  PTS: %d" % (self.gp, self.pts)
    return s

  def playGame(self, points):
    """example of adding data to player object"""
    self.gp += 1
    self.pts += points

  def ppg(self):
    """calculate average points per game"""
    if self.gp == 0:
      return 0
    else:
      ave = self.pts/float(self.gp)
      return ave

  def trade(self,newteam):
    """change team to newteam"""
    self.team = newteam

  def getName(self):
    """getter for player's name"""
    return self.name

  def getTeam(self):
    """getter for player's team"""
    return self.team
