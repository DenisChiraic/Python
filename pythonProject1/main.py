from functools import reduce
def ub1(subject: str):
    with open("text.txt", "r") as file:
        l = file.read().split('\n')
        neue_list = list(map(lambda el: el.split(','), l))
        print(neue_list)
        sub_list = list(filter(lambda el: el[2] == subject, neue_list))
        print(sub_list)
        noten = reduce(lambda x,y: x + int(y[3]), sub_list, 0) / len(sub_list)
        return round(noten, 2)

def test_ub1():
    assert ub1("Advanced programming") == 8.17
    assert ub1("Advanced programming") == 8


# test_ub1()
x = ub1("Advanced programming")
print(x)