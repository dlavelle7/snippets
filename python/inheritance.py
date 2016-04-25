"""Example of inheritance and the use of super()"""


class Super(object):

    def __init__(self, value):
        self.value = value

    def do(self):
        print "Super has {0}!".format(self.value)


class SubA(Super):
    pass


class SubB(Super):

    def __init__(self, value, unique_value):
        super(SubB, self).__init__(value)
        self.unique_value = unique_value

    def do(self):
        super(SubB, self).do()
        print "SubB also has {0}!".format(self.unique_value)


sub_a = SubA('foo')
sub_a.do()

sub_b = SubB('spam', 'eggs')
sub_b.do()
