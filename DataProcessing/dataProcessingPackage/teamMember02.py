# File Name : teamMember02.py
# Student Name: Will Claus, Hailey Manuel, Abel Yemaneab
# email:  clausws@mail.uc.edu, manuelhv@mail.uc.edu, yemaaneag@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   04/13/25
# Course #/Section:   IS4010-001
# Semester/Year:   2/2025
# Brief Description of the assignment:  This assignment shows how to show something interesting from a csv file

# Brief Description of what this module does. This module shows how to show the total number of electric vehicles from a csv file

# Anything else that's relevant:

# Citations: https://colab.research.google.com/drive/10Je9XNf257cSQA2GVrpAQmXod_toq_je

from CSVUtilitiesPackage.CSVUtilities import *
class teamMember02:
    def print_something_interesting(self, data):
            
                electric_counts = [row for row in data if row["Fuel_Type"].strip().lower() == 'electric']
                print(f"Total Electric Cars: {len(electric_counts)}")





