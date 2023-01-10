class Quiz():
    def __init__(self, quiz_dict: dict, index: int):
        self.__QUIZ_DICT = quiz_dict
        self.__INDEX = index
    

    def get_index(self):
        return self.__INDEX
    

    def question(self):
        return self.__QUIZ_DICT["question"]

    def option1(self):
        if self.index:
            return "1. " + self.__QUIZ_DICT["options"][0]
        return self.__QUIZ_DICT["options"][0]

    def option2(self):
        if self.index:
            return "2. " + self.__QUIZ_DICT["options"][1]
        return self.__QUIZ_DICT["options"][1]

    
    def option3(self):
        if self.index:
            return "3. " + self.__QUIZ_DICT["options"][2]
        return self.__QUIZ_DICT["options"][2]

    def option4(self):
        if self.index:
            return "4. " + self.__QUIZ_DICT["options"][3]
        return self.__QUIZ_DICT["options"][3]


    def correct(self):
        return self.__QUIZ_DICT["correct_option"]

    def correct_answer(self):
        return self.__QUIZ_DICT["options"][int(self.correct())-1]
    


    