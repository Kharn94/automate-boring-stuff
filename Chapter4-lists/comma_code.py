spam = ['apples', 'bananas', 'tofu', 'cats']
spam_empty = []

def comma(any_list):
    if any_list == []:
        pass
    else:
        o_string = ''
        for i in range(len(any_list)-1):
            o_string = any_list[i] + ' ' + o_string
        o_string = o_string + 'and ' + any_list[-1]
        print(o_string)


comma(spam)
comma(spam_empty)
