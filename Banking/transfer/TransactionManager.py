from abc import ABC, abstractmethod
class TransactionManager(ABC):
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...

    
    @abstractmethod
    def show_transaction_history(self) -> None:
        ...


    