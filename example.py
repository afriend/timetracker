from ClassTimetracker import * #get classes from ClassTimetracker file

import json


from pprint import pprint






track = Timetracker() # make myBuddy into a Calculator object

customer = track.parseCustomer()

print customer
# if customer variable is provided take it

# else ask for it







foo = track.getPythonDataFromFile('sample.json')


currenttime = time.strftime("%Y-%m-%d-%H:%M:%S")

newEntry = {
   currenttime : {
   	"time": {
        "start": "20:48",
        "end": "20:55"
    },
    "job": "XXXXXXXXXXXXXXX"
   }
}


foo.update(newEntry)


track.writePythonDataToFile('sample.json', foo)

