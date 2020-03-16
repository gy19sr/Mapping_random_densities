# Assessment_2
This is the second project for GEOG5990 at Leeds University
please refer to my report on making the model
Student ID: 201378222

### Steps of the Model:
1. Brings in the environment
2. Initialising parameters
3. Create Unique agent IDs and attach agents to the environment
4. The agents leave the pub and randomly move until they find their home leaving a density trail behind them
5. Plot the density and end location of the agents 
6. Write a csv file of the density data

### List of Contents:
1. Model.py -- This is the main model that will be run
2. agentframework.py -- This is where code for the agents in the model are kept (essential to model)
3. in.txt -- This is the text file that holds the values for the environment (essential to model)
4. README.md -- This is what is currently being viewed, important details about the code and model within here
5. License -- This is the license agreement for the code within the repositry 
6. density.csv -- This is the end csv file that the model will write into
7. __pycache__ -- This is automatically generated folder, often kept hidden in repositories
8. Code summary.odt -- This word document explains the code making process and sources used as part of the assessment 2 criteria
9. UML diagram -- this word document holds the UML diagram as rquested as part of the assessment
10. environment_2 -- This is the text file that holds the values for the environment that will be edited to hold density as well 

### Prerequisites
Python 3.7
Anaconda3 (64bit) was used to make and test this model. 
The Spyder interface within Anaconda should be used to run the model. 

### Installing
install Anaconda3 with python 3.7 open Spyder. 
download whole repository to run model (model, in, agentframework are essential)	

## Instructions to run model:

1. Open "Model.py" in Spyder (Phthon).
2. Run model.
3. Several prints will show the end locations and ID's of the agents
4. the scatterplot will show the density and end locations
5. open the density csv file in notepad to see the end density values 


### How it should run:
A GUI should pop up where the model can be run from, as well as a figure testing the base environment.There should be an environment and one group of agents (white). The model will have all the agents leave the center pub and randomly move until they find an environment value with the same value as the agent ID. The agents should leave behind a trail of agent density.  The density will then be written into a csv file. 


### known issues and what to avoid:
The model can take a large amount of time to run even when not an animation, as it requires a large number of iterations for the drunks to naturally find their house. 

The csv cannot be opened in excel as the data is too long. Open in notepad or .txt file equivalent 

Agents don't always find their house, as it is just a random chance as to whether or not the model individuals reach their house. More time and processing power will lead to all individuals reaching their house.

If any issue in running the model occurs, please email gy19sr@leeds.ac.uk. A response will be given within two working days.

### Licensing:
found on repository

###  End
