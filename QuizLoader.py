import json
import random


class QuizLoader:
    __QUIZ = []
    __QUIZ_COUNT = 0
    __LAST_QUIZ_ID = -1

    def __init__(self):
        pass

    def load_quiz_json_file(self):
        #  we assume that there is quiz.json file inside assets folder
        try:
            with open('assets/quiz_functions.json', 'rt') as quiz_file:
                self.__QUIZ = json.load(quiz_file)
                # print(json.dumps(self.__QUIZ, indent=2))
                return True
        except FileNotFoundError:
            return False

    def load_quiz_from_text_file(self):
        try:
            with open('assets/quiz_functions.txt', 'rt') as quiz_file:
                total_questions = quiz_file.readline().strip()
                self.__QUIZ_COUNT = int(total_questions)
                for line in quiz_file:
                    question = line.strip()
                    option1 = quiz_file.readline().strip()
                    if option1.find("CORRECT:") != -1:
                        correct_option = 1
                        option1 = option1.replace("CORRECT:", "")
                    option2 = quiz_file.readline().strip()
                    if option2.find("CORRECT:") != -1:
                        correct_option = 2
                        option2 = option2.replace("CORRECT:", "")
                    option3 = quiz_file.readline().strip()
                    if option3.find("CORRECT:") != -1:
                        correct_option = 3
                        option3 = option3.replace("CORRECT:", "")
                    option4 = quiz_file.readline().strip()
                    if option4.find("CORRECT:") != -1:
                        correct_option = 4
                        option4 = option4.replace("CORRECT:", "")

                    options = [option1, option2, option3, option4]

                    # append each question as dictionary to the __QUIZ list
                    self.__QUIZ.append(
                        {
                            "question": question,
                            "options": options,
                            "correct_option": correct_option
                        }
                    )

            #print(json.dumps(self.__QUIZ, indent=4))
            return True
        except FileNotFoundError:
            return False

    def get_random_quiz(self, index = False):
        if len(self.__QUIZ) == 0:
            return None
        
        ### current quiz and last quiz should not be the same
        
        CURRENT_QUIZ_ID = random.randint(0, len(self.__QUIZ) - 1)
        while self.__LAST_QUIZ_ID == CURRENT_QUIZ_ID:
            CURRENT_QUIZ_ID = random.randint(0, len(self.__QUIZ) - 1)                    

        ## update last quiz id
        self.__LAST_QUIZ_ID = CURRENT_QUIZ_ID

        # get the quiz with respective id
        quiz = QuizLoader.Quiz(self.__QUIZ[CURRENT_QUIZ_ID], index)
        
        return quiz

    def get_total_question(self):
        return len(self.__QUIZ)

    class Quiz:

        def __init__(self, quiz_dict, index):
            #if isinstance(quiz_dict, dict):
            self.index = index
            self.__QUIZ_DICT = quiz_dict

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










