class classclass(object):
    """docstring for classclass."""

    var_for_all_classes = "string"


    def __init__(self, arg):
        super(classclass, self).__init__()
        self.var_for_specific_instance = arg
        self.listname = []

    def add_to_list(self, arg):
        self.listname.append(arg)

x = classclass(99999999)
x.add_to_list("thats a number")
x.add_to_list("this is a list")
x.add_to_list("spanish class is the best place for coding")
y = classclass("this is another instance")
y.add_to_list("this is another list for another instance")
y.add_to_list("cool, huh?")
print(x.var_for_specific_instance)
print(x.listname)
print(y.var_for_specific_instance)
print(y.listname)
