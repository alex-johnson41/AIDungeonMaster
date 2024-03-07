from abc import ABC, abstractmethod


class AbstractAIModel(ABC):

    @abstractmethod
    def communicate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass