from enum import Enum
import ConfigParser
from exceptions import *
import abc
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
        self.connect()
        self.on()

    def disconnect(self):
        self._disconnect()
        self.state = State.DISCONNECTED

    def connect(self):
        self._connect()
        self.state = State.CONNECTED

    def off(self):
        self._off()
        self.state = State.OFF

    def on(self):
        self._on()
        self.state = State.ON

    @abc.abstractmethod
    def _disconnect(self):
        return

    @abc.abstractmethod
    def _connect(self):
        return

    @abc.abstractmethod
    def _off(self):
        return

    @abc.abstractmethod
    def _on(self):
        return

    @abc.abstractmethod
    def _get_status(self):
        return

class FanComponent(Component):
    def __init__(self):
        super(FanComponent, self).__init__()

    def _disconnect(self):
        print "disconnecting fan"

    def _connect(self):
        print "connecting fan"

    def _off(self):
        print "fan off"

    def _on(self):
        print "fan on"

    def _get_status(self):
        print "getting status"

class DehumidifierComponent(Component):
    def __init__(self):
        super(DehumidifierComponent, self).__init__()

    def _disconnect(self):
        print "disconnecting dehumidifier"

    def _connect(self):
        print "connecting dehumidifier"

    def _off(self):
        print "dehumidifier off"

    def _on(self):
        print "dehumidifier on"

    def _get_status(self):
        print "getting status of dehumidifier"


class TemperatureComponent(Component):
    def __init__(self):
        super(TemperatureComponent, self).__init__()

    def _disconnect(self):
        print "disconnecting temperature"

    def _connect(self):
        print "connecting temperature"

    def _off(self):
        print "temperature off"

    def _on(self):
        print "temperature on"

    def _get_status(self):
        print "getting status of temperature"

class LightComponent(Component):
    def __init__(self):
        super(LightComponent, self).__init__()

    def _disconnect(self):
        print "disconnecting light"

    def _connect(self):
        print "connecting light"

    def _off(self):
        print "light off"

    def _on(self):
        print "light on"

    def _get_status(self):
        print "getting status of light"

fan = FanComponent() 
light = LightComponent() 
temperature = TemperatureComponent() 
dehumid = DehumidifierComponent() 
