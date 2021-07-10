'''
Loop tracing: show the values of each variable after each itteration

Be aware of copying and where variables are stored.

__str__ converts the object into a string when it gets printed

USE THIS DOCUMENT FOR TESTING

lambda a: a+10

for a string: "blah blah %s %s blah blah %s %s" %(s1, s2, s3, s4)

class classname(object):
    def __init__(self, object1, object2, object3):
        self.__object1 = object1
        self.__object2 = object2
        self.__object3 = object3

    def __str__(self):
        return (something in a string)

    def someFunction(self, someParameter):
        ---
        return ---

class subclass(classname):
    def __init__(self, object1, object2, object3, object4):
        super().__init__(object1, object2, object3)

    def someOtherFunction(self, someOtherParameter):
        ---
        return ---


'''

