import sys, random

## usage: python random_env.py <num_x> <num_y>
## randomly generates elevation and prize values
if __name__=="__main__":
    if len(sys.argv) == 3:
        xnum = int(sys.argv[1])
        ynum = int(sys.argv[2])
        for x in range(xnum):
            for y in range(ynum):
                print '%d\t%d\t%f\t%f' % (x, y, random.random(), random.random())
    else:
        print "Usage: python random_env.py <num_x> <num_y>"
       
