import random

from Questions import  Question
class Service:
    def __init__(self, repo):
        self.__repo = repo
        self.points = 0

    def get_all_questions(self):
        return self.__repo.get_all()

    def add(self, question):
        self.__repo.add(question)

    def get_number_of_questions(self):
        questions=self.__repo.get_all()
        easyn=0
        mediumn=0
        hardn=0
        for q in questions:
            if q.get_difficulty()=='easy':
                easyn+=1
            elif q.get_difficulty()=='medium':
                mediumn+=1
            elif q.get_difficulty()=='hard':
                hardn+=1

        number=[easyn,mediumn,hardn]
        return number

    def create(self,difficulty,number,file):
        questions=self.__repo.get_all()
        easyq=list(filter(lambda x:(x.get_difficulty()=='easy'),questions))
        mediumq=list(filter(lambda x:(x.get_difficulty()=='medium'),questions))
        hardq=list(filter(lambda x:(x.get_difficulty()=='hard'),questions))
        easyq=random.shuffle(easyq)
        mediumq=list(random.shuffle(mediumq))
        hardq=list(random.shuffle(hardq))
        file=open(file,"w")
        lines=[]
        count=0
        if difficulty=='easy':
            for q in easyq:
                count+=1

                lines.append(f"{q.get_id()};{q.get_text()};{q.get_choice_a()};{q.get_choice_b()};{q.get_choice_c()};{q.get_correct_choice()};{q.get_difficulty()}")
                if count==int(number/2):
                    break
        elif difficulty=='medium':
            for i in range(int(number / 2)):
                q = random.choice(mediumq)
                for l in mediumq:
                    if l == q:
                        del(l)
                lines.append(
                    f"{q.get_id()};{q.get_text()};{q.get_choice_a()};{q.get_choice_b()};{q.get_choice_c()};{q.get_correct_choice()};{q.get_difficulty()}")
        elif difficulty=='hard':
            for i in range(int(number / 2)):
                q = random.choice(hardq)
                for l in hardq:
                    if l == q:
                        del(l)
                lines.append(
                    f"{q.get_id()};{q.get_text()};{q.get_choice_a()};{q.get_choice_b()};{q.get_choice_c()};{q.get_correct_choice()};{q.get_difficulty()}")

        for l in lines:
            file.write(l)
            file.write("\n")
        file.close()


    def search_id(self, id):
        verify = self.__repo.search_id(id)
        return verify
