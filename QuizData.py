import json


class QuizData():
    @staticmethod
    def load_quiz_json_file():        
        #  we assume that there is quiz.json file inside assets folder
        try:
            with open('assets/quiz_functions.json', 'rt') as quiz_file:
                #print(json.dumps(self.__QUIZ, indent=2))
                return json.load(quiz_file)                            
        except FileNotFoundError:
            return []
    

    @staticmethod
    def load_quiz_from_text_file():
        QUIZS = []  # contains individual dictionary of quizes
        try:
            with open('assets/quiz_functions.txt', 'rt') as quiz_file:
                total_questions = quiz_file.readline().strip()
                #__QUIZ_COUNT = int(total_questions)
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
                    QUIZS.append(
                        {
                            "question": question,
                            "options": options,
                            "correct_option": correct_option
                        }
                    )

            print(json.dumps(QUIZS, indent=4))
            return QUIZS
        except FileNotFoundError:
            return []


print(len(QuizData.load_quiz_from_text_file()))