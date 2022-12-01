# input - string = "abracadabra"
# output - abrackdabra

def replace(position,string,character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    print(string)
replace(5,"abracadabra",'k')
