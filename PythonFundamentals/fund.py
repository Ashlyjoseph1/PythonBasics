# FE==> html,css,bootstrap,javascript
# BE==> python django,mysql,api[django rest frame works]
# vsc git and github

# coding standards

#  snake case (underscore)(python) (fn name,variable name)
#  camel case
#  pascal case (PersonDetails)(class name)
# def add (n1,n2):
#     return n1+n2
# def add (n1,n2,n3):
#     return n1+n2+n3
# def add (n1,n2,n3,n4):
#     return n1+n2+n3+n4
def add(*args):
    print(args)
add(18,5,4)


def add(*args):
    return sum(args)
print(add(10,12,1))


def print_details(*args):
    print(args[0])
    print(args[1])
    print(args[2])
print_details("hari","ekm","kakkanad")

def print_details(*args,**kwargs):
    print(kwargs)
print_details(name="hari",loc="ekm",workloc="kakkanad")
