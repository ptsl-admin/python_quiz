""" assembling everything together """
from QuizLoader import *
from QuizData import *
from quiz_gui import *


if __name__ == "__main__":

    # get data with the help of Quizdata class
    quizs = QuizData.load_quiz_from_text_file()

    # initialize the quiz loader (logic class)
    loader = QuizLoader(quizs)

    # pass loader to to the App class which handles the GUI interface and events
    app = App(loader)
    
    # invoke main loop of the app object to get the  GUI interface
    app.mainloop()
