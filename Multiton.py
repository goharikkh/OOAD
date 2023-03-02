class Multiton:
    instances = []
    max_instances = 5  # maximum number of instances allowed
    count = 0
    def __new__(cls, *args, **kwargs):
        if len(cls.instances) >= cls.max_instances:
            obj = cls.instances[cls.count]
            cls.count += 1
            return obj
        else:
            obj = super().__new__(cls)
            cls.instances.append(obj)
            return obj


obj1 = Multiton()
obj2 = Multiton()
obj3 = Multiton()
obj4 = Multiton()
obj5 = Multiton()
obj6 = Multiton()
obj7 = Multiton()
obj8 = Multiton()

print(obj6 is obj1)
print(obj7 is obj2)
print(obj8 is obj3)



