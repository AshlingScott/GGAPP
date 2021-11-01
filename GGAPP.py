from tkinter import*
from PIL import ImageTk, Image
from Character import Character

#characters supported by app
character_list = [
	"Chipp",
	"Ramlethal",
	"JackO"
]

#create Characters
Chipp = Character("Chipp", "ChippWakeups.png")
Ram = Character("Ramlethal", "RamlethalWakeups.png")

#create window
root = Tk()
root.title("Guilty Gear Companion App")
root.geometry("850x750")
root.resizable(False, False)

#GG logo
gg_logo = ImageTk.PhotoImage(Image.open("GGStriveLogo.png"))
logo_label = Label(image=gg_logo)
logo_label.grid(row=0, column=1, columnspan=2)

#frame that changes to display wanted data
main_frame = LabelFrame(root, padx=20, pady=20)
main_frame.grid(row=1, column=0, columnspan=4)

#character select widgets
character_selected = StringVar()
character_selected.set("Chipp")

#changes displayed image based on dropdown choice
def update_char_selected(new_char):
	global chart_label

	if new_char == "Chipp":
		chart_label.destroy()
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/ChippWakeups.png"))

	if new_char == "Ramlethal":
		chart_label.destroy()
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/RamlethalWakeups.png"))

	if new_char == "JackO":
		chart_label.destroy()
		wakeup_chart = ImageTk.PhotoImage(Image.open("Images/JackOWakeups.png"))

	chart_label = Label(main_frame, image=wakeup_chart)
	chart_label.photo = wakeup_chart
	chart_label.grid(row=2, column=0, columnspan=2)

#the wakeup chart, changes depending on character select
wakeup_chart = ImageTk.PhotoImage(Image.open("Images/ChippWakeups.png"))
chart_label = Label(main_frame, image=wakeup_chart)
chart_label.photo = wakeup_chart
chart_label.grid(row=2, column=0, columnspan=2)

character_label = Label(main_frame, text="Wakeup Options", font="Helvetica 18 bold")
drop_down = OptionMenu(main_frame, character_selected, *character_list, command=update_char_selected)

character_label.grid(row=0, column=0)
drop_down.grid(row=0, column=1)

#Options on main page
wakeup_options_button = Button(root, text="Wakeup Options", width=25)
optimal_routes_button = Button(root, text="Optimal Combo Routes", width=25)
matchup_chart_button = Button(root, text="Matchup Chart", width=25)
placeholder_button = Button(root, text="Placeholder", width=25)

wakeup_options_button.grid(row=2, column=0, padx=(25,12), pady=25)
optimal_routes_button.grid(row=2, column=1, pady=25)
matchup_chart_button.grid(row=2, column=2, pady=25)
placeholder_button.grid(row=2, column=3, padx=(12, 0), pady=25)

root.mainloop()
