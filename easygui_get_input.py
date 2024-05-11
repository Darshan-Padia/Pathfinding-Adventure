from easygui import *
# from tkinter import Tk


def get_input(s="question",img=""):
    # root = Tk()
    # pos = int(root.winfo_screenwidth() * 0.5), int(root.winfo_screenheight() * 0.2)
    # root.withdraw()
    # rootWindowPosition = "+%d+%d" % pos

    # # patch rootWindowPosition
    # rootWindowPosition = rootWindowPosition
    ans = enterbox(s,image=img)
    return ans


def show(s = 'message'):
    # root = Tk()
    # pos = int(root.winfo_screenwidth() * 0.5), int(root.winfo_screenheight() * 0.2)
    # root.withdraw()
    # rootWindowPosition = "+%d+%d" % pos

    # # patch rootWindowPosition
    # rootWindowPosition = rootWindowPosition
    msgbox(s)
