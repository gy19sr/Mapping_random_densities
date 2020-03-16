# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:51:00 2019

@author: gy19sr


Planning for Drunks
 
Ipython Console can be set to inline, if not try Tkinter
"""


'''
Step 1: import required packages
'''

import matplotlib.pyplot #allows to use scatterplot functions 
import csv #allows for csv reader and writer functions
import agentframework #connects to agent framework 
matplotlib.use('TkAgg') #allows tinker plots
import tkinter #allows tinker functions





'''
Step 2: import and read the csv 'in' and 'environment_2'
'''


f = open('in.txt', newline='') 
#open the csv file in working directory 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#each row is returned as a list of strings

environment = [] # create environment list
for row in reader:				# A list of rows
    environment.append(row) #the rows read the environment values
    
f.close() #end work with the csv




'''
environment_2 is where the density map will be displayed
'''
f = open('environment_2.txt', newline='') 
#open the csv file in working directory 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#each row is returned as a list of strings

environment2 = [] # create environment list
for row in reader:				# A list of rows
    environment2.append(row) #the rows read the environment values
    
f.close() #end work with the csv




'''
Optional step: test if environment is showing up correctly
    will pop up as figure if tinker used
'''

#matplotlib.pyplot.xlim(0,300)
#matplotlib.pyplot.ylim(0,300)
#matplotlib.pyplot.imshow(environment)






'''
Step 3: Initialising parameters
'''
num_of_agents = 25 #the number of drunks,the offcial model is 25 of them
num_of_iterations = 800000 # may take some time to fully run the model , but will lead to most accurate result
agents = [] # a list for the drunks to attach the framework to
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #setting up scatterplot size
ax = fig.add_axes([0, 0, 1, 1]) #setting up scatterplot axis





'''
Optional step: find out pub and home points
'''

#to find xy locations of the pub and houses if need be
print ("environment[] =", environment[148]) #find out where the pub is located good for y axis, just replace list row till 1 no longer shows up 
specific = environment[148].index(180.0)  #set specific to the y value and search for 1
print("specific =", specific) # find the specific locations of pubs earliest x axis 

#tests on how to find house and pub id's and loactions if done house by house
houseID = environment[148][22] #setting House ID = to environment specific location
print ("house ID =", houseID) #display value of house ID


###switch to one agent at a time!!







'''
Step 4: Create a Unique ID for each Agent, and add the environment and agentframework to the list
'''

for i in range(num_of_agents): # create a loop for number of agents
    agentID = ((1+i)*10) # setting to agents value by multiplying each number by 10
    print ("agentID =",agentID) #display agents increasing in ID by factor of 10 to test if done correctly
    agents.append(agentframework.Agent(environment,agents,agentID, environment2)) #attach frameworks environment, agents, agentID and xy to agents
    agent_location = agents[i] #creating value that holds the x y location of each agent
    print("agent starting location=",agents[i]) #display agent location to test if in correct range
    






'''
Step 5: Agents leave the bar and move randomly until the agent finds its home
'''



for j in range(num_of_iterations): #for each iteration
    for i in range(num_of_agents): #for each agent within each iteration 
        agent_location = agents[i]  #creating value that holds the x y location of each agent
        agentID = ((1+i)*10) # setting to agents value by multiplying each number by 10
        if environment [agent_location.y][agent_location.x] == agent_location.agentID: # if the enviuronment value is equal to agent ID
            agents[i].stop()
            #for i in range(num_of_agents):
                #print ("4")
            #when the agent ID is equal to the environment value stop that agent 
            #some print tests, best to do with low iterations (10000) and agent num (5)
            #switch between != and == to see if prints agents at home after move
            #print("supposed to stop")
            #print("agent ID = ",agentID)
            #print("location after move",agents[i])
            #print("environment value",environment[agent_location.y][agent_location.x])
        else:
            #agents[i].share_with_neighbours(neighbourhood)
            agents[i].density()
            agents[i].move() #move up and down, left and right randomly by 1 unit
            #add a value of 1 to environment for each location it is in
            #if the values are not equal then move the agents and add density
            #to test if moving and same ID
            #print ("agentID =",agentID)
            #print ("agent after move =", agents[i])
            #print("envoronment value =",environment[agent_location.y][agent_location.x]) ## will read 0's and 1's so it's working



'''
optional change: if you wish for the agents to leave the pub one at a time and reach its home, then the next agent goes, comment out the code above and use the code below
'''


"""
for i in range(num_of_agents): #for each agent
    for j in range(num_of_iterations): #fun the set up iterations
        agent_location = agents[i]  #creating value that holds the x y location of each agent
        agentID = ((1+i)*10) # setting to agents value by multiplying each number by 10
        if environment [agent_location.y][agent_location.x] == agent_location.agentID:
            agents[i].stop()
        else:
            agents[i].move() 
            agents[i].density()
"""




            
'''
Step 6: test environment density and end locations of agentIDs
'''


#testing if enviroment is adding to it's density       
print ("environment2[] =", environment2[264]) 


#print end locations and values. this wwill tell you how many agents have reached their home when agent ids line up with environment values
for i in range(num_of_agents): #for each agent
    agentID = ((1+i)*10) #set agent ID
    agent_location = agents[i] #create agent location marker
    if environment [agent_location.y][agent_location.x] == agent_location.agentID: #if the environment value equals the agent ID
        print ("end agentID =",agentID) #display eache agent ID
        print("end agent location=",agents[i]) #display their end location
        print("end envoronment value =",environment[agent_location.y][agent_location.x]) #print the value to see if matches agent ID
        print("arrived home") #say the drunk was successful
    else:
        print("failed drunk") #say that the drunk couldn't find its home



'''
Optional step 7: print without a gui 
    #this method is better for testing, just comment out the gui option
'''



print("scatter plot")


matplotlib.pyplot.imshow(environment) #attach the environment to the scatterplot
for i in range(num_of_agents): #for each agent
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='white') #plot end location of agents
matplotlib.pyplot.show() #display the scatterplot





'''
Step 8: create csv with new environment data
'''


density = environment2 # new name for the newly updated environment list

with open('density.csv', 'w', newline='') as csvfile: #open the csv called density in the folder
    testwriter = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_NONNUMERIC) #create the writting settings
    testwriter.writerow(density) #write the new data to the density csv in row format

#go to the folder to see if it has changed the enviroment values from 0 or look printed environment line
#note with density map, house locations are included and should be regarded as unique values not an indication that steps were taken there

f.close() 


'''
Step 9: display the final density map and agent locations in a GUI
'''


#matplotlib.pyplot.scatter(hidden[0][1], hidden[0][0], color='red')


        
def run(): #creat a definition for when run is used
    matplotlib.pyplot.imshow(environment2) #attach the environment to the scatterplot  
    for i in range(num_of_agents): #for each agent
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='white') #plot end location of agents 
    canvas.draw() #show the scatterplot on the canvas not on the 
    #matplotlib.pyplot.show() #display the scatterplot



root = tkinter.Tk() # giving tkinter an ID
root.wm_title("Model") # put a title in the top bar
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) #putting in a blank canvas
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)  #putting in a blank canvas


frame = tkinter.Frame(root) #set frame
frame.pack() #pack the frame

run_button = tkinter.Button(frame,
#create a run button
                   text="Run Model",
                   command=run)
#button runs model
run_button.pack(side=tkinter.LEFT)
#place button left side



quit_button = tkinter.Button(frame, 
#quit button 
                   text="QUIT", 
                   fg="red",
                   command=root.destroy)
#clicking destroys the root
quit_button.pack(side=tkinter.LEFT)
#place button next to run 


menubar = tkinter.Menu(root) #sets a menubar definition
root.config(menu=menubar) #configure a new menubar
model_menu = tkinter.Menu(menubar) #the menu bar will host the model
menubar.add_cascade(label="Model", menu=model_menu) #add a dropdown to the menubar
model_menu.add_command(label="Run model", command=run, state="normal") #the dropdown can run the model

w = tkinter.Canvas(root, width=10, height=10) #set canvas size
w.pack()

tkinter.mainloop() #close the tkinter loop



'''
end of model
'''
