# functions go here
def num_check(question):

#checks users enter an integer instead of characters
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# Main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit:  ")

    if name == "xxx":
        break

    age = num_check("Age ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry, you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again")
        continue

        tickets_sold += 1


print("You have sold {} ticket/s".format(tickets_sold))