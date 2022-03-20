import random as r
import math as m
import numpy as np

class generator:
    def __init__(self, size, seed, max_value, min_value, water_probability, land_probability):
        self.size_ = size
        self.seed_ = r.seed(seed)
        self.max_value_ = max_value
        self.min_value_ = min_value
        self.water_probability_ = water_probability
        self.land_probability_ = land_probability
        self.map_ = np.zeros((size, size) ,dtype=int)
        # mage a vareable to store the median value of the map
        self.median_ = 0
    
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
        self.normalized_map_ = np.round(self.map_ / self.median_)
        # return the map
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
        self.normalized_map_ = np.round(self.map_ / self.median_)
        # return the map
           
        return self.map_ , self.median_ , self.normalized_map_

    def temp_map(self):
        self.mountain = self.median_ * 0.5
        self.plato = self.median_ * 0.25
        self.normal_land = self.median_
        self.low_land = self.median_ / 2
        self.temp_map = np.zeros((self.size_, self.size_) ,dtype=str)
    
    # generate a temprature map based on the heinght of the map and based on water and land
    # the higher the value the colder the temprature
    # the tempratures will affect other tempratures on the map
    # the temprature map will be used to generate the other maps
    
        for i in range(self.size_):
            for j in range(self.size_):
                if self.map_[i][j] >= self.mountain:
                    self.temp_map[i][j] = "mountain"
                elif self.map_[i][j] >= self.plato:
                    self.temp_map[i][j] = "plato"
                elif self.map_[i][j] >= self.normal_land:
                    self.temp_map[i][j] = "normal_land"
                elif self.map_[i][j] >= self.low_land:
                    self.temp_map[i][j] = "low_land"
                else:
                    self.temp_map[i][j] = "water"
            
        return self.temp_map
    

generator.__init__(generator,10, r.random(), 100, -100, 0.3, 0.4)
print(f"{generator.generate_map(generator)} \n \n {generator.smooth_map(generator)} \n \n {generator.temp_map(generator)}")
