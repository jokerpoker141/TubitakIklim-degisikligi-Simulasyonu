import random as r
import math as m
import numpy as np

class generator:
    def __init__(self, size, seed, max_value, min_value, water_probability, temprature):
        self.size_ = size
        self.seed_ = r.seed(seed)
        self.max_value_ = max_value
        self.min_value_ = min_value
        self.water_probability_ = water_probability
        self.land_probability_ = 1 - water_probability
        self.map_ = np.zeros((size, size) ,dtype=int)
        # mage a vareable to store the median value of the map
        self.median_ = 0
        self.temprature_ = temprature
    
    def generate_map(self):
        # generate the map
        for i in range(self.size_):
            for j in range(self.size_):
                # assing a random number depenfing on the max and minimum values at __init__
                self.map_[i][j] = r.randint(self.min_value_, self.max_value_)
                if self.map_[i][j] < self.median_:
                    self.map_[i][j] = 0
        # calculate the median value of the map
        self.median_ = np.median(self.map_)
        # normalize the map
        return self.map_
    
    def smooth_map(self):
           # smooth the map by averaging the values of the map and the values around it
        for i in range(self.size_):
            for j in range(self.size_):
                if i == 0 or i == self.size_ - 1 or j == 0 or j == self.size_ - 1:
                    continue
                else:
                    if (self.map_[i-1][j] + self.map_[i+1][j] + self.map_[i][j-1] + self.map_[i][j+1]) == 0:
                        self.map_[i][j] = 0
                    elif (self.map_[i-1][j] + self.map_[i+1][j] + self.map_[i][j-1] + self.map_[i][j+1]) != 0:
                        self.map_[i][j] = (self.map_[i-1][j] + self.map_[i+1][j] + self.map_[i][j-1] + self.map_[i][j+1]) / 4
        # calculate the median value of the map
        self.median_ = np.median(self.map_)
        # normalize the map
        normalized_map = self.map_
        return self.map_ , self.median_ , normalized_map
    

    def categorize_map(self):
        categorized_map_int = np.zeros((self.size_, self.size_) ,dtype=int)
        for i in range(self.size_):
            for j in range(self.size_):
                try:
                    if self.map_[i][j] > (self.median_*4)/3:
                        categorized_map_int[i][j] = 1 # 1 = mountain
                    # if the value is bigger than the median value and has a mountain in a 1 cell radius around it then its a hill
                    elif self.map_[i][j] > self.median_ and (self.map_[i-1][j] == 1 or self.map_[i+1][j] == 1 or self.map_[i][j-1] == 1 or self.map_[i][j+1] == 1 or self.map_[i-1][j-1] == 1 or self.map_[i+1][j+1] == 1 or self.map_[i-1][j+1] == 1 or self.map_[i+1][j-1] == 1):
                        categorized_map_int[i][j] = 2 # 2 = hill
                    # if the value is bigger than the median value and is not a hill then its a plato
                    elif self.map_[i][j] > self.median_ and (self.map_[i-1][j] != 2 or self.map_[i+1][j] != 2 or self.map_[i][j-1] != 2 or self.map_[i][j+1] != 2 or self.map_[i-1][j-1] != 2 or self.map_[i+1][j+1] != 2 or self.map_[i-1][j+1] != 2 or self.map_[i+1][j-1] != 2):
                        categorized_map_int[i][j] = 3 # 3 = plain
                    # if the value is zero or below zero then its water
                    elif self.map_[i][j] <= 0:
                        categorized_map_int[i][j] = 4 # 4 = water
                    # if the value is below the median value then its land and has no water in a 1 cell radius around it
                    elif self.map_[i][j] <= self.median_ and (self.map_[i-1][j] != 4 or self.map_[i+1][j] != 4 or self.map_[i][j-1] != 4 or self.map_[i][j+1] != 4 or self.map_[i-1][j-1] != 4 or self.map_[i+1][j+1] != 4 or self.map_[i-1][j+1] != 4 or self.map_[i+1][j-1] != 4):
                        categorized_map_int[i][j] = 5 # 5 = plains
                    else:
                        categorized_map_int[i][j] = 0 # 0 = nothing
                except IndexError:
                    pass
                
            # explatin the categoryized map
        self.categorized_map_int = categorized_map_int
        self.categorized_map = np.zeros((self.size_, self.size_), dtype="object")
        for i in range(self.size_):
            for j in range(self.size_):
                if categorized_map_int[i][j] == 1:
                    self.categorized_map[i][j] = "Mountain"
                elif categorized_map_int[i][j] == 2:
                    self.categorized_map[i][j] = "Hill"
                elif categorized_map_int[i][j] == 3:
                    self.categorized_map[i][j] = "Plains"
                elif categorized_map_int[i][j] == 4:
                    self.categorized_map[i][j] = "Water"
                elif categorized_map_int[i][j] == 5:
                    self.categorized_map[i][j] = "Plains"
        
        
        return self.categorized_map, self.categorized_map_int
    
    def save(self):
        # saves all the parameters to a file in the same directory as the script file
        with open("parameters.txt", "w") as f:
            f.write("size: " + str(self.size_) + "\n")
            f.write("seed: " + str(self.seed_) + "\n")
            f.write("max and min height: " + str(self.max_value_) + " " + str(self.min_value_) + "\n")
            f.write("map: " + str(self.map_) + "\n")
            f.write("median: " + str(self.median_) + "\n")
            f.write(f"categorized map :\n  {str(self.categorized_map)} \n")
            f.write("categorized map int: \n" + str(self.categorized_map_int) + "\n")
            

        
                  
        
                    
generator.__init__(generator,10, r.random(), 100000000, -100, 0.3, np.random.randint(10,32))
generator.generate_map(generator)
unformatted_map = generator.map_ + 0

#print(unformatted_map)

generator.smooth_map(generator)
formatted_map = generator.map_
#print(f"\n \n {formatted_map}" )

generator.categorize_map(generator)
#print(generator.categorized_map)
#generator.save(generator)
#print(f"unformatted_map: {unformatted_map}, \n \n formatted_map: {formatted_map}")

