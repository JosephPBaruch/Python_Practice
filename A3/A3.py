sample = "This is a sample text. Sample text is a good example as It showcases how to count words in a text string."

#print(sample)

my_list = []
my_dict = {}


def make_dict(text):
    list = text.split(' ')
    for i in range(len(list)):
        list[i] = list[i].lower()
        #print(list[i])
        if '.' in list[i]:
            list[i] = list[i].replace('.','')
        if dict.get(list[i]):
            dict[list[i]] += 1
        else:
            dict[list[i]] = 1
    return dict

dict = make_dict(sample)

keys = list(dict.keys())