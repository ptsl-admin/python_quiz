import json
import random


class QuizLoader:
    """ The quiz loader class is actually the logic class, it handles all the actions in
        coordination with the GUI class
    """
    __QUIZ = []
    __LAST_QUIZ_ID = -1

    def __init__(self, QUIZ: list):
        """ Quiz loader constructor """
        self.__QUIZ = QUIZ
     

    def get_random_quiz(self, index = False):
        """ form the list of quizs get a random one """
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
        """ ge the total questions form the pulled data"""
        return len(self.__QUIZ)

    class Quiz:
        """ The Quiz Class. returns all the quiz items individually """

        def __init__(self, quiz_dict, index):

            """ initialize with quiz dict and assign to self  """
            #if isinstance(quiz_dict, dict):
            self.index: int = index
            self.__quiz_dict: dict = quiz_dict

        def question(self):
            """ get the question item of the quiz """
            return self.__quiz_dict["question"]

        def option1(self):
            """ get option item 1 """
            if self.index:
                return "1. " + self.__quiz_dict["options"][0]
            return self.__quiz_dict["options"][0]

        def option2(self):
            """ get option item 2 """
            if self.index:
                return "2. " + self.__quiz_dict["options"][1]
            return self.__quiz_dict["options"][1]

        
        def option3(self):
            """ get option item 3 """
            if self.index:
                return "3. " + self.__quiz_dict["options"][2]
            return self.__quiz_dict["options"][2]

        def option4(self):
            """ get option item 4 """
            if self.index:
                return "4. " + self.__quiz_dict["options"][3]
            return self.__quiz_dict["options"][3]


        def correct(self)->int:
            """ get the correct option index 1, 2, 3, 4"""
            return self.__quiz_dict["correct_option"]

        def correct_answer(self):
            """ get the correct answer, not the index but the item itself """
            return self.__quiz_dict["options"][int(self.correct())-1]

        
        def is_correct_option(self, correct_index: int)-> bool:
            """_summary_"""
            
            if self.correct() == correct_index:
                return True
            return False









