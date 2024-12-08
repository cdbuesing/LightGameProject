import random
import time
import threading

start_time = 0
elapsed_time = 0
initiated = False

def show_frame(self, index):
    """
    Changes the current page to the page matching the provided index

    Args:
        index (int): The index of the page in frames

    Returns:
        nothing
    """
    frame = self.getFrame(index)
    frame.tkraise()
    if(index == 2):
       update_leaderboard(self)
    elif(index == 3):
        self.setName(self.getInput())
        self.setName(self.getName().strip())
        if (self.getName() == ''):
            self.setName('Anonymous')
        self.clearName()
        reset(self)
        initiate(self)
    elif(index == 4):
        stop_event.set()



def click(self, r, c):
    """
    Changes the status of the button clicked and the buttons directly touching the clicked button from what they are to the opposite
    Then calls the check_win() function

    Args:
        r (int): row index in the matrix of the box clicked
        c (int): column index in the matrix of the box clicked

    Returns:
        nothing
    """
    if (self.getLogicMatrix(r,c) == 0):
        self.setLogicMatrix(r,c,1)
        self.setGameMatrix(r,c,"blue")
    else:
        self.setLogicMatrix(r,c,0)
        self.setGameMatrix(r,c,"white")
    if (r != 0):
        if (self.getLogicMatrix(r-1,c) == 0):
            self.setLogicMatrix(r-1,c,1)
            self.setGameMatrix(r-1,c,"blue")
        else:
            self.setLogicMatrix(r-1,c,0)
            self.setGameMatrix(r-1,c,"white")
    if (r != 4):
        if (self.getLogicMatrix(r+1,c) == 0):
            self.setLogicMatrix(r+1,c,1)
            self.setGameMatrix(r+1,c,"blue")
        else:
            self.setLogicMatrix(r+1,c,0)
            self.setGameMatrix(r+1,c,"white")
    if (c != 0):
        if (self.getLogicMatrix(r,c-1) == 0):
            self.setLogicMatrix(r, c-1, 1)
            self.setGameMatrix(r,c-1,"blue")
        else:
            self.setLogicMatrix(r,c-1,0)
            self.setGameMatrix(r,c-1,"white")
    if (c != 4):
        if (self.getLogicMatrix(r,c+1) == 0):
            self.setLogicMatrix(r,c+1,1)
            self.setGameMatrix(r,c+1,"blue")
        else:
            self.setLogicMatrix(r,c+1,0)
            self.setGameMatrix(r, c + 1, "white")
    global initiated
    if (initiated):
        check_win(self)


def check_win(self):
    """
    Checks if the win condition has been met. If it has, calls the win() function

    Returns:
        nothing
    """
    for r in range(5):
        for c in range(5):
            if (self.getLogicMatrix(r,c) == 0):
                return
    win(self)


def win(self):
    """
    Ends the game and calculates score. Changes the page to the end page.
    Finds where to place the new score in the leaderboard, and then rewrites the new leaderboard

    Returns:
        nothing
    """
    self.updateScoreLabel(f'You Beat the Game in {elapsed_time} seconds!')
    show_frame(self,4)
    if (board_check() == False):
        boardfile = open('leaderboard.txt', 'w', newline='')
        boardfile.write(f'1: {self.getName()}: {elapsed_time} seconds\n')
        boardfile.close()
    else:
        boardfile = open('leaderboard.txt', 'r')
        board_lines = boardfile.read()
        board_lines = board_lines.split('\n')
        board_lines.pop()
        for i in range(len(board_lines)):
            temp = len(str(i+1)) -1
            board_lines[i] = board_lines[i][(3+temp):]
        inserted = False
        for i in range(len(board_lines)):
            cur_line = board_lines[i].split(' ')
            if (elapsed_time < float(cur_line[1])):
                board_lines.insert(i, f'{self.getName()}: {elapsed_time} seconds')
                inserted = True
                break
        if (inserted == False):
            board_lines.append(f'{self.getName()}: {elapsed_time} seconds')
        boardfile.close()
        boardfile = open('leaderboard.txt', 'w', newline='')
        for i in range(len(board_lines)):
            boardfile.write(f'{i + 1}: {board_lines[i]}\n')
        boardfile.close()


def initiate(self):
    """
    Initiates the gameboard to be random
    Also records the start time for the player

    Returns:
        nothing
    """
    for r in range(5):
        for c in range(5):
            temp = random.randint(0, 2)
            if (temp == 1):
                click(self,r, c)
    global initiated
    initiated = True
    global start_time
    start_time = time.time()
    global timer_thread
    makeTimer(self)
    timer_thread.start()


def reset(self):
    """
    Resets the board to be ready for initiation and then a new game

    Returns:
        nothing
    """
    for r in range(5):
        for c in range(5):
            self.setLogicMatrix(r,c,1)
            self.setGameMatrix(r,c,"blue")
    global start_time
    start_time = 0
    global elapsed_time
    elapsed_time = 0
    global initiated
    initiated = False

def update_leaderboard(self):
    """
    Updates the Game Leaderboard to match the Leaderboard file

    Returns:
        nothing
    """
    if (board_check() == False):
        self.updateLeaderboard('N/A')
        return
    boardfile = open('leaderboard.txt', 'r')
    self.updateLeaderboard(boardfile.read())
    boardfile.close()


def board_check():
    """
    Makes sure that there is a leaderboard file before trying to open it

    Returns:
        True if the file exist and False if it does not
    """
    while True:
        try:
            with open('leaderboard.txt', 'r') as f:
                break
        except FileNotFoundError:
            return False
    return True

def makeTimer(self):
    """
    Makes the timer to keep track of player time
    """
    global stop_event
    stop_event = threading.Event()
    global timer_thread
    timer_thread = threading.Thread(target=timer, args=(self, stop_event,))
    timer_thread.daemon = True

def timer(self, stop):
    """
    Activates the timer to show the current seconds when playing the game

    Args:
        stop (threading.Event()): The event to stop the timer when the game is beaten

    Returns:
        nothing
    """
    global elapsed_time
    elapsed_time = 0
    while not stop.is_set():
        elapsed_time = time.time() - start_time
        elapsed_time = round(elapsed_time, 2)
        self.updateTimer(f'{elapsed_time} seconds')
        self.updateWindow()
        time.sleep(.01)