from Questions import Question


class Repo:
    def __init__(self, filename):
        self._filename = filename
        self._questions = []
        self.load_file()

    def load_file(self):
        file = open(self._filename, "r")
        lines = file.read()
        lines = lines.splitlines()
        for l in lines:
            values = l.split(';')
            question = Question(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
            self._questions.append(question)
        file.close()

    def save_file(self):
        lines=[]
        questions=self._questions
        file=open(self._filename,"w")
        for q in questions:
            lines.append(f"{q.get_id()};{q.get_text()};{q.get_choice_a()};{q.get_choice_b()};{q.get_choice_c()};{q.get_correct_choice()};{q.get_difficulty()}")

        for l in lines:
            file.write(l)
            file.write("\n")
        file.close()

    def get_all(self):
        return self._questions

    def search_id(self, id):
        ids = list(filter(lambda x: (x.get_id() == id), self._questions))
        if len(ids) == 1:
            return ids[0]
        else:
            return None

    def add(self,question):
        self._questions.append(question)
        self.save_file()
