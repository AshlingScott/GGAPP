from tkinter import*
from PIL import ImageTk, Image
from Character import Character

#create window
root = Tk()
root.title("Guilty Gear Companion App")
root.geometry("850x750")
root.resizable(False, False)

current_frame = "Wakeups"

#characters supported by app
character_selected = StringVar()
character_list = [
	"Chipp",
	"Ramlethal",
	"JackO"
]

#GG logo
gg_logo = ImageTk.PhotoImage(Image.open("Images/GGStriveLogo.png"))
logo_label = Label(image=gg_logo)
logo_label.grid(row=0, column=1, columnspan=2)

#frame that changes to display wanted data
main_frame = LabelFrame(root, padx=20, pady=20)
main_frame.grid(row=1, column=0, columnspan=4)

#switch to new frame section: Wakeups, Combos, Matchups
def switch_to_frame(frame):
	#update frame variable
	global current_frame
	current_frame = frame
	print("Switch to frame")

	#defaults to Chipp
	character_selected.set("Chipp")
	chart_image = ImageTk.PhotoImage(Image.open("Images/Chipp" + frame + ".png"))
	chart_label = Label(main_frame, image = chart_image)
	chart_label.photo = chart_image
	chart_label.grid(row=2, column=0, columnspan=2)

	character_label = Label(main_frame, text = frame + " Options", font="Helvetica 18 bold", padx=25)
	drop_down = OptionMenu(main_frame, character_selected, *character_list, command=update_frame)

	character_label.grid(row=0, column=0)
	drop_down.grid(row=0, column=1)

#switches the character used, from drop down list
def update_frame(new_char):
	global current_frame
	print("Update Frame")

	chart_image = ImageTk.PhotoImage(Image.open("Images/" + new_char + current_frame+ ".png"))

	chart_label = Label(main_frame, image=chart_image)
	chart_label.photo = chart_image
	chart_label.grid(row=2, column=0, columnspan=2)

#initializes set to Wakeups frame
chart_label = Label(main_frame)
switch_to_frame("Wakeups")

#Option Buttons on bottom row of page
wakeup_options_button = Button(root, text="Wakeup Options", width=25, command=lambda: switch_to_frame("Wakeups"))
optimal_routes_button = Button(root, text="Optimal Combo Routes", width=25, command=lambda: switch_to_frame("Combos"))
matchup_chart_button = Button(root, text="Matchup Chart", width=25)
placeholder_button = Button(root, text="Placeholder", width=25)

wakeup_options_button.grid(row=2, column=0, padx=(25,12), pady=25)
optimal_routes_button.grid(row=2, column=1, pady=25)
matchup_chart_button.grid(row=2, column=2, pady=25)
placeholder_button.grid(row=2, column=3, padx=(12, 0), pady=25)

root.mainloop()
