""" Westerosi House Database

An 'A Song of Ice and Fire' Program which lists the information of a chosen
House in Westeros, including the current lord and heir, and defining which
figure is the current head of that noble house.

Please note that all information provided is up to date following 'A Dance of Dragons'
by George R.R. Martin.

Using An API of Ice and Fire:
https://anapioficeandfire.com/
"""

""" PROGRAM SET UP:
    > Run the command: python -m pip install requests to install the module
    > No API key is needed to use this API
"""

import requests
import random

# Define the API link
API_LINK = "https://anapioficeandfire.com/api"

# Writing a function to find members of the searched house with info from the API
def get_house_members(house):
    house_member_list = []

    # Search for the head of house first
    current_lord_info = house["currentLord"]

    if current_lord_info != "" :
        current_lord_response = requests.get(current_lord_info)
        current_lord = current_lord_response.json()
        lord_name = current_lord["name"]

        if lord_name == "" :
            lord_name = "Head of house undefined."

        is_head_of_house = True  # Used a boolean to confirm if listed member is house head

        house_head_info = "Current Head of House: " + lord_name
        house_member_list.append(house_head_info)

    else:
        house_member_list.append("Current Head of House: None recorded.")

    # Now find information on the heir, same process as above
    heir_info = house["heir"]

    if heir_info != "" :
        heir_response = requests.get(heir_info)
        house_heir = heir_response.json()
        heir_name = house_heir["name"]

        if heir_name == "" :
            heir_name = "Heir to the house is unknown."

        is_head_of_house = False # False because this member is the heir, not the ruling lord.

        heir_info = "Heir: " + heir_name
        house_member_list.append(heir_info)

    else:
        house_member_list.append("Heir: None recorded.")
        # The if else statements are used to loop through the data to see if there is
        # a recorded heir under the searched house. Same as above for the ruling lord.

    return house_member_list

# Now we need a user input to find information on a Westerosi house
house_search = input("Enter a name of a noble house in Westeros: ").strip().lower()
print()

found_house = None  # Start off with none because the search hasn't happened yet
page_number = 1 # Start off at page one since we're searching the whole house directory

# Using a while loop to search through the house pages until all have been covered
while found_house is None :
    response = requests.get(f"{API_LINK}/houses?page={page_number}")
    houses = response.json()

    if len(houses) == 0:
        break # Cut the loop when all houses have been searched

    # Check if the searched house matches a house in the database exactly
    for house in houses:
        house_checker = house["name"].lower().split()

        if house_search in house_checker :
            found_house = house
            break

    page_number += 1

# When the searched house is found, print the information
if found_house != None :
    print("House Name:", found_house["name"])
    print("Region:", found_house["region"])
    print("Words:", '"' + found_house["words"] + '"')

# Checking if the noble house has an ancestral seat
    if len(found_house["seats"]) > 0:
        seat = found_house["seats"][0]
    else:
        seat = "No seat listed"

    print("Seat:", seat)
    print()

    # Recalling the house member function from above and print with house information
    house_members = get_house_members(found_house)

    for member in house_members:
        print(member)
    print()

    # Fun little ending message randomly chosen upon each search, keeping to theme
    ending_message = random.choice([
        "Your queries have been transcribed within the Citadel's archives.",
        "A raven flies diligently once more.",
        "The maesters ponder over future queries.",
        "Another house recorded into the vast histories of Westeros."
    ])

    print(ending_message)

    # Okay now to display information in a report and open as a file
    house_report = """
    ==============================
    Westerosi Noble House Database
    ==============================
    """
    house_report += "House Name: " + found_house["name"] + "\n"
    house_report += "Region: " + found_house["region"] + "\n"
    house_report += "Words: " + '"' + found_house["words"][:50] + '"' + "\n"
    house_report += "Seat: " + seat + "\n"

    for member in house_members:
        house_report += member + "\n"

    house_report += "\n" + ending_message

    # Now to write into a .txt file
    with open("westerosi_house_database.txt:" , "w") as file:
        file.write(house_report)

    print("Your search has been recorded in westerosi_house_database.txt")
    print()

else:
    print("House not found, please try searching for another.")








