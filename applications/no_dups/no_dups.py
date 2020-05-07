def no_dups(s):
    if s == "":
        return ""

    word_arr = s.split()

    seen = {}
    output = ""

    for i in word_arr:
        try:
            test = seen[i]
        except KeyError:
            output += i + " "
            seen[i] =  1
    output = output.rstrip()
    
    return output
    # split
    # loop through
    # add to dictionary
    # if in dictionary don't add to list
    # else add to list
    # Implement me.


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))