def calculate_addition(num_1):
    addition = num_1
    return addition


def calculate_addition2(num_2):
    addition2 = num_2
    return addition2


# Main
question = int(input("Enter first number: "))
question1 = int(input("Enter second number: "))
answer = calculate_addition(question + question1)
print(f" {question} + {question1} = {answer}")
