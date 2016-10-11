#ClassTimetracker.py 
import time
import json
import sys, os
import argparse

from Tkinter import *

class Timetracker(object):

    #define class to simulate a simple tu

    def __init__ (self):

        #start with zero

        self.current = 0

    def add(self, amount):

        #add number to current

        self.current += amount

    def getCurrent(self):

        return self.current

    def createFileIfNotExists():
        filename = time.strftime("%Y-%m-%d")
        f = open(filename, 'w')
        f.close()    

    def getPythonDataFromFile(self, filename):
        # Reading data back
        filepath =  os.path.dirname(sys.argv[0]) + "/" + filename
        with open(filepath) as data_file:    
            data = json.load(data_file)

        data_file.close()
        return data     

    def writePythonDataToFile(self, filename, data):
        print "hello bob"
        filepath =  os.path.dirname(sys.argv[0]) + "/" + filename
        print "what?"
        json_data = json.dumps(data, sort_keys=True)
        #json_data = json.dump(data, sort_keys=True)

        #pprint(json_data)




        with open(filepath, 'w') as data_file:   
            data_file.write(json_data)
            #json.dump(json_data, data_file)

 

    def parseCustomer(self):
        parser = argparse.ArgumentParser(description='Description of your program')
        parser.add_argument('-p','--project', help='Project to track', required=False)
        args = vars(parser.parse_args())

        if args['project']:
            return args['project']
        else: 
            print "query project"
            return self.queryProject()

    def queryProject(self):
        master = Tk()
        Label(master, text="Projekt / Taetigkeit").grid(row=0)

        e1 = Entry(master)

        e1.grid(row=0, column=1)
        master.bind('<Return>', self.assign_customer)
        Button(master, text='Show', command=self.assign_customer).grid(row=3, column=1, sticky=W, pady=4)

        mainloop( )

    def assign_customer(self):
        print("Assigned customer: %s\n" % (e1.get()))
        master.quit()
        