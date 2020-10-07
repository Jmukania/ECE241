# Jordy Mukania
# ECE 241 Project #1 Main Class
# Oct 3, 2020

class City:  # City Class

    def __init__(self, cityData):  # Initiates city object
        # Variables needed to set up attributes
        city = cityData.split(',')  # Delimiter (,) to split each cell in CSV file into array
        city_and_state = city[1]  # Array for city & and state in case to split more
        csSplit = city_and_state.split()  # Splits city and state into array
        state_Index = len(csSplit) - 1  # Index for state

        # Variables for City
        self.cid = city[0]  # City ID
        self.cname = ' '.join(csSplit[0:state_Index])  # City Name... Joins Name if more than one in array
        self.cstate = csSplit[state_Index]  # State name of city
        self.pop = city[2]  # Population of city
        self.cities = city[4:]  # Array w COVID data of confirmed cases for city

    def __str__(self):  # String that prints cid, cname, cstate and most recent confirmed cases for city object print
        return "cid: " + self.cid + "; cname: " + str(self.cname) + "; cstate: " + self.cstate + "; cases:" \
               + self.cities[len(self.cities) - 1]

# Code to test output

testCity = "23700, Forest City AR, 71492,21968,1064,1116,1144"
myCity = City(testCity)
print(myCity)
