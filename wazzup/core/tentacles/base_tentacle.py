from abc import ABC, abstractmethod
from typing import Any, Generic, List, Dict, TypeVar
from datetime import datetime


T_content = TypeVar("T_content", bound=Dict[str, Any])

class BaseTentacle(Generic[T_content], ABC):
    
    
    
    
    @abstractmethod
    def authenticate(self, credentials: Dict[str, str]) -> None:
        """
        Authenticate the importer with the given credentials.
        """
        pass

    @abstractmethod
    def fetch_data(
        self,
        user_id: int,
        platform_id: int,
        channel_id: int,
        start_time: datetime,
        end_time: datetime,
    ) -> List[Dict[str, Any]]:
        """
        Fetch data from the platform for the given user, platform, channel, and time range.
        Returns a list of dictionaries representing the fetched data.
        """
        pass
    
    listeners: list =[]
    
    @abstractmethod
    def on_message(self, message: T_Message) -> None:
        """
        Called when a message is received.
        """
        pass
    
    @abstractmethod
    def start_listening(self, user_id: int, platform_id: int, channel_id: int) -> None:
        """
        Listen for changes in the platform for the given user and channel.
        """
        pass
    
    @abstractmethod
    def stop_listening(self, user_id: int, platform_id: int, channel_id: int) -> None:
        """
        Stop listening for changes in the platform for the given user and channel.
        """
        pass

    @