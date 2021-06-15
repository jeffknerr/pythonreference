

from nbaplayer import *

p1 = NBAPlayer("Jeff Knerr", 11, "Philadelphia 76ers")
print(p1)
p1.playGame(20)    # good game!
p1.playGame(10)    # so-so...
print(p1)
print("%s is averaging %5.1f points/game" % (p1.getName(), p1.ppg()))
p1.playGame(3)     # Jeff not playing well....let's trade him
p1.trade("New York Knicks")
print(p1)
