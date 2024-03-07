from Questions import Question


class Ui:
    def __init__(self, service):
        self.__service = service

    def help(self):
        print(
            "Add a question to the master question list:'add <id> <text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty> ")
        print("Create a quiz in a file:create <difficulty> <number_of_questions> <file>")

    def run(self):
        print("Enter 'help' for instructions!")
        while True:
            option = input("Your option:")
            option = option.split(' ', 1)
            if len(option) == 1:
                if option[0] == 'help':
                    self.help()
            elif len(option) == 2:

                if option[0] == 'add':
                    values = option[1].split(';')
                    if len(values) == 7:
                        try:
                            self.add(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
                        except ValueError as ve:
                            print(ve)

                if option[0] == 'create':
                    values = option[1].split(' ')
                    if len(values) == 3:
                        try:
                            self.create(values[0], int(values[1]), values[2])
                        except ValueError as ve:
                            print(ve)

    def add(self, id, text, choice_a, choice_b, choice_c, correct, difficulty):
        verify = self.__service.search_id(id)
        if verify != None:
            raise ValueError("This id already exists!")
        if choice_c == choice_b and choice_a == choice_b:
            raise ValueError("The choices can't be the same!")
        if correct != choice_a and correct != choice_b and correct != choice_c:
            raise ValueError("The correct answear is not in the choices!")
        if difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
            raise ValueError("The difficulty is invalid!")
        quesion = Question(id, text, choice_a, choice_b, choice_c, correct, difficulty)
        self.__service.add(quesion)

    def create(self, difficulty, number, file):
        if difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
            raise ValueError("Invalid difficulty!")
        if number < 1:
            raise ValueError("Your quiz does not contain questions!")
        total = self.__service.get_number_of_questions()
        if difficulty == 'easy' and total[0] < number / 2:
            raise ValueError("There are not enough easy questions!")
        if difficulty == "medium" and total[1] < number / 2:
            raise ValueError("There are not enough medium questions!")
        if difficulty=='hard' and total[2]<number/2:
            raise ValueError("There are not enough hard questions!")
        self.__service.create(difficulty,number,file)

