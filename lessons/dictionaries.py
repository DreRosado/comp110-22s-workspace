"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionaryu
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Acess a value by its key -- "lookup"
print("UNC has " + str(schools['UNC']) + " students")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

schools["Duke"] = 6717 

is_duke_present: bool = "Duke" in schools
print("Duke is present: " + str(is_duke_present))
print(schools)

# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")