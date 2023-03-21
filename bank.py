def main():
   user_greeting = input("Greeting: ")
   value_returned = value(user_greeting)
   print(value_returned)


def value(greeting):
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("hello world"):
       return 0
    elif greeting_lower.startswith("h"):
       return 20
    else:
        return 100


if __name__ == "__main__":
    main()