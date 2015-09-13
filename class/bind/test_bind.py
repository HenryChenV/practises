class Human(object):
    def __init__(self, addr, name):
        print 'I am a Human.'
        self.addr = addr
        self.name = name

    def get_name(self):
        return self.name


class Female(Human):
    def __init__(self, addr, name, breast, waist, hip):
        print 'I am a Female.'
        Human.__init__(self, addr, name)
        self.breast = breast
        self.waist = waist
        self.hip = hip


f = Female('shanghai', 'henry', 0, 0, 0)
print Human.get_name(f)
