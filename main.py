import random


destinations = ["Disney Land", "Hawaii", "New Zeland", "Hershey Park"]
restraunts = ["Docking Bay 7 Food and Cargo","Itchy Butt(Chicken Joy)", "The Shed te Motu", "The Chocolate Avenue Grill"]
transportations = ["Bus", "Cruise", "Plane", "RV"]
entertainments = ["See Walt Disneys' apartment", "Visit Hawaii Volcano National Park", "Hobbit movie set tour", "Hershey Park Kissing Tower"]

print("Hello, allow me to generate a random Day Trip for you") 

def make_a_decision(destinations, restraunts, transportations, entertainments):
    day_trip = destinations + restraunts + transportations + entertainments
    user_yes = "Yes"
    no_way = "No"
    print(random.choice(destinations))

    print(random.choice(restraunts))
    print(random.choice(transportations))
    print(random.choice(entertainments))
    input("Do you like this trip, or would you like to change something? Yes or No? ")
    if day_trip == user_yes:
        print("Great, you'll enjoy what's planned!")

        return day_trip
    
result_from_user = make_a_decision(destinations, restraunts, transportations, entertainments)
    
    
    
    
    
    #     return make_a_decision()
    # day_trip()
            # fine_dinning = random.choice(restraunts)
    # no_fighting = random.choice(trasnsportations)
    # that_was_fun = random.choice(entertainments)
    # return result_journey
    


# input("Would you want to confirm or change these choices? ")
# user_input = sounds_great = "Confirm"
# print(sounds_great)
# user_input = change_something = "Change something"
# print(random.choice(destinations))
# print(random.choice(restraunts))
# print(random.choice(trasnsportations))
# print(random.choice(entertainments))

# def make_a_decision(favorite_spot, fine_dinning, no_fighting, that_was_fun):
#     result_journey = favorite_spot + fine_dinning + no_fighting + that_was_fun
#     return result_journey



# change_something == True
# print(destinations = random.choice(destinations))
# print(restraunts = random.choice(restraunts))
# print(trasnsportations = random.choice(trasnsportations))
# print(entertainments = random.choice(entertainments))


# def favorite_trip_selection(souds_great, change_something):
#     if souds_great == True:
#         print("Great, have a wonderful trip!")
#     elif change_something == False:
#         print(destinations = random.choice(destinations))
#         print(restraunts = random.choice(restraunts))
#         print(trasnsportations = random.choice(trasnsportations))
#         print(entertainments = random.choice(entertainments))
#         return favorite_trip_selection
#         print(favorite_trip_selection)

# favorite_trip_selection()


# fav_trip = False
# trip_choice = False

# display trip to user
# prompt user t confirm or change trip?
# 





# def user_choice():

#     fav_trip == user_choice
#     input("Do you like these options?")
#     while fav_trip in trip_choice == True:
#         if trip_choice == fav_trip:
#             print("Sounds great, have a blast!")
#         elif trip_choice != fav_trip:
#             print("which item would you like to change?")
#             new_choice = fav_trip(random.choice)
#             return new_choice
#             print(user_choice)

#         user_choice()
