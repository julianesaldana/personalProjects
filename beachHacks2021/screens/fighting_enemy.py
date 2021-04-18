from tkinter import *

from game_characters.enemies import *
from game_mechanics.point_detection import *

global battle_running
global current_score
global boss_count
battle_running = False
current_score = 0
boss_count = 0


class App():
    def __init__(self):
        # Window options.
        self.root = Tk()
        self.root.title("type(Quest)")
        self.root.geometry("1000x650")

        self.root.resizable(0, 0)

        # TITLE SCREEN
        self.title_label = Label(self.root, text="type(Quest)", font="Courier 60 italic bold")
        self.title_label.place(x=250, y=75)
        # self.title_label.grid()

        title_image = PhotoImage(file='images/Cody_the_Crab.gif')
        self.title_image_area = Label(self.root, image=title_image)
        self.title_image_area.place(relx=0.25, rely=0.80, anchor=CENTER)

        title_image1 = PhotoImage(file='images/Byte_the_Shark.gif')
        self.title_image_area1 = Label(self.root, image=title_image1)
        self.title_image_area1.place(relx=0.5, rely=0.5, anchor=CENTER)

        title_image2 = PhotoImage(file='images/Crypto_the_Clam.gif')
        self.title_image_area2 = Label(self.root, image=title_image2)
        self.title_image_area2.place(relx=0.75, rely=0.80, anchor=CENTER)

        self.play_button = Button(self.root, text='PLAY', command=self.character_select, font="Comic-Sans 30")
        self.play_button.place(relx=0.5, rely=0.80, anchor=CENTER)

        self.score = StringVar()
        self.score.set(current_score)
        self.current_score = Label(self.root, textvariable=self.score, font="Courier 10 bold", bg="white")

        # TITLE SCREEN END GO TO CHARACTER_SELECT() FUNCTION

        # PREMADE WIDGETS/DISPLAYS

        self.start_battle = Button(self.root, text="Start the Type!", command=self.start, font=("Arial 12 bold"))
        # self.attack = Button(self.root,text="Subtract 10 Health",command=self.damage,font=("Arial 12 bold"))

        #
        self.enemy_time_displayed = StringVar()
        self.enemy_time_displayed.set(
            "+30 health each round! Sentence bosses every 5th!")  # This value is the time that counts how many seconds until next enemy attack.
        self.time_display = Label(self.root, textvariable=self.enemy_time_displayed, font=("Courier 20 bold"),
                                  bg="yellow")

        # CHECKING RETURN
        def onReturn(event):
            self.damage()

        self.current_word = StringVar()
        self.current_word.set('Hello world!')
        self.word_box = Label(self.root, textvariable=self.current_word, font=("Courier 10 bold"), bg="white")

        self.type_box = Entry(self.root, font=("Courier 10 bold"), bg="white")  # Text box for player to enter words.
        self.type_box.bind('<Return>', onReturn)

        self.player_hp = StringVar()
        # self.player_hp.set(20) # Starting HP of player (remains after battle).
        self.player_health = Label(self.root, textvariable=self.player_hp, font=("Courier 15 bold"), bg="green")

        self.enemy_hp = StringVar()
        # self.enemy_hp.set(20) # Starting HP of enemy.
        self.enemy_health = Label(self.root, textvariable=self.enemy_hp, font=("Courier 15 bold"), bg="red")

        cody_image = PhotoImage(file='images/Cody_the_Crab.gif')
        self.cody_button = Button(self.root, image=cody_image, command=self.cody_select)
        self.cody_player = Label(self.root, image=cody_image)

        byte_image = PhotoImage(file='images/Byte_the_Shark.gif')
        self.byte_button = Button(self.root, image=byte_image, command=self.byte_select)
        self.byte_player = Label(self.root, image=byte_image)

        crypto_image = PhotoImage(file='images/Crypto_the_Clam.gif')
        self.crypto_button = Button(self.root, image=crypto_image, command=self.crypto_select)
        self.crypto_player = Label(self.root, image=crypto_image)

        enemy_image = PhotoImage(file='images/EnemiesImages/7.gif')
        self.enemy_player = Label(self.root, image=enemy_image)

        # Placing the boxes.
        # self.type_box.place(x=130,y=200)
        # self.player_health.place(x=130,y=250)
        # self.enemy_health.place(x=200,y=250)
        # self.time_display.place(x=160,y=10)

        # self.attack.place(x=130,y=150)
        # self.start_battle.place(x=130,y=100)

        self.root.mainloop()

    def character_select(self):
        self.time_display.place_forget()
        self.title_label.place_forget()
        self.title_image_area.place_forget()
        self.title_image_area1.place_forget()
        self.title_image_area2.place_forget()
        self.play_button.place_forget()

        # self.cody_image_area.place(x=500,y=100)

        # CHARACTER SELECT BEGINS
        self.title_label = Label(self.root, text='Choose your character!', font="Courier 30 italic bold")
        self.title_label.place(relx=0.50, rely=0.15, anchor=CENTER)
        # self.title_label.place_forget()

        # Cody
        self.cody_button.place(relx=0.25, rely=0.50, anchor=CENTER)

        # Byte
        self.byte_button.place(relx=0.50, rely=0.50, anchor=CENTER)

        # Crypto
        self.crypto_button.place(relx=0.75, rely=0.50, anchor=CENTER)


    # def loop_character_select(self):
    #     self.time_display.place_forget()
    #     self.title_label = Label(self.root, text='Choose your character!', font="Courier 30 italic bold")
    #     # self.title_label.pack(ipady=50)
    #     self.title_label.place_forget()  ####
    #
    #     # Cody
    #     self.cody_button.place(relx=0.15, rely=0.80, anchor=W)
    #     # Byte
    #     self.byte_button.place(relx=0.15, rely=0.80, anchor=W)
    #     # Crypto
    #     self.crypto_button.place(relx=0.15, rely=0.80, anchor=W)

    def cody_select(self):
        global player_image
        global enemy_image
        # Give specific stats
        self.score.set(0)
        self.player_hp.set(100)
        player_image = PhotoImage(file='images/Cody_the_Crab.gif')
        enemy_image = PhotoImage(file='images/EnemiesImages/7.gif')
        self.word_box.place(relx=0.50, rely=0.45, anchor=CENTER)
        self.type_box.place(relx=0.50, rely=0.60, anchor=CENTER)
        self.player_health.place(relx=0.15, rely=0.68, anchor=W)
        self.enemy_health.place(relx=0.85, rely=0.68, anchor=E)
        self.time_display.place(relx=0.5, rely=0.10, anchor=CENTER)
        self.current_score.place(relx=0.95, rely=0.10, anchor=E)

        # self.attack.pack(pady=20)
        self.start_battle.place(relx=0.50, rely=0.80, anchor=CENTER)

        self.cody_button.place_forget()
        self.byte_button.place_forget()
        self.crypto_button.place_forget()
        self.title_label.place_forget()

        self.cody_player.place(relx=0.15, rely=0.80, anchor=CENTER)

    def byte_select(self):

        global player_image
        global enemy_image
        # Give specific stats
        self.score.set(0)
        self.player_hp.set(100)
        player_image = PhotoImage(file='images/Byte_the_Shark.gif')
        enemy_image = PhotoImage(file='images/EnemiesImages/7.gif')
        self.word_box.place(relx=0.50, rely=0.45, anchor=CENTER)
        self.type_box.place(relx=0.50, rely=0.60, anchor=CENTER)
        self.player_health.place(relx=0.15, rely=0.68, anchor=W)
        self.enemy_health.place(relx=0.85, rely=0.68, anchor=E)
        self.time_display.place(relx=0.5, rely=0.10, anchor=CENTER)
        self.current_score.place(relx=0.95, rely=0.10, anchor=E)

        # self.attack.pack(pady=20)
        self.start_battle.place(relx=0.50, rely=0.80, anchor=CENTER)

        self.cody_button.place_forget()
        self.byte_button.place_forget()
        self.crypto_button.place_forget()
        self.title_label.place_forget()

        self.byte_player.place(relx=0.15, rely=0.80, anchor=CENTER)

    def crypto_select(self):
        global player_image
        global enemy_image
        # Give specific stats
        self.score.set(0)
        self.player_hp.set(100)
        player_image = PhotoImage(file='images/Crypto_the_Clam.gif')
        enemy_image = PhotoImage(file='images/EnemiesImages/7.gif')
        self.word_box.place(relx=0.50, rely=0.45, anchor=CENTER)
        self.type_box.place(relx=0.50, rely=0.60, anchor=CENTER)
        self.player_health.place(relx=0.15, rely=0.68, anchor=W)
        self.enemy_health.place(relx=0.85, rely=0.68, anchor=E)
        self.time_display.place(relx=0.5, rely=0.10, anchor=CENTER)
        self.current_score.place(relx=0.95, rely=0.10, anchor=E)

        # self.attack.pack(pady=20)
        self.start_battle.place(relx=0.50, rely=0.80, anchor=CENTER)

        self.cody_button.place_forget()
        self.byte_button.place_forget()
        self.crypto_button.place_forget()
        self.title_label.place_forget()

        self.crypto_player.place(relx=0.15, rely=0.80, anchor=CENTER)

    # BATTLE STUFF
    def start(self):
        global battle_running
        global current_enemy
        global boss_count
        global enemy_image

        random_image = random.randint(1, 20)
        enemy_image = PhotoImage(file='images/EnemiesImages/{}.gif'.format(random_image))
        self.enemy_player.configure(image=enemy_image)
        self.enemy_player.place(relx=0.85, rely=0.80, anchor=CENTER)

        boss_count += 1
        if boss_count == 5:
            current_enemy = BossEnemy("Enemy")
            boss_count = 0  # Might change later
        else:
            current_enemy = random.choice(
                [EasyEnemy("Enemy"), MediumEnemy("Enemy"), HardEnemy("Enemy"), SuperHardEnemy("Enemy")])
        self.enemy_hp.set(current_enemy.hp)
        self.enemy_time_displayed.set(current_enemy.time)
        self.current_word.set(current_enemy.word)
        ###
        # player1 = Player("Player1")
        # enemy1 = EasyEnemy("Enemy1")
        # self.player_health = player1.hp
        # self.enemy_hp = enemy1.hp
        ###
        # self.player_hp.set(newHP)

        battle_running = True
        self.start_battle.place_forget()
        self.timer()  # Starts the timer.

    def damage(self):
        global current_enemy, current_score

        result = stringCheck(self.type_box.get(), self.current_word.get())
        current_score += result[0]
        self.score.set(current_score)
        removed_player_hp = int(self.player_hp.get()) - int(result[1])
        self.player_hp.set(removed_player_hp)
        removed_enemy_hp = int(self.enemy_hp.get()) - int(result[0])
        self.enemy_hp.set(removed_enemy_hp)
        self.type_box.delete(0, 'end')

        current_enemy.generateNewWord()

        # newWord = 'NEXT'
        self.current_word.set(current_enemy.word)
        # enemy_hp = int(self.enemy_hp.get()) - 10
        # self.enemy_hp.set(enemy_hp)

    def timer(self):
        global battle_running
        global current_enemy
        global boss_count
        enemy_hp = self.enemy_hp.get()

        if int(self.player_hp.get()) <= 0:
            battle_running = False
            self.enemy_time_displayed.set('GAME OVER')
            self.type_box.place_forget()
            self.player_health.place_forget()
            self.enemy_health.place_forget()
            self.word_box.place_forget()
            # self.attack.place_forget()
            self.start_battle.place_forget()
            self.cody_player.place_forget()
            self.byte_player.place_forget()
            self.crypto_player.place_forget()
            self.enemy_player.place_forget()
            # self.current_score.place_forget()
            self.root.after(5000, self.character_select)

        if int(enemy_hp) <= 0:
            if boss_count == 4:
                self.enemy_time_displayed.set('Boss incoming!')
            else:
                self.enemy_time_displayed.set('Victory! +30 Health')
                self.player_hp.set(int(self.player_hp.get()) + 30)
            battle_running = False
            self.root.after(5000, self.start)


        if battle_running:
            enemy_time = self.enemy_time_displayed.get()
            if str(enemy_time) == 'Attacking!':
                enemy_time = 0
            enemy_time = int(enemy_time)
            if enemy_time != 0:
                enemy_time -= 1
            else:
                enemy_time = current_enemy.time

                newHP = int(self.player_hp.get()) - current_enemy.damage
                self.player_hp.set(newHP)

            if enemy_time == 0:
                enemy_time = 'Attacking!'

                # THIS CONNECTS TO THE GAME OVER SCREEN

            self.enemy_time_displayed.set(enemy_time)

            self.root.after(1000, self.timer)  # 1 second passes, runs code again.
