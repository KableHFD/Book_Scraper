import wood_scraper
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

OptionList = [
'                            SciFi                          ',
'                            Thrillers                      ',
'                            History                        ']

window = tk.Tk()

window.title('Pick your book category')
window.geometry('700x550')

canvas=tk.Canvas(window, width=700, height=550)
image=ImageTk.PhotoImage(Image.open('C:/Users/blake/OneDrive/Pictures/lake.png'))

canvas.create_image(350, 275, image=image)
canvas.place(x=0, y=0)


mainframe = tk.Frame(window, bg= "blue")
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(padx=100, pady=100)

variable = tk.StringVar(window)
variable.set('Book Categories')


label = tk.Label(text="Choose category:", width=20, font=('Helvetica', 12), fg='black', bg='#4d6182')
label.pack(side="top")

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=60, font=('Helvetica', 12), cursor= "hand2", bg='white')
opt.pack(side="top")

result = tk.Label(width=90, font=('Helvetica', 12), fg='black', bg='#4d6182')
result.pack(side='top')


# result2 = tk.Label(width=90, font=('Helvetica', 12), fg='Blue')
# result2.pack(side='top')
# result2.bind(("<Button-1>", lambda e: callback2()))

def callback2():
	if variable.get() == '                            History                        ':
		webbrowser.open_new(wood_scraper.hurl())
	elif variable.get() == '                            Thrillers                      ':
		webbrowser.open_new(wood_scraper.turl())
	else:
		webbrowser.open_new(wood_scraper.scurl())

book_link = tk.Button(window, text='Book Link', command=callback2, cursor="hand2")
book_link.pack(side='top')
book_link.bind(("<Button-1>", lambda e: callback2()))


quit = tk.Button(window, text='Quit Program', command= window.quit, width=20, cursor="hand2")
quit.pack(padx=90, pady=70)



def callback(*args):
	if variable.get() == '                            History                        ':
		result.configure(text=wood_scraper.History())
		# result2.configure(text=wood_scraper.hurl())
		# webbrowser.open_new(wood_scraper.hurl())
	elif variable.get() == '                            Thrillers                      ':
		result.configure(text=wood_scraper.Thrillers())
		# result2.configure(text=wood_scraper.turl())
		# webbrowser.open_new(wood_scraper.turl())
	else:
		result.configure(text=wood_scraper.SciFi())
		# result2.configure(text=wood_scraper.scurl())
		# webbrowser.open_new(wood_scraper.scurl())
	






    

variable.trace("w", callback)



window.mainloop()