import wood_scraper
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

OptionList = [
'                            SciFi                          ',
'                            Thrillers                      ',
'                            History                        ']

window = tk.Tk()

window.title('Best Seller')
window.geometry('800x450')

canvas=tk.Canvas(window, width=800, height=450)
image=ImageTk.PhotoImage(Image.open('C:/Users/blake/OneDrive/desktop/Book_Scraper/lake.png'))
backgroung_label= tk.Label(window, image=image)
backgroung_label.place(relwidth=1, relheight=1)


mainframe = tk.Frame(window, bg= "blue")
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(padx=100, pady=100)

variable = tk.StringVar(window)
variable.set('Choose Book Category')


opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=60, font=('Helvetica', 12), cursor= "hand2", bg='#81828a')
opt.pack(side="top")

result = tk.Label(width=85, height=4, font=('Helvetica', 11), fg='#bcc2c2', bg='#4d6182')
result.pack(side='top')


def url():
	if variable.get() == '                            History                        ':
		webbrowser.open_new(wood_scraper.hurl())
	elif variable.get() == '                            Thrillers                      ':
		webbrowser.open_new(wood_scraper.turl())
	else:
		webbrowser.open_new(wood_scraper.scurl())

book_link = tk.Button(window, text='Book Link', command=url, cursor="hand2", fg='#ffffff', bg='#81828a')
book_link.pack(side='top')
# book_link.bind(("<Button-1>", lambda e: url()))


quit = tk.Button(window, text='Quit Program', command= window.quit, width=20, cursor="hand2", bg='#81828a')
quit.place(relx=.41, rely=.9)



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