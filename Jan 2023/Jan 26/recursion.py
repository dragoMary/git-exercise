
def hello(hollywood_star):
    if hollywood_star == '':
        pass   #stop my func in some condition Base case
    else:
        hollywood_star = hollywood_star[1:]
        print(hollywood_star)
        hello(hollywood_star)
hello('hollywood_star')