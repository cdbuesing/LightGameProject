from tkinter import *
import logic


class GUI:
    def __init__(self, window):
        self.window = window

        ## Frame to hold pages
        self.container = Frame(self.window)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        ## empty list to hold pages
        self.frames = list()

        ## Start Page
        self.frame_start = Frame(self.container)
        self.label_start = Label(self.frame_start, text='WELCOME\nTo The Light Game')
        self.label_name = Label(self.frame_start, text='Enter Your Name')
        self.input_name = Entry(self.frame_start)
        self.button_instructions = Button(self.frame_start, text='INSTRUCTIONS', command=lambda: logic.show_frame(self,1))
        self.button_board = Button(self.frame_start, text='LEADERBOARD', command=lambda: logic.show_frame(self,2))
        self.button_start = Button(self.frame_start, text='START', command= lambda: logic.show_frame(self,3))
        self.label_start.pack(expand= True)
        self.label_name.pack()
        self.input_name.pack()
        self.button_instructions.pack(expand= True)
        self.button_board.pack(expand= True)
        self.button_start.pack(expand= True)
        self.frames.append(self.frame_start)
        self.frame_start.grid(row = 0, column = 0, sticky = NSEW)

        ## Instructions Page
        self.frame_instructions = Frame(self.container)
        self.label_instructions = Label(self.frame_instructions, text='This is the Light Game\nWhen You Click a Square,\nIt\'s Status and The Status Of All Squares Directing Touching it Will Switch\nFrom Either On to Off or Off to On\nYour Goal is to Make the Entire Grid On, Which is Represented By Blue\nGood Luck!')
        self.button_back_two = Button(self.frame_instructions, text='BACK', command=lambda: logic.show_frame(self,0))
        self.label_instructions.pack()
        self.button_back_two.pack(side="bottom")
        self.frames.append(self.frame_instructions)
        self.frame_instructions.grid(row=0, column=0, sticky=NSEW)

        ## Leaderboard Page
        self.frame_board = Frame(self.container)
        self.label_leaderboard = Label(self.frame_board, text='N/A')
        self.button_back = Button(self.frame_board, text='BACK', command=lambda: logic.show_frame(self, 0))
        self.label_leaderboard.pack()
        self.button_back.pack(side="bottom")
        self.frames.append(self.frame_board)
        self.frame_board.grid(row=0, column=0, sticky=NSEW)

        ## Game Page
        self.frame_game = Frame(self.container)
        self.frame_grid = Frame(self.frame_game)
        self.label_timer = Label(self.frame_game, text = '0 seconds')
        self.game_matrix = list()
        self.logic_matrix = list()
        for r in range(5):
            self.game_matrix.append(list())
            self.logic_matrix.append(list())
            for c in range(5):
                tup = (r,c)
                self.game_matrix[r].append(Button(self.frame_grid, bg="blue", command= lambda temp=tup: logic.click(self,temp[0],temp[1])))
                del tup
                self.logic_matrix[r].append(1)
                self.frame_grid.grid_rowconfigure(r, weight=1)
                self.frame_grid.grid_columnconfigure(c, weight=1)
                self.game_matrix[r][c].grid(row=r, column=c, sticky=NSEW)
        self.frame_grid.pack(side="top", fill = "both", expand = True)
        self.label_timer.pack(side="bottom", fill = "both")
        self.frames.append(self.frame_game)
        self.frame_game.grid(row=0, column=0, sticky=NSEW)

        ## End Page
        self.frame_end = Frame(self.container)
        self.label_end = Label(self.frame_end, text=f'Thanks For Playing!')
        self.label_score = Label(self.frame_end, text='')
        self.button_return = Button(self.frame_end, text='Return To Start', command=lambda: logic.show_frame(self,0))
        self.label_end.pack(expand= True)
        self.label_score.pack(expand= True)
        self.button_return.pack(side="bottom")
        self.frames.append(self.frame_end)
        self.frame_end.grid(row=0, column=0, sticky=NSEW)

        logic.show_frame(self,0)

    def clearName(self):
        """
        Clears the input box for the name

        Returns:
            nothing
        """
        self.input_name.delete(0, END)

    def setName(self, name):
        """
        Sets the player_name variable to whatever is input for the name parameter

        Args:
            name (str): string for the players name

        Returns:
            nothing
        """
        self.player_name = name

    def getInput(self):
        """
        Returns:
            a string of the current text in the entry box input_name
        """
        return self.input_name.get()

    def getName(self):
        """
        Returns:
            the variable player_name
        """
        return self.player_name

    def getFrame(self, index):
        """
        Args:
            index (int): the index for the desired frame in the list frames

        Returns:
            the frame in frames at the input index
        """
        return self.frames[index]

    def getLogicMatrix(self, r, c):
        """
        Args:
            r (int): the row index in logic_matrix for the desired int
            c (int): the column index in logic_matrix for the desired int

        Returns:
            the int in logic_matrix at the row and column indexes provided
        """
        return self.logic_matrix[r][c]

    def setLogicMatrix(self, r, c, value):
        """
        Sets the int stored at the row and column indexes in logic_matrix to value

        Args:
            r (int): the row index in logic_matrix for the desired int
            c (int): the column index in logic_matrix for the desired int
            value (int): the desired value to set the int at the row and column indexes to

        Returns:
            nothing
        """
        self.logic_matrix[r][c] = value

    def setGameMatrix(self, r, c, color):
        """
        Sets the background color of the button at the row and column indexes in game_matrix to color

        Args:
            r (int): the row index in game_matrix for the desired button
            c (int): the column index in game_matrix for the desired button
            color (str): the string for the desired color to set the buttons background color to

        Returns:
            nothing
        """
        self.game_matrix[r][c].config(bg=color)

    def updateWindow(self):
        """
        Causes the window to update

        Returns:
            nothing
        """
        self.window.update()

    def updateScoreLabel(self, message):
        """
        Sets the text in the Label label_score to message

        Args:
            message (str): the message desired to set the text of label_score to

        Returns:
            nothing
        """
        self.label_score.config(text=message)

    def updateLeaderboard(self, message):
        """
        Updates the text of the Label label_leaderboard to message

        Args:
            message (str): the message desired to set the text of label_leaderboard to

        Returns:
            nothing
        """
        self.label_leaderboard.config(text=message)

    def updateTimer(self, time):
        """
        Sets the text in the Label label_timer to time

        Args:
            time (str): the message of the current time in seconds since the start of the game

        Returns:
                nothing
        """
        self.label_timer.config(text=time)