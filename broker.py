class BrokerMeta(type):
    """A broker metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'get_position') and 
                callable(subclass.get_position) and 
                hasattr(subclass, 'place_order') and 
                callable(subclass.place_order))

class BrokerSuper:
    """A broker superclass"""
    def get_position(self) -> str:
        print("parent broker position")

    def place_order(self) -> int:
        pass

class FuturesBroker(metaclass=BrokerMeta):
    """broker interface built from brokerMeta metaclass."""
    pass
