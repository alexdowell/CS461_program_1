# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:42:14 2022

@author: alexa
"""

import math as m
import matplotlib.pyplot as plt # plotting tools
import time
import sys
#cities_x_y = []
#contents_list = []
#with open('coordinates.txt') as f:
#    for line in f:
#        contents = f.read()
#        cities_x_y = contents
#        contents_list = contents.split(",")
#                                                   ###working on importing data
#
#for line in open('coordinates.txt').readlines():
#    line = line.strip()
#    cities_x_y.append(line)
#    cities_x_y.append(line[1])
#    cities_x_y.append( line[2])
#
#print(cities_x_y)

        
        
def compute_distance(current_pos, another_pos):
    """compute distance"""
    dist = m.sqrt((another_pos[0] - current_pos[0])**2+(another_pos[1]- current_pos[1])**2)
    return dist


def city_xycost_finder(cities_x_y, current_city_name, goal):
    current_city =[]
    for city in cities_x_y: 
            if city[0] == current_city_name:
                
                dist = compute_distance([city[1], city[2]], [goal[1], goal[2]])
                current_city = [city[0], city[1], city[2], dist]
                return current_city


                



if __name__=='__main__':
    cities_x_y = [["Abilene", 38.9220277, -97.2666667],["Andover", 37.6868403, -97.1657752], ["Anthony", 37.1575168, -98.0728946], ["Argonia", 37.2670166, -97.7726807], ["Attica", 37.2421271, -98.2351967], ["Augusta", 37.6913277, -97.0537108], ["Bluff_City", 37.0760844, -97.8793212], ["Caldwell", 37.0346731, -97.6179436], ["Cheney", 37.632882, -97.789442], ["Clearwater", 37.5166968, -97.5325458], ["Coldwater", 37.2574937, -99.3549149], ["Derby", 37.5517122, -97.2867892], ["El_Dorado", 37.8098997, -96.8943313], ["Emporia", 38.3792991, -96.2615044], ["Florence", 38.2434672, -96.9378672], ["Greensburg", 37.6050677, -99.3005641], ["Harper", 37.2852232, -98.0368352], ["Haven", 37.9020486, -97.7926952], ["Hillsboro", 38.3494571, -97.2156415], ["Hutchinson", 38.0572062, -97.9414547], ["Junction_City", 39.0379342, -96.8799338], ["Kingman", 37.6480942, -98.1693967], ["Kiowa", 37.0190996, -98.4940572], ["Leon", 37.6892622, -96.7916587], ["Lyons", 38.3477177, -98.22167], ["Manhattan", 39.1682049, -96.6901159], ["Marion", 38.3589767, -97.0267385], ["Mayfield", 37.2618658,  -97.5508871], ["McPherson", 38.3704302, -97.6917722], ["Medicine_Lodge", 37.2855616,  -98.5888462], ["Mulvane", 37.4868677, -97.2575929], ["Newton", 38.0353742, -97.4239353], ["Oxford",  37.2734026, -97.1777267], ["Pratt", 37.6753423, -98.7769217], ["Rago", 37.4527946, -98.0905053], ["Salina", 38.8254325, -97.702327], ["Sawyer", 37.4972558, -98.6880621], ["South_Haven", 7.0497874, -97.4052061], ["Topeka", 39.0130335, -95.7782425], ["Towanda", 37.7971427, -97.0063152], ["Viola", 37.4827584, -97.6496081], ["Wellington", 37.2691963, -97.5199806], ["Wichita", 37.6645257, -97.5841207], ["Winfield", 37.2844228,  -96.999848], ["Zenda", 37.4447194, -98.2849356]]
    adjecent_cities_list = [["Anthony", "Bluff_City", "Kiowa", "Attica", "Harper"], ["Attica", "Medicine_Lodge"], ["Augusta", "Winfield", "Andover", "Leon", "Wichita"], ["Caldwell", "South_Haven", "Bluff_City", "Mayfield"], ["El_Dorado", "Towanda", "Andover", "Augusta", "Emporia"], ["Florence", "McPherson", "Hillsboro", "El_Dorado"], ["Greensburg", "Coldwater", "Pratt"], ["Harper", "Anthony", "Argonia", "Rago"], ["Hutchinson", "Newton", "Haven"], ["Junction_City", "Abilene", "Marion", "Manhattan", "Topeka"], ["Kingman", "Cheney", "Pratt", "Hutchinson"], ["Marion", "McPherson", "Newton", "Emporia"], ["Mayfield", "Wellington", "Caldwell", "Argonia"], ["McPherson", "Salina", "Lyons", "Hillsboro"], ["Medicine_Lodge", "Attica", "Kiowa", "Coldwater"], ["Newton", "McPherson", "Hutchinson", "Florence"], ["Rago", "Viola", "Sawyer"], ["Salina", "Abilene", "Hays"], ["Sawyer", "Pratt", "Zenda"], ["Wellington", "Oxford",  "Mayfield", "Mulvane", "South_Haven"], ["Wichita", "Derby", "Clearwater", "Cheney", "Mulvane", "Andover", "Newton", "El_Dorado"]]
    
    for city in cities_x_y:
        print(city[0])
        
    start_name = str(input("Enter starting city from the above list: "))
    count = 0
    for city in cities_x_y:
        if city[0] == start_name:
            count = count + 1
    if count != 1:
        print("ERROR!! not a valid city.")
        print("ERROR!! reopen and try again.")
        sys.exit()
    goal_name = str(input("Enter ending city from the above list: ")) 
    for city in cities_x_y:
        if city[0] == goal_name:
            count = count + 1
    if count != 2:
        print("ERROR!! not a valid city.")
        print("ERROR!! reopen and try again.")
        sys.exit()
    for city in cities_x_y: 
            if city[0] == goal_name:
                goal = city
                goal.append(0)
                
    frontier = [] # where I can go but haven't gone to yet
    been_there = [] # been to these spots

    current_city = city_xycost_finder(cities_x_y, start_name, goal)
    start_city = current_city
    frontier.append(current_city)
    start_time = time.time()
    ### Astar ########################
    count = 0
    while len(frontier) != 0:
#        if count == 7:
#            break
#        count = count + 1
        city_cost_min = []
        for city in frontier:    # finding the min cost of cities in frontier 
            city_cost_min.append(city[3])

        current_min_cost = min(city_cost_min)
#        print("current_min_cost", current_min_cost)
        for city in frontier:
            if city[3] == current_min_cost:                    
                current_city = city
#                print("the frontier1:", frontier)
                been_there.append(current_city)

        if current_min_cost == 0 :
            print("break")# breaks when you reach the goal
            break
        frontier_city_names =[]
        temp_frontier = []
        for adjecent_cities in adjecent_cities_list: # finding cities adjecent to the current city
            for city in adjecent_cities:
                
                    if current_city[0] == city:
                        temp_frontier.append(adjecent_cities) 
#                        print("the temp frontier", temp_frontier)
        for tier in temp_frontier:  # checking to see if there is any duplicate cities
            for city in tier:
                if city == current_city[0]:
                    continue
                if city not in frontier_city_names:
                    frontier_city_names.append(city)
        count = 0
        for city in frontier_city_names:    # making sure we don't revisit been there
            for path_city in been_there:
                if city == path_city[0]:
#                    print("the Problem:", city)
                    frontier_city_names.remove(city)
                    count = count + 1
                    if count == 1:
                        break
        frontier = []
        for city in frontier_city_names:
            for town in cities_x_y:
                if town[0] == city:
                    if city == goal[0]:
                        frontier.append(goal)
                        continue
                    city2goal = compute_distance([town[1], town[2]], [goal[1], goal[2]])
                    city2city = compute_distance([current_city[1], current_city[2]], [town[1], town[2]])
                    dist = city2goal + city2city
                    frontier_city = [town[0], town[1], town[2], dist]
                    frontier.append(frontier_city)
#                    print("the_frontier is",frontier)
    count = -1
    count2 = 0
    indexlist = []
    for a in been_there:
        print("a")
        for b in been_there:
            print("b:", b)
            print(count)
            count = count + 1
            if a == b:
                count2 = count2 + 1
                indexlist.append(count)
            if count2 == 2:
                break
    final_there = []
    count = 0
    for a in been_there:
        if indexlist[0] == count:
            break
        final_there.append(a)
        count = count + 1
    count = 0
    b  = 0
    for a in been_there:
        if indexlist[1] <= count:  
            final_there.append(a)
        count = count + 1  
#        if len(frontier_city_names) == 1: #next check
#            print("yo")
#            for city in been_there:
#                if city == frontier_city_names:
#                    been_there.remove(city)
    path_x =[]
    path_y =[]
    path_x_y =[]
    path_city_names =[]
    path_cost = 0

    print("the path is: ")
    count = 1
    for city in final_there:
        path_x.append(city[1])
        path_y.append(city[2])
        path_x_y.append([city[1], city[2]])
        path_city_names.append(city[0])
        path_cost = path_cost + city[3]
        if city[0] == start_city[0]:
            print("ending at city: ", start_city[0] , start_city[1], start_city[2])
            continue
        print("city #", count,": ", city[0], city[1], city[2] )
        count = count + 1
        if city[0] == goal[0]:
            print("beginning at city: ", goal[0] , goal[1], goal[2])
    print("runtime : --- %s seconds ---" % (time.time() - start_time))
    plt.plot(start_city[1], start_city[2], marker="x", color="red")
    plt.text(start_city[1], start_city[2], start_city[0], horizontalalignment='right', fontsize=7)
    plt.plot(goal[1], goal[2], marker="x", color="red")
    plt.text(goal[1], goal[2], goal[0], horizontalalignment='right', fontsize=7)

    for city in cities_x_y:
        if city[0] == start_city[0]:
            continue
        if city[0] == goal[0]:
            continue
        if city[0] == 'South_Haven':
            for place in been_there:
                if place[0] == 'South_Haven':
                    plt.plot(city[1],city[2] , marker="x",color="blue")
                    plt.text(city[1], city[2], city[0], horizontalalignment='right', fontsize=7)
            continue
        plt.plot(city[1],city[2] , marker="x",color="blue")
        plt.text(city[1], city[2], city[0], horizontalalignment='right', fontsize=7)

    plt.plot(path_x,path_y)

    
    #gridlines#
    plt.grid()
    plt.grid(which='minor')
    plt.minorticks_on()

        
                
                
    
   
                
