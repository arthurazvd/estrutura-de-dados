class Counter(object):
    """Modela um contador."""

    # Variável de classe
    instances = 0

    # Construtor
    def __init__(self):
        """Configura o contador."""
        Counter.instances += 1
        self.reset()

    # Métodos mutator
    def reset(self):
        """Define o contador como 0."""
        self.value = 0

    def increment(self, amount=1):
        """Adiciona amount ao contador."""
        self.value += amount

    def decrement(self, amount=1):
        """Subtrai amount do contador."""
        self.value -= amount

    # Métodos accessor
    def getValue(self):
        """Retorna o valor do contador."""
        return self.value

    def __str__(self):
        """Retorna a representação de string do contador."""
        return str(self.value)

    def __eq__(self, other):
        """Retorna True se self é igual a other, ou False caso contrário."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.value == other.value