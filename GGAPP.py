from tkinter import*
from PIL import ImageTk, Image

global character_list
global character_selected

#characters supported by app
character_list = [
	"Chipp",
	"Ramlethal",
	"Jacko",
	"Ky"
]

root = Tk()
root.title("Guilty Gear Companion App")
root.geometry("850x750")
root.resizable(False, False) 

#Main screen logo
gg_logo = ImageTk.PhotoImage(Image.open("GGStriveLogo.png"))
logo_label = Label(image=gg_logo)
logo_label.grid(row=0, column=1, columnspan=2)

#frame that changes to display wanted data
main_frame = LabelFrame(root, padx=20, pady=20)
main_frame.grid(row=1, column=0, columnspan=4)

#character select widgets
character_selected = StringVar()
character_selected.set("Chipp")

character_label = Label(main_frame, text="Select your character")
drop_down = OptionMenu(main_frame, character_selected, *character_list)

character_label.grid(row=0, column=0)
drop_down.grid(row=1, column=0)

#the wakeup chart, changes depending on character select
wakeup_chart = ImageTk.PhotoImage(Image.open("ChipWakeups.png"))
chart_label = Label(main_frame, image=wakeup_chart)
chart_label.photo = wakeup_chart
chart_label.grid(row=2, column=0, columnspan=2)

#Wakeup chart page, shows outcomes of all wakeup interactions for a selected character
# Is also the default page
def wakeup_click():

	wake_up_screen = Toplevel()
	wake_up_screen.title("Wakeup Options Chart")
	wake_up_screen.geometry("900x600")

	wakeup_frame = LabelFrame(wake_up_screen, padx=20, pady=20)
	wakeup_frame.grid(row=0, column=0)

	#brings up wakup oki chart for selected character
	def show_chart():
		chipp_w_chart = ImageTk.PhotoImage(Image.open("ChipWakeups.png"))
		chipp_image_label = Label(wake_up_screen, image=chipp_w_chart)
		chipp_image_label.photo = chipp_w_chart
		chipp_image_label.grid(row=3, column=0, columnspan=2)

	character_selected = StringVar()
	character_selected.set("Chipp")

	#character select widgets
	#character_label = Label(wakeup_frame, text="Select your character")
	#drop_down = OptionMenu(wakeup_frame, character_selected, *character_list)
	#confirm_button = Button(wake_up_frame, text="Choose", command=show_chart, width=25)

	#character_label.grid(row=0, column=0, columnspan=2)
	#drop_down.grid(row=1, column=0, sticky="ew")
	#confirm_button.grid(row=1, column=1)


confirm_button = Button(main_frame, text="Choose", width=25)  #command=show_chart
confirm_button.grid(row=1, column=1)


#Options on main page
wakeup_options_button = Button(root, text="Wakeup Options", command=wakeup_click, width=25)
optimal_routes_button = Button(root, text="Optimal Combo Routes", width=25)
matchup_chart_button = Button(root, text="Matchup Chart", width=25)
placeholder_button = Button(root, text="Placeholder", width=25)

wakeup_options_button.grid(row=2, column=0, padx=25)
optimal_routes_button.grid(row=2, column=1)
matchup_chart_button.grid(row=2, column=2)
placeholder_button.grid(row=2, column=3)

#e = Entry(root, width=50)
#e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


#def myClick():
	#myLabel = Label(root, text=e.get())
	#myLabel.grid(row=2, column=0, columnspan=3)

# Create widgets
#title = Label(root, text="Guilty Gear App")
#myButton = Button(root, text="click me", command=myClick, fg="blue", bg="white")

# Add widgets
#title.grid(row=0, column=0)
#myButton.grid(row=1, column=0)
#title.pack()
#myButton.grid(row=1, column=0, columnspan =3)


root.mainloop()