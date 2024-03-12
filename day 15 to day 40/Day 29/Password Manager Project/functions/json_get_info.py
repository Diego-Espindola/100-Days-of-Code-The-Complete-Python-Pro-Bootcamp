import json


def find_most_used():
    try:
        email_counts = {}
        with open(r"C:\Users\Diego Espindola\Documents\GitHub\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for"
                  r"-2023\day 15 to day 40\Day 29\Password Manager Project\passwords_json.json", "r") as file:

            data = json.load(file)
            for user_data in data.values():
                email = user_data["email"]
                if email in email_counts:
                    email_counts[email] += 1
                else:
                    email_counts[email] = 1
            return max(email_counts, key=email_counts.get)
    except json.JSONDecodeError:
        return ""


def find_website(_website):
    try:
        with open(r"C:\Users\Diego Espindola\Documents\GitHub\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for"
                  r"-2023\day 15 to day 40\Day 29\Password Manager Project\passwords_json.json", "r") as file:

            data = json.load(file)
            json_info = data[_website]
            return json_info
    except (KeyError, json.JSONDecodeError):
        return False
