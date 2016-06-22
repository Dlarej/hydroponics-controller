from enum import Enum
import ConfigParser
from exceptions import *
from abc import ABCMeta, abstractmethod

class State(Enum):
    DISCONNECTED = -2
    CONNECTED = -1
    OFF = 0
    ON = 1

class Component(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        # Initialization behavior for all devices:
        # Attempt to connect and turn on

    def disconnect(self):
        self.__disconnect()
        self.state = State.DISCONNECTED

    def connect(self):
        self.__connect()
        self.state = State.CONNECTED

    def off(self):
        self.__off()
        self.state = State.OFF

    def on(self):
        self.__on()
        self.state = State.ON

    @abc.abstractmethod
    def __disconnect(self):
        return

    @abc.abstractmethod
    def __connect(self):
        return

    @abc.abstractmethod
    def __off(self):
        return

    @abc.abstractmethod
    def __on(self):
        return

    @abc.abstractmethod
    def __get_status(self):
        return

class FanComponent(Component):
    def __init__(self):
        super(FanComponent, self).__init__()

class DehumidifierComponent(Component):
    def __init__(self):
        super(DehumidifierComponent, self).__init__()

class TemperatureComponent(Component):
    def __init__(self):
        super(TemperatureComponent, self).__init__()
        # Temperature in Farenheit

class LightComponent(Component):
    def __init__(self):
        super(LightComponent, self).__init__()

