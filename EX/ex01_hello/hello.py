def hello():
    """EX01 hello."""
    """
    
    1. Print Hello
    Example output:
    What is your name? Mari
    Hello, Mari! Enter a random number: 5
    Great! Now enter a second random number: 4
    5 + 4 is 9
    """
    # ask for a name
    name = input("What is your name? ")
    # ask for first random number
    num1 = int(input(f"Hello, {name}! Enter a random number: "))
    # ask for second random number
    num2 = int(input("Great! Now enter a second random number: "))
    # print out sum
    print(num1, "+", num2, " is ", str(num1 + num2) + ".")


def poem():
    """
    2. Poem

    Example output:
    Roses are red,
    violets are blue,
    I love to code
    And so will you!
    """
    color = input("Name your favourite color: ")
    objects = input("Name an object in plural: ")
    activity = input("Name an activity ")
    print(f"Roses are {color},\n{objects} are blue,\nI love to {activity} \n And so will you!")


def greetings_greetings_greetings():
    """
    3. GreetingsGreetingsGreetings

    Example output:
    Enter a greeting: Hello
    Enter a recipient: world
    How many times to repeat: 3
    Hello world! Hello world! Hello world!
    """
    greeting = input("Enter a greeting: ") + " "
    recipient = input("Enter a recipient: ") + " "
    times = input("How many times to repeat: ")
    full_greet = (greeting + recipient) * int(times)
    print(full_greet)


hello()
poem()
greetings_greetings_greetings()
