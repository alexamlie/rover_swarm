from rover import rover
import random

class environment(object):
    def __init__(self, full_env, rover_num, x_view_dist, y_view_dist):        
        self.full_environment = full_env # list of lists of tuples
        self.x_view_dist = x_view_dist
        self.y_view_dist = y_view_dist
        self.x_max = len(full_env)
        self.y_max = len(full_env[0])
        
        # initialize rovers:
        self.rover_list = [] # start with empty list
        for i in range(0, rover_num):
            # get the starting location
            starting_loc = (random.randrange(self.x_max), random.randrange(self.y_max))
            # get the starting environment

            # only precompute the minimum because negative indices mess it up
            # but indexing past the maximum of the array is fine
            minx = max(0, (starting_loc[0] - self.x_view_dist))
            # first get only the x coordinates
            starting_env = full_env[minx:starting_loc[0] + self.x_view_dist + 1]
            # now parse out the appropriate y coordinates as well
            for xcoord in range(len(starting_env)):
                miny = max(0, (starting_loc[1] - self.y_view_dist))
                starting_env[xcoord] = starting_env[xcoord][miny:(starting_loc[1] + self.y_view_dist + 1)]
            # now we have the restricted environment                
            thisrover = rover(starting_loc, starting_env)
            # add this rover to the list
            self.rover_list.append(thisrover)
            # print thisrover.location
            # print thisrover.local_env
               
    def time_step(self):
        for rov in self.rover_list:
            newloc_set = False
            while not newloc_set:
                desired_loc = rov.move()
                # check if the move is legal
                if (desired_loc[0] >= 0 & desired_loc[0] < self.x_max) & (desired_loc[1] >= 0 & desired_loc[1] < self.y_max):
                    # compute the new environment
                    minx = max(0, (desired_loc[0] - self.x_view_dist))
                    # first get only the x coordinates
                    new_env = self.full_environment[minx:desired_loc[0] + self.x_view_dist + 1]
                    # now parse out the appropriate y coordinates as well
                    for xcoord in range(len(new_env)):
                        miny = max(0, (desired_loc[1] - self.y_view_dist))
                        new_env[xcoord] = new_env[xcoord][miny:(desired_loc[1] + self.y_view_dist + 1)]
                    rov.update_rover(desired_loc, new_env)
                    newloc_set = True # move on to the next rover

    
    def get_state(self):
        state_string = ""
        for rovnum in range(len(self.rover_list)):
            thisloc = self.rover_list[rovnum].location
            state_string += "Rover %d: (%d, %d)\t" % (rovnum, thisloc[0], thisloc[1])
        # remove the last tab
        state_string = state_string[0:-1]
        return state_string
