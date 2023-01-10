from QuizLoader import *
from quiz_gui import *


if __name__ == "__main__":

    loader = QuizLoader()

    
    app = App(loader)
    
    app.mainloop()
