In key value format
A key cannot be a list but can be a value

empty_dict = {}
empty_dict['key'] = value
menu["cheesecake"] = 8

Add multiple keys:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

Dict comprehension:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

#Get a key:
user_ids.get('superStackSmash', 100000) where 100000 is default value

#Remove a key value pair
- Remove if found else print No Prize
print(raffle.pop(320291, "No Prize"))


#Get All Keys:
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

for student in test_scores.keys():
 print(student)


#Get All Values:
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
 print(score_list)

list(test_scores.values())

#Get All Items:
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")
