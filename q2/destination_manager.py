destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("Vacay Destinations:")
for travel in destinations:
    print(travel)

print("Vacay spot na nasa budget mo:")
print(destinations[1:4])

google = str(input("Enter your dream vacay place: "))

if google in destinations:
    print("Yes! Punta ka na here.")
else:
    print("Cant find it. Ewan ko sayo jan.")

destinations[2] = "Iloilo"

print("Here are the updated destinations!")
print(destinations)

# The first lines make a list.
# The next line creates a for loop in which a variable "travel" is described to have the list of destinations.
# Another variable is used for the for loop.
# The next line prints the text and displays the destination from index 1 to 3. It starts as 1 and ends at 3, thats why 4 is used instead of 3.
# "google" is used as a variable to see what is tyoed in by the user. If the typed message is included in the list of destinations then it prints the text, yet if it doesnt then it prits the other text
# I used an if, else command.
# After that, a line is used to replace the item with index 2 with Iloilo instead. 
# The final 2 lined are used to print the text and to display the updated list. The list follows the new instructions instead of the old. 
# Instead of showing Davao as an item, it displays Iloilo.
