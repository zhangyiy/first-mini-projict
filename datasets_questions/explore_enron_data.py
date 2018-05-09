#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print enron_data["SKILLING JEFFREY K"]["salary"]
#print enron_data["LAY KENNETH L"]['total_payments']
#print enron_data['FASTOW ANDREW S']['total_payments']
enron_data_values = enron_data.values()
count = 0
for i in range(len(enron_data_values)):
    if enron_data_values[i]["poi"] == 'true':
        if enron_data_values[i]["total_payments"] == 'NaN':
            count +=1
print count


