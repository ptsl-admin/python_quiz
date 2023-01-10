import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import tkinter.font as tkFont
from functools import partial


class App(tk.Tk):
    def __init__(self, quiz_loader):
        super().__init__()
        self.title('THI QUIZ')
        self.geometry('700x500')
        self.resizable(0,0)

        # assign quiz loader instance to self        
        self.__quiz_loader = quiz_loader
        
        # load quiz from the text file
        self.__quiz_loader.load_quiz_from_text_file()

        # get random quiz
        self.__quiz = quiz = self.__quiz_loader.get_random_quiz(index = True)            

        # create widgets and assign quiz contents
        self.create_widgets(quiz)
        
    def create_widgets(self, quiz):
        # display header image
        self.header_image = tk.PhotoImage(file='./assets/quiz_logo.png')
        self.header_image_label = ttk.Label(self, image=self.header_image)

        self.header_image_label.grid(column = 0, row = 0, columnspan = 2)
        self.grid_columnconfigure(0,weight = 1) # horizontally align center
        self.grid_columnconfigure(1,weight = 1) # horizontally align center
        #self.grid_columnconfigure(2,weight = 1) # horizontally align center
        #self.grid_columnconfigure(3,weight = 1) # horizontally align center
        #self.grid_columnconfigure(4,weight = 1) # horizontally align center
        #self.grid_columnconfigure(5,weight = 1) # horizontally align center
        
        # create question label        
        self.question_label = ttk.Label(self, text=quiz.question(), font = "Arial 18 bold", borderwidth=5,relief="ridge",wraplength=680)        
        self.question_label.grid(column = 0, row = 1, columnspan = 2, pady = 30)
        self.grid_columnconfigure(1,weight = 1) # horizontally align center


        font = "Arial 12"
        # create option 1 button
        self.btn_option_1 = tk.Button(self, text =quiz.option1(), font = font, wraplength=300, command = partial(self.user_choice, 1))
        self.btn_option_1.grid(column = 0, row = 2, pady = 20)

        # create option 2 button
        self.btn_option_2 = tk.Button(self, text =quiz.option2(), font = font, wraplength=300, command = partial(self.user_choice, 2))
        self.btn_option_2.grid(column = 1, row = 2, pady = 20)

        # create option 3 button
        self.btn_option_3 = tk.Button(self, text =quiz.option3(), font = font, wraplength=300, command = partial(self.user_choice, 3))
        self.btn_option_3.grid(column = 0, row = 3, pady = 20)

        # create option 4 button
        self.btn_option_4 = tk.Button(self, text =quiz.option4(), font = font, wraplength=300, command = partial(self.user_choice, 4))
        self.btn_option_4.grid(column = 1, row = 3, pady=20)

    def render_quiz(self, quiz):
        self.question_label["text"] = quiz.question()
        self.btn_option_1["text"] = quiz.option1()
        self.btn_option_2["text"] = quiz.option2()
        self.btn_option_3["text"] = quiz.option3()
        self.btn_option_4["text"] = quiz.option4()
        
    def user_choice(self, a = 0):
        quiz = self.__quiz
        if quiz.correct() == a:
            msgbox.showinfo("Correct", "You have selected Correct option \n\n {0}".format(quiz.correct_answer()))

            ## at this point load next question
            
            self.load_next_quiz()
            
        else:
            msgbox.showerror("Wrong", "You have selected Wrong option. Correct answer is \n\n {0}".format(quiz.correct_answer()))



    def load_next_quiz(self):
        self.__quiz = quiz = self.__quiz_loader.get_random_quiz(index = True)

        self.render_quiz(quiz)
        
        

