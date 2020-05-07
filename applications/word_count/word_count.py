import string

def word_count(s):
    # split by word
    my_list = s.split()

    remove = """ " : ; , . - + = / \ | [ ] { } ( ) * ^ & """
    
    output = {}
    for i in my_list:
        temp = ""
        for j in i:
            if j in remove:
                continue
            else:
                temp += j
        temp = temp.lower()
        if temp:
            try:
                output[temp] += 1
            except KeyError:
                output[temp] = 1
    

    return output

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))