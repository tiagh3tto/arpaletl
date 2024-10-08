from sqlalchemy import Engine
from abc import ABC, abstractmethod


class IDbClient(ABC):
    """
    Interface for database client
    """
    

    engine: Engine


    @abstractmethod
    def __init__(self):
        """
        Constructor for IDbClient
        """


    @abstractmethod
    def __del__(self):
        """
        Destructor for IDbClient
        """


    def get_engine(self) -> Engine:
        """
        Return engine
        """
        return self.engine

