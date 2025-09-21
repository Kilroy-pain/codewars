def find_missing_letter(chars):
    #checking the validity of the array
    if len(chars) < 2:
        print("Array must have at least 2 letters")
    else:
        pass
    #checking presence of any skipped position in the alphabet
    for letter in range(len(chars) - 1):
        if ord(chars[letter + 1]) - ord(chars[letter]) > 1:
            return chr(ord(chars[letter]) + 1)
    #incase there is no skipped position
    return None
