
def get_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")

def get_age(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) >= 0:
            return int(value)
        print("Please enter a valid non-negative integer for age.")

def main():
    print("Welcome! I'll create a short personal introduction for you.")
    name = get_nonempty("What's your name? ")
    age = get_age("How old are you? ")
    hobby = get_nonempty("What's a hobby you enjoy? ")

    print("\n--- Your Personal Introduction ---")
    print(f"Hello, {name}! ")
    print(f"You are {age} years old.")
    print(f"A hobby you enjoy is: {hobby}.")
    print("Nice to meet you! Have a great day ")

if __name__ == "__main__":
    main()
