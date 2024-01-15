import tkinter as tk
import random
import time
from datetime import datetime

jsonfile = []

fname = ""

class ACTGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ACT Game")
        ## Constants
        self.num_buttons = 18
        self.num_red_buttons = 3
        self.error_label = tk.Label(root, text="",font=('Times New Roman', 15, 'bold'))
        self.error_label.pack()
        self.currentround = -1
        self.wincount = 0
        self.curr_round = tk.Label(root, text=self.currentround,font=('Times New Roman', 15, 'bold'))
        self.curr_round.pack()
        ## Current round variables
        self.elucid = False
        self.numreds = 0
        self.lastidx = 0
        self.rounddata = [0,0]
        self.round_time = 0
        self.elapsed_time = datetime.now() - datetime.now()
        
        # ui elements
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game,width=10,height=3,font=('Times New Roman', 15, 'bold'))
        self.reset_button.pack()

        self.reset_game()

    def reset_game(self):
        if self.currentround == 25:
            self.buttons_frame.destroy()
            self.endgame()
        else:
            
            self.error_label.config(text="")
            self.currentround+=1
            self.curr_round.config(text="Round "+str(self.currentround))
            self.start_time = time.time()
            ## check if we win or not
            if self.numreds >= 3:
                self.wincount+=1
            ## reset to new round
            self.elucid=False
            if self.start_time:
                self.rounddata[1]=self.elapsed_time.total_seconds()
                jsonfile.append(self.rounddata)
            print("Round "+str(len(jsonfile)-1)+": ",end="")
            print(self.rounddata)
            self.rounddata = [0,0]
            self.numreds=0 # reset
            self.lastidx=0 # reset
            ## diagnostics
            print(self.wincount)
            ## remake the gui elements
            self.buttons_frame.destroy()
            self.buttons_frame = tk.Frame(self.root)
            self.buttons_frame.pack()
            self.button_colors = ['red'] * self.num_red_buttons + [self.random_color() for _ in range(self.num_buttons - self.num_red_buttons)]
            random.shuffle(self.button_colors)
            self.buttons = []
            for i in range(self.num_buttons):
                button = tk.Button(self.buttons_frame, text=str(i+1), width=10, height=5, bg=self.button_colors[i],
                                command=lambda idx=i: self.check_button(idx))
                button.pack(side=tk.LEFT)
                self.buttons.append(button)
            self.restart_stopwatch()

    def restart_stopwatch(self):
        self.start_time = datetime.now()
        self.update_time()

    def update_time(self):
        if self.start_time:
            self.elapsed_time = datetime.now() - self.start_time
            self.root.after(100, self.update_time)



    def random_color(self):
        colors = ['blue', 'green', 'yellow', 'purple', 'orange', 'pink']
        return random.choice(colors)

    def check_button(self, idx):
        ##print(idx)
        if (self.lastidx < idx or idx==0) and self.button_colors[idx] == 'red':
            self.numreds+=1
            self.lastidx=idx
            if self.numreds>=3:
                if (not self.elucid) or self.start_time:
                    self.elucid=True
                    self.rounddata[0]=self.elapsed_time.total_seconds()
                    self.restart_stopwatch()
        else:
            self.handle_error()

    def handle_error(self):
        self.numreds=-9
        self.error_label.config(text="ERROR MADE",font=('Times New Roman', 15, 'bold'))
        if (not self.elucid) or self.start_time:
            self.elucid=True
            self.rounddata[0]=self.elapsed_time.total_seconds()
            self.restart_stopwatch()

    def endgame(self):
        ## export as json file
        print("Participant: "+fname)
        print("Wins: "+str(self.wincount))
        print("Losses: "+str(25-self.wincount))
        roundaverage = 0
        lengood = 0
        reactaverage = 0
        for i in jsonfile:
            if (i[0]!=0):
                lengood+=1;
                roundaverage+=i[0]
                reactaverage+=i[1]
        roundaverage /= lengood
        reactaverage /= lengood
        print("Good Rounds: "+str(lengood))
        print("Round Average: "+str(roundaverage))
        print("React Average: "+str(reactaverage))
        print(jsonfile)
        print("Entropy: ")
        


def start_game(root, player_name):
    
    root.destroy()
    game_root = tk.Tk()
    game = ACTGame(game_root)
    game_root.mainloop()



def start_menu():
    root = tk.Tk()
    root.title("ACT Game Start Menu")

    label = tk.Label(root, text="Enter your name:",font=('Times New Roman', 15, 'bold'))
    label.pack()

    name_entry = tk.Entry(root,font=('Times New Roman', 15, 'bold'))
    name_entry.pack()
    fname = name_entry.get()
    start_button = tk.Button(root, text="Start Game", font=('Times New Roman', 15, 'bold'), command=lambda: start_game(root, fname))
    start_button.pack()
    root.mainloop()


if __name__ == "__main__":
    start_menu()