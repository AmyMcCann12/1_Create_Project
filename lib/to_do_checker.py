def to_do_checker(text):
    if text == "":
        raise Exception("No text has been inputted!")
    return "TODO" in text.upper()

