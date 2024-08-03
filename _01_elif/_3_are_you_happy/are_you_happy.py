from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #
    #Use pop-ups to recreate the chart using if and elif statements
    an1 = simpledialog.askstring('hi', 'are you happy?')
    if an1 == 'yes':
        messagebox.showinfo('hi', 'keep doing what you are doing')
    elif an1 == 'no':
        an2 = simpledialog.askstring('hi', 'do you want to be happy?')

    if an2 == 'yes':
        messagebox.showinfo('hi', 'then change something')
    if an2 == 'no':
        messagebox.showinfo('hi', 'keep doing what you are doing')

    pass
