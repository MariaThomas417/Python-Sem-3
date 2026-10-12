import numpy as np
import pandas as pd

fees = np.array([15000, 25000, 30000, 40000, 20000])

print("Average Fee:", np.mean(fees))
print("Maximum Fee:", np.max(fees))
print("Minimum Fee:", np.min(fees))

data = {
    "Course": ["Python", "Java", "Data Science",
               "Cybersecurity", "Web Development"],
    "Fee": fees
}

df = pd.DataFrame(data)

print("\nCourse Fee Details:")
print(df)

print("\nCourses with fees greater than 25000:")
print(df[df["Fee"] > 25000])

"""
Output 

Average Fee: 26000.0
Maximum Fee: 40000
Minimum Fee: 15000

Course Fee Details:
            Course    Fee
0           Python  15000
1             Java  25000
2     Data Science  30000
3    Cybersecurity  40000
4  Web Development  20000

Courses with fees greater than 25000:
           Course    Fee
2    Data Science  30000
3   Cybersecurity  40000
"""