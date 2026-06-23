# Function with output

# title(): convert from kimhan to Kimhan
def format_name(first_name, last_name):
    """
        Take the first_name and last_name as the input
        Return fullname
    """
    
    return first_name.title() + " " + last_name.title()

print(format_name("kimhan", "teng"))

