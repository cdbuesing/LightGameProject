from gui import *


def main() :
    window = Tk()
    window.title('Light Game')
    window.geometry('500x600')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()