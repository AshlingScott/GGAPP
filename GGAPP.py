from tkinter import*
from PIL import ImageTk, Image
from Character import Character

#create window
root = Tk()
root.title("Guilty Gear Companion App")
root.geometry("850x750")
root.resizable(False, False)

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

#switches to Wakeup Frame, defaults to Chipp as selected character
def switch_to_wakeup_chart():
	global drop_down
	drop_down.destroy()

	character_selected.set("Chipp")
	wakeup_chart = ImageTk.PhotoImage(Image.open("Images/ChippWakeups.png"))
	chart_label = Label(main_frame, image=wakeup_chart)
	chart_label.photo = wakeup_chart
	chart_label.grid(row=2, column=0, columnspan=2)

	character_label = Label(main_frame, text="Wakeup Options", font="Helvetica 18 bold")
	drop_down = OptionMenu(main_frame, character_selected, *character_list, command=update_wakeup_chart)

	character_label.grid(row=0, column=0)
	drop_down.grid(row=0, column=1)

#updates the Wakeup Frame to the selected character
def update_wakeup_chart(new_char):
	if new_char == "Chipp":
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/ChippWakeups.png"))
	if new_char == "Ramlethal":
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/RamlethalWakeups.png"))
	if new_char == "JackO":
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/JackOWakeups.png"))

	chart_label = Label(main_frame, image=wakeup_chart)
	chart_label.photo = wakeup_chart
	chart_label.grid(row=2, column=0, columnspan=2)

def switch_to_combo_chart():
	global drop_down
	drop_down.destroy()

	character_selected.set("Chipp")
	wakeup_chart = ImageTk.PhotoImage(Image.open("Images/ChippCombos.png"))
	chart_label = Label(main_frame, image=wakeup_chart)
	chart_label.photo = wakeup_chart
	chart_label.grid(row=2, column=0, columnspan=2)

	character_label = Label(main_frame, text="Combo Routes", font="Helvetica 18 bold")
	drop_down = OptionMenu(main_frame, character_selected, *character_list, command=update_combo_chart)

	character_label.grid(row=0, column=0)
	drop_down.grid(row=0, column=1)

def update_combo_chart():
	if new_char == "Chipp":
		combo_chart = ImageTk.PhotoImage(Image.open("Images/ChippCombos.png"))
	if new_char == "Ramlethal":
		combo_chart = ImageTk.PhotoImage(Image.open("Images/RamlethalWakeups.png"))
	if new_char == "JackO":
		combo_chart = ImageTk.PhotoImage(Image.open("Images/JackOWakeups.png"))

	chart_label = Label(main_frame, image=combo_chart)
	chart_label.photo = combo_chart
	chart_label.grid(row=2, column=0, columnspan=2)

character_label = Label(main_frame, text="Wakeup Options", font="Helvetica 18 bold")
drop_down = OptionMenu(main_frame, character_selected, *character_list, command=update_wakeup_chart)

character_label.grid(row=0, column=0)
drop_down.grid(row=0, column=1)

chart_label = Label(main_frame)
switch_to_wakeup_chart()

#Options on main page
wakeup_options_button = Button(root, text="Wakeup Options", width=25, command=switch_to_wakeup_chart)
optimal_routes_button = Button(root, text="Optimal Combo Routes", width=25, command=switch_to_combo_chart)
matchup_chart_button = Button(root, text="Matchup Chart", width=25)
placeholder_button = Button(root, text="Placeholder", width=25)

wakeup_options_button.grid(row=2, column=0, padx=(25,12), pady=25)
optimal_routes_button.grid(row=2, column=1, pady=25)
matchup_chart_button.grid(row=2, column=2, pady=25)
placeholder_button.grid(row=2, column=3, padx=(12, 0), pady=25)

root.mainloop()
