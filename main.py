import random

destinations = ["Disney Land", "Hawaii", "New Zeland", "Hershey Park"]
restraunts = ["Docking Bay 7 Food and Cargo","Itchy Butt(Chicken Joy)", "The Shed te Motu", "The Chocolate Avenue Grill"]
trasnsportations = ["Bus", "Cruise", "Plane", "RV"]
entertainments = ["See Walt Disneys' apartment", "Visit Hawaii Volcano National Park", "Hobbit movie set tour", "Hershey Park Kissing Tower"]

fav_trip = destinations
fine_dinning = restraunts
no_fighting = trasnsportations
that_was_fun = entertainments

print(random.choice(fav_trip))
print(random.choice(fine_dinning))
print(random.choice(no_fighting))
print(random.choice(that_was_fun))