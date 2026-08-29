class Student(object):
    """Modela um aluno com nome e notas de teste."""
    
    def __init__(self, name, num_scores=3):
        """Inicializa o aluno com nome e um número de notas (padrão 3)."""
        self.name = name
        self.scores = [0] * num_scores
    
    def getName(self):
        """Retorna o nome do aluno."""
        return self.name
    
    def getScore(self, index):
        """Retorna a nota na posição especificada."""
        if 0 <= index < len(self.scores):
            return self.scores[index]
        return None
    
    def setScore(self, index, value):
        """Define a nota na posição especificada."""
        if 0 <= index < len(self.scores):
            self.scores[index] = value
    
    def getNumberOfScores(self):
        """Retorna o número de notas."""
        return len(self.scores)
    
    def getHighestScore(self):
        """Retorna a nota mais alta."""
        if self.scores:
            return max(self.scores)
        return 0
    
    def getAverageScore(self):
        """Retorna a média das notas."""
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0
    
    def __str__(self):
        """Retorna a representação em string do aluno."""
        result = f"Name: {self.name}\n"
        for i, score in enumerate(self.scores, 1):
            result += f"Score {i}: {score}\n"
        return result

# Função de teste
def test_student():
    student = Student("Ken Lambert", 3)
    student.setScore(0, 88)
    student.setScore(1, 77)
    student.setScore(2, 100)
    print(student)
    print(f"Highest Score: {student.getHighestScore()}")
    print(f"Average Score: {student.getAverageScore():.2f}")

if __name__ == "__main__":
    test_student()