"""
SET 3 - TASK 5: Check whether a route description is a palindrome.
Ignores letter case, spaces and punctuation/separators.
Run: python task5_palindrome_route_description.py
"""

def is_route_palindrome(description):
    left = 0
    right = len(description) - 1

    while left < right:
        # Skip characters that are not letters or digits.
        while left < right and not description[left].isalnum():
            left += 1
        while left < right and not description[right].isalnum():
            right -= 1

        if description[left].casefold() != description[right].casefold():
            return False
        left += 1
        right -= 1

    return True


def main():
    print("SET 3 - TASK 5: ROUTE PALINDROME CHECKER")
    examples = [
        "HUB-A, HUB-B, HUB-A",
        "A-B-C-B-A",
        "HUB-A to HUB-C",
        "Madam, I'm Adam",
    ]

    for route in examples:
        print(f"{route!r} ->", "PALINDROME" if is_route_palindrome(route) else "NOT A PALINDROME")

    user_route = input("\nEnter a route description to check (or press Enter to skip): ").strip()
    if user_route:
        print("Result:", "PALINDROME" if is_route_palindrome(user_route) else "NOT A PALINDROME")


if __name__ == "__main__":
    main()
