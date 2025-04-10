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