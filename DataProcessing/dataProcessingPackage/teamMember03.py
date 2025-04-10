# File Name : teamMember03.py
# Student Name: Hailey Manuel, Will Claus, Abel Yemaneab
# email:  yemaneag@mail.uc.edu, clausws@mail.uc.edu, manuelhv@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   04/13/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment teaches us how to manipulate data from a csv

# Brief Description of what this module does. This module lists the total amount of cars per brand.
# Citations:

# teamMember03.py
from collections import Counter
class teamMember03:
    def print_something_interesting(self, data):
        try:
            brand_counts = Counter(row['Brand'] for row in data)
            print("Total amount of cars per brand:")
            for brand, count in brand_counts.most_common(5):
                print(f"{brand}: {count} listings")
        except Exception as e:
            print("teamMember03 Error:", e)