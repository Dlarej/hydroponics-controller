
from enum import Enum

class State(Enum):
    OFF = 0
    ON = 1

class Component(object):
    def __init__(self):
        self.state = State.OFF
        print "hellooo"

class FanComponent(Component):
    def __init__(self):
        super(FanComponent, self).__init__()
