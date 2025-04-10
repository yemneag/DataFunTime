# teamMember01.py

# teamMember01.py
# File Name : teamMember01.py
# Student Name: Hailey Manuel, Will Claus, Abel Yemaneab
# email:  yemaneag@mail.uc.edu, clausws@mail.uc.edu, manuelhv@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   04/13/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment teaches us how to manipulate data from a csv

# Brief Description of what this module does. This module lists the average size of a car engine within the dataset.
# Citations: N/A

class teamMember01:
    def print_something_interesting(self, data):
        engine_sizes = [
                float(row['Engine_Size']) 
                for row in data 
                if row['Engine_Size'].replace('.', '', 1).isdigit()
            ]

        if not engine_sizes:
                print("No valid engine size data found.")
                return

        average_engine_size = sum(engine_sizes) / len(engine_sizes)
        print(f"\nAverage Engine Size: {average_engine_size:.2f} L \n")
 

