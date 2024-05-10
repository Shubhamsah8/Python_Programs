data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
        {"V": "S009"}, {"VIII": "S007"}]

# Using set to store the unique values
unique_values = set()

for d in data:
    for value in d.values():
        unique_values.add(value)

print("Unique Values: ",unique_values)
