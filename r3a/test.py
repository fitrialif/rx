import time
import r3c
from r3s import get_dist, get_sensorpin


print "test start, initializing chasis and sensors"
r = r3c.r3c() #initialize chassis

print "@@@@@@@@@@ sensor readings start"
for x in range(0, 30):
    print "Reading #: ",x
    get_dist('fl')
    get_dist('fc')
    get_dist('fr')
    print "\n\n"

print "@@@@@@@@@@ sensor readings end"

print "@@@@@@@@@@ journey start"

r.journey('random',90)
print "@@@@@@@@@@ journey end"

'''
print "nav test 60 secs"
r.nav(-100,-100,-1)
r.nav(100,100,60)
r.stop()

print "pivot left"
r.pivot('left')
time.sleep(2)
print "pivot right"
r.pivot('right')

print "fwd"
r.nav(65,65,5)
print "backup"
r.nav(-65,-65,5)
'''

print "test over!"
