class Mother(object):
    def say(self, *args, **kwargs):
       print("Im mother")

class Children(Mother):
    def say(self, *args, **kwargs):
       print("Im children")
       return super().say(*args, **kwargs)


if __name__  == "__main__":
    # Simple mother class
    objm = Mother()
    objm.say()

    # Children says and call mother says with super
    objc = Children()
    objc.say()

