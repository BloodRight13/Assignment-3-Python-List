#Task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:13]
print ("The second week tempatures are:", second_week)

#Task 2
temperatures.remove(101)
print(temperatures)

#Task 3
temperatures.sort(reverse=True)
print(temperatures)
print(temperatures[4:9])