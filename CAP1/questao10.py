class Student:
    def __init__(self, name, number_of_scores):
        self.name = name
        self.scores = [0] * number_of_scores

    def get_score(self, position):
        return self.scores[position]

    def set_score(self, position, score):
        self.scores[position] = score

    def get_number_of_scores(self):
        return len(self.scores)

    def get_highest_score(self):
        return max(self.scores)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def get_name(self):
        return self.name

    def __str__(self):
        result = f"Name: {self.name}\n"

        for i in range(len(self.scores)):
            result += f"Score {i + 1}: {self.scores[i]}\n"

        return result


def tester():
    name = input("Digite o nome do estudante: ")
    number_of_scores = int(input("Digite a quantidade de notas: "))

    student = Student(name, number_of_scores)

    for i in range(number_of_scores):
        score = float(input(f"Digite a nota {i + 1}: "))
        student.set_score(i, score)

    print("\n--- Informações do estudante ---")
    print(student)

    print(f"Maior nota: {student.get_highest_score()}")
    print(f"Média: {student.get_average_score():.2f}")
    print(f"Quantidade de notas: {student.get_number_of_scores()}")


if __name__ == "__main__":
    tester()