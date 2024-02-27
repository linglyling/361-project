# 361test
Communication contract
The microservice reads a JSON file (named "schedule.students.json") in the format of a list of dictionaries where each dictionary corresponds to an individual's information. It then outputs a file called calendar.json that makes a calendar of days and what times are open to be booked by people by blocking out days that are supposed to be booked from "schedule.students.json". You must have a file named "schedule.students.json" for the microservice to use.
Here is an example of a way to request data from the microservice, called "MakeCalendar.py".

##############################################################

import subprocess

subprocess.run(["python", "MakeCalendar.py"])

##############################################################

You would then have a file called calendar.json. There are many ways to get information from a json file. Here is an example of one way:

##############################################################

import json
with open('calendar.json', 'r') as infile:
    calendar = json.load(infile)
print(calendar)

##############################################################

UML diagram:
![image](https://github.com/linglyling/361-project/assets/66285417/97a7726c-ff1a-43d1-8257-315a429aae1a)

