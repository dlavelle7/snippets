
def scope_test():

    def do_local():
        spam = "local"  # scope only last for life of function call

    def do_nonlocal():
        nonlocal spam  # refers to spam in scope_test()'s scope
        spam = "non local"  # resassigns spam in scope_test()'s scope

    def do_global():
        global spam  # defines spam in module level scope
        spam = "global"

    spam = "scope_test scope"

    do_local()
    print(spam)

    do_nonlocal()
    print(spam)

    do_global()
    print(spam)  # references nearest scope which is still scope_test()'s scope


scope_test()
print(spam)  # spam not required to be previously assigned, now in module scope
