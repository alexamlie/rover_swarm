import random

class rover(object):
    def __init__(self, starting_loc, env_info):
        # initialize the class variables
        self.location = starting_loc # tuple, (x, y)
        self.local_env = env_info # list of lists of tuples
        self.history = [] # remember where it's been
        self.fuel = -1 # for now

    # print them as locations
    def __str__(self):
        return str(self.location)

    # the movement function. returns the location in (x, y) tuple the rover wants
    # to move to
    def move(self):
        # for now, just randomly go in a direction
        return (random.randrange(self.location[0]-1, self.location[0]+2), random.randrange(self.location[1]-1, self.location[1]+2))

    def update_rover(self, new_loc, env_info):
        self.history.append(self.location)
        self.location = new_loc # update the location
        self.local_env = env_info # update the local environment
        self.fuel = self.fuel
        
