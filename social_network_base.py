from abc import ABC, abstractmethod


class SocialNetworkBase(ABC):
    @abstractmethod
    def authenticate(self):
        raise NotImplementedError()

    @abstractmethod
    def get_feed(self):
        raise NotImplementedError()

    @abstractmethod
    def create_post(self):
        raise NotImplementedError()

    @abstractmethod
    def get_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def like_add(self):
        raise NotImplementedError()

    @abstractmethod
    def like_delete(self):
        raise NotImplementedError()
