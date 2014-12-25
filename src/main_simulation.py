"""
The main program for the rover swarm simulation
"""

import argparse, sys, os
from environment import environment

if __name__=="__main__":
    # create the argument parser
    parser = argparse.ArgumentParser(description="Simulate a swarm of Mars rovers")
    parser.add_argument("env_file", help="The file containing the information about the environment, tab separated.")
    parser.add_argument("num_rovers", type=int, help="The number of rovers you want to use")
    parser.add_argument("x_view_dist", type=int, help="How many squares in each direction the rovers can see in the X direction")
    parser.add_argument("y_view_dist", type=int, help="How many squares in each direction the rovers can see in the Y direction")
    parser.add_argument("time_steps", type=int, help="How many time steps you'd like to simulate")
    pargs = parser.parse_args()
    # parse the environment file here:
    raw_env = [] # start with an empty list
    with open(pargs.env_file, 'r') as env_file:        
        for line in env_file:
            thisline = line.strip().split("\t")
            x = int(thisline[0])
            y = int(thisline[1])
            raw_env.append([float(thisline[2]), float(thisline[3])])
    # reshape the environment list into the format we want
    # http://stackoverflow.com/questions/10124751/convert-a-flat-list-to-list-of-list-in-python
    full_env = zip(*[iter(raw_env)]*(y+1))
    
    # initialize the environment
    simul_env = environment(full_env, pargs.num_rovers, pargs.x_view_dist, pargs.y_view_dist)
    for i in range(0, pargs.time_steps):
        simul_env.time_step()
    
        curstate = simul_env.get_state()
        # print current state or write it to output file
        print curstate
    
