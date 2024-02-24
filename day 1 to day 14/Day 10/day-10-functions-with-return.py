def format_name(f_name, l_name):
    # Doc strings, to documentate while calling functions
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


formated_string = format_name(input("What is your first name? "),
                              input("What is your last name? "))
print(formated_string)
