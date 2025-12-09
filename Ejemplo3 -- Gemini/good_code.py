import threading
import logging
from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor

# Configuración de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Transaction:
    """Representa una transacción financiera inmutable."""
    user_id: int
    amount: Decimal
    type: str
    target_account: Optional[str] = None

class BankAccount:
    """
    Gestiona el estado de una cuenta bancaria de forma segura para hilos.
    Implementa el patrón Monitor para evitar condiciones de carrera.
    """
    def __init__(self, initial_balance: Decimal):
        self._balance = initial_balance
        self._lock = threading.Lock()

    @property
    def balance(self) -> Decimal:
        with self._lock:
            return self._balance

    def deposit(self, amount: Decimal) -> None:
        """Añade fondos de manera segura usando un bloqueo."""
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        
        with self._lock:
            self._balance += amount
            logger.info(f"Depósito: {amount}. Nuevo saldo: {self._balance}")

    def withdraw(self, amount: Decimal) -> bool:
        """
        Intenta retirar fondos de manera atómica.
        Returns: True si el retiro fue exitoso, False si no hay fondos.
        """
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")

        with self._lock:
            if self._balance >= amount:
                self._balance -= amount
                logger.info(f"Retiro: {amount}. Nuevo saldo: {self._balance}")
                return True
            
            logger.warning(f"Fondos insuficientes para retiro de {amount}")
            return False

class TransactionProcessor:
    """Servicio encargado de orquestar el procesamiento de transacciones en lote."""

    def __init__(self, account: BankAccount):
        self.account = account

    def process_transaction(self, tx: Transaction) -> None:
        """
        Procesa una única transacción aplicando la lógica de negocio.
        La complejidad ciclomática se mantiene baja delegando lógica.
        """
        try:
            if tx.type == 'DEPOSIT':
                self.account.deposit(tx.amount)
            elif tx.type == 'WITHDRAW':
                self._handle_withdrawal(tx)
            else:
                logger.error(f"Tipo de transacción desconocido: {tx.type}")
        except Exception as e:
            logger.error(f"Error procesando transacción {tx}: {e}")

    def _handle_withdrawal(self, tx: Transaction) -> None:
        """Lógica encapsulada para retiros."""
        success = self.account.withdraw(tx.amount)
        if not success:
            # Aquí se podría implementar lógica de reintento o notificación
            pass

    def process_batch(self, transactions: List[Transaction], max_workers: int = 4) -> None:
        """
        Procesa una lista de transacciones de forma concurrente.
        Utiliza ThreadPoolExecutor para una gestión eficiente de hilos.
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.process_transaction, transactions)

# Ejemplo de uso limpio y tipado
if __name__ == "__main__":
    cuenta_principal = BankAccount(initial_balance=Decimal("10000.00"))
    procesador = TransactionProcessor(cuenta_principal)
    
    lote_transacciones = [
        Transaction(user_id=1, amount=Decimal("500.00"), type='WITHDRAW'),
        Transaction(user_id=2, amount=Decimal("200.00"), type='DEPOSIT'),
        Transaction(user_id=1, amount=Decimal("99999.00"), type='WITHDRAW'), # Fallará controladamente
    ]
    
    procesador.process_batch(lote_transacciones)