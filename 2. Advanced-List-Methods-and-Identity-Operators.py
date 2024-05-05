#Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
sorted_submitted = sorted(submitted)
attended = ["Charlie", "Eve", "Alice", "Frank"]
sorted_attended = sorted(attended)
print(sorted_submitted, sorted_attended)

if "Alice" in submitted and "Alice" in attended: print("Alice attended and submitted")
if "Bob" in submitted and "Bob" in attended: print("Bob attended and submitted.")
if "Charlie" in submitted and "Charlie" in attended: print("Charlie attended and submitted.")
if "David" in submitted and "David"  in attended: print("David attended and submitted.")
if "Eve"  in submitted and "Eve" in attended: print("Eve attended and submitted.")
if "Frank"  in submitted and "Frank" in attended: print("Frank attended and submitted.")

#Task 2

if submitted == attended:
    print("The attended and sumbmited list are the same.")
else:
    print("The lists are not the same.")

#Task 3
attended.remove("Eve")
attended.remove("Frank")
print(attended)
