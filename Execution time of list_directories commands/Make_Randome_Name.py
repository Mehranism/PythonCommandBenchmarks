def Make_randome_folder_name(Len):
    #The function Make_random_folder_name generates strings
    # of a given length by combining random combinations of
    # lowercase and uppercase English letters and numbers.
    # If you need to include other characters in generating
    # a random name, you can add them to the string Valid_chars.
    import string
    import random
    Valid_chars = string.digits+string.ascii_letters
    #Valid_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Name=""
    for i in range(Len):
        Name += Valid_chars[random.randint(0,len(Valid_chars)-1)]
    return Name