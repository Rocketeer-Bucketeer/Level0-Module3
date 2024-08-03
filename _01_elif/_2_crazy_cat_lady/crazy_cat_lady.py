from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    window = Tk()
    window.withdraw()
    number_of_cats = simpledialog.askinteger('hi', 'how many cats do you have?')
    if number_of_cats >= 3:
        messagebox.showinfo('hi', 'you are a crazy cat lady')
    elif number_of_cats > 0 and number_of_cats < 3:
        play_video('https://www.youtube.com/watch?v=8sI-zy3oF-c')
    elif number_of_cats == 0:
        play_video('https://www.google.com/search?q=frog+sitting+on+a+bench+like+a+human&oq=frog+sitting+on+a+bench+like+a+&gs_lcrp=EgZjaHJvbWUqCAgBEAAYFhgeMgYIABBFGDkyCAgBEAAYFhgeMg0IAhAAGIYDGIAEGIoFMg0IAxAAGIYDGIAEGIoFMgoIBBAAGIAEGKIEMgoIBRAAGIAEGKIE0gEJMTA2NjFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#')


    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
