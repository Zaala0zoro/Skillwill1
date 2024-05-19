#  დავალება 1.  დაწერე ფუნქცია, რომელსაც გადაეცემა
# Dictionary და დააბრუნებს რიცხვით value -
# ებს შორის მინიმალურს #
def find_min_value(d):
    if not d:
        raise ValueError("ლექსიკონი ცარიელია")

    values = d.values()

    if not all(isinstance(value, (int, float)) for value in values):
        raise ValueError("ყველა ცვლადი უნდა იყოს ინტეჯერ ტიპის")

    return min(values)


example_dict = {'a': 8, 'b': 2.6, 'c': 13, 'd': 20}
min_value = find_min_value(example_dict)
print(f"მინიმალური ცვლადი არის: {min_value}")


#  დავალება 2. დაწერე ფუნქცია, რომელსაც გადაეცემა
# რიცხვი n და რეკურსიულად დაითვლის n
# რიცხვის ფაქტორიალს #
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("შეყვანილი მონაცემი უნდა იყოს არანეგატიური რიცხვი!")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = 6
result = factorial(number)
print(f"The factorial of {number} is: {result}")
