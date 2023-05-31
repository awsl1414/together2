class Msg(object):
    def __init__(self, name) -> None:
        self.name = name

    def msg(self):
        return {"msg": self.name}
