import curses
from curses import wrapper
import time
import queue
maze=[
    ["#","#","#","s","#","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," ","#","#","#"],
    ["#"," "," "," "," ","#"],
    ["#","#","#","e","#","#"]
]
def print_maze(maze,stdscr):
    WHITE=curses.color_pair(1)
    RED=curses.color_pair(2)

    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            stdscr.addstr(i,j*2,value,RED)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    stdscr.clear()
    print_maze(maze,stdscr)
    stdscr.refresh()
    stdscr.getch()
wrapper(main)