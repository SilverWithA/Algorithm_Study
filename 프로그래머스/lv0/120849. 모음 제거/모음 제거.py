def solution(my_string):
    sub_string = ["a", "e", "i", "o", "u"]
    

    for i in sub_string:
        my_string = my_string.replace(i,"")
    return my_string         