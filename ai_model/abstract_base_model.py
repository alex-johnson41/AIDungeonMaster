from abc import ABC, abstractmethod


class AbstractBaseModel(ABC):

    @abstractmethod
    def communicate(self, prompt: str) -> str:
        pass