counties = ["Arapahoe","Denver","Jefferson"]
for Arapahoe in counties:
    print(Arapahoe)
for Denver in counties:
    print(Denver)


numbers = [0,1,2,3,4,]
for num in numbers:
    print(num)
for num in range(5):
    print(num)

counties_tuple = ("Arapahoe", "Denver", "Jefferson") 
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
for county in counties_tuple:
    print(counties)

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
      print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

voting_data = {"Arapahoe has 422829 registered voters"}, {"Denver county has 463353 registered voters"}, {"Jefferson county has 432438 registered voters"}
for county_dict in voting_data:
    print(county_dict) 


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['county'])

# f-string format
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes/total_votes)*100
print("I received" + str(percentage_votes)+ "% of the total votes.")

# Below is the edited coded above using the f-string method
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100} % of the total votes. ")

# Skill Drill using f-string with dictionaries
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.item():
    print(county + "county has" + str(voters) + "registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
# on line 67 is another metho using f-strings to make the code more intuitive and clear

# Multiline f-string
candidate_votes = 3345
total_votes = 23123
candidate_votes = int(input("How many votes did the you get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes} number of votes." f"The total number of votes in the election was {candidate_votes}." f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

# using thr Floating-Point decimals
candidate_votes = 3345
total_votes = 23123
candidate_votes = int(input("How many votes did the you get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"you recieved {candidate_votes:,} number of votes." f"The total number of votes in the election was {total_votes:,}." f"You recieved {candidate_votes/ total_votes* 100:.2f}% of the total votes.")
print(message_to_candidate)

# 3.2.11 Skill Drill 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

voting_data = {"Arapahoe has 422829 registered voters"}, {"Denver county has 463353 registered voters"}, {"Jefferson county has 432438 registered voters"}
for county_dict in voting_data:
    print(county_dict) 
    