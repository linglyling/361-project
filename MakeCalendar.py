import json

with open('schedule.students.json', 'r') as infile:
    input_file = json.load(infile)

calendar = {"Monday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Tuesday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Wednesday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Thursday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Friday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Saturday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            "Sunday": {3: "OPEN", 4: "OPEN", 5: "OPEN", 6: "OPEN", 7: "OPEN", 8: "OPEN", 9: "OPEN"},
            }

for entry in input_file:
    calendar[entry["date"]][entry["time"]] = "BLOCK"

with open('calendar.json', 'w') as outfile:
    json.dump(calendar, outfile)
