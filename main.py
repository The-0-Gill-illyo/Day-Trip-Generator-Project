import random


destinations = ["Disney Land Cruise!", "Hawaii!", "New Zeland!", "Hershey Park!"]
restraunts = ["Docking Bay 7 Food and Cargo, at Disney Land!","Itchy Butt(Chicken Joy), in Honolulu!", "The Shed te Motu, over looking the water in New Zeland!", "The Chocolate Avenue Grill, in Hersey Pennsylvania!"]
transportations = ["Celebry Bus Tour!", "10 Day/9 Night Cruise!", "First-Class Plane!", "RV Cross-County Trip!"]
entertainments = ["See Walt Disneys' apartment!", "Visit Hawaii Volcano National Park!", "Hobbit movie set tour!", "Hershey Park Kissing Tower!"]



user_choosen_destinatation = random.choice(destinations)
user_choosen_restraunt = random.choice(restraunts)
user_choosen_transportation = random.choice(transportations)
user_choosen_entertainment = random.choice(entertainments)


def display_travel_choices():
        print("Vacation Destination: " + user_choosen_destinatation)
        print("Dining Experience: " + user_choosen_restraunt)
        print("Travel Type: " + user_choosen_transportation)
        print("Tours and Vacation Sites: " + user_choosen_entertainment)

print("Hello, allow me to generate a random Day Trip for you")

confimed_trip = False

while not confimed_trip:
        display_travel_choices()

        respose = input("Would you like to go on the journey? yes or no   ")
        print(respose)

        if respose == "yes":
                print(f'Fantastic, Enjoy your trip at {user_choosen_destinatation}! The attractions at {user_choosen_entertainment}, accompanied with an excellent dining experience at {user_choosen_restraunt}. Please remember to travel safely and follow all third-party companies while traveling by {user_choosen_transportation}! Have a great trip!')
                confimed_trip = True
        elif respose == "no":
                print("Destination")
                print("Restraunt")
                print("Transportation")
                print("Entertainment")
                respose = input("Which would you like to change? ")

                if respose == "Destination":
                        user_choosen_destinatation = random.choice(destinations)
                elif respose == "Restraunt":
                        user_choosen_restraunt = random.choice(restraunts)
                elif respose == "Transportation":
                        user_choosen_transportation = random.choice(transportations)
                elif respose == "Entertainment":
                        user_choosen_entertainment = random.choice(entertainments)
        else:
                print("Invalid please try again")