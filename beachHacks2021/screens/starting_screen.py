# from tkinter import *
# from tkinter import ttk

# root = Tk()


# def starting_screen():
#     # ! STARTING SCREEN

#     # ! Making window size
#     root.geometry("1000x650")

#     # # ! Frames
#     # f1 = Frame(root)
#     # f2 = Frame(root)

#     # ! Title_label
#     title_label = ttk.Label(text="Welcome to Type(Quest)")
#     title_label.pack(ipady=50)

#     # ! Image_label
#     image_label = ttk.Label()
#     image_label.pack()

#     # ! Image
#     image = PhotoImage(file='images/Cody_the_Crab_resize.png')
#     image_label.config(image=image)

#     # ! Callback from play button to transition frames
#     # def callback(output):
#     #     print(output)

#     # # * add
#     # for frame in (f1,f2):
#     #     frame.pack()

#     # ! Capturing input with buttons
#     play_button = ttk.Button(text="Play", command=lambda: root.destroy())
#     play_button.pack(pady=15)

#     # ! Directions
#     directions_label = ttk.Label(
#         text="Directions:\n- Eliminate enemies by typing word correctly displayed on the screen\n-"
#              + " Game gets progressively harder as you eliminate more enemies\n- Survive ")
#     directions_label.pack()

#     # ! Configurations

#     # * Title Name Configuration
#     title_label.config(font=("Courier", 30, "italic", "bold"))

#     root.mainloop()


# # * Call
# # starting_screen()
