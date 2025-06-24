
import tkinter as tk
from time import strftime


class DigitalClock:
    """
    A simple digital clock GUI application.
    """

    def __init__(self, root: tk.Tk):
        """
        Initialize the GUI and clock label.
        :param root: tkinter root window.
        """
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        self.label = tk.Label(
            self.root,
            font=('Courier', 48),
            background='black',
            foreground='cyan'
        )
        self.label.pack(expand=True)

        self.update_time()

    def update_time(self):
        """
        Update the clock label every second.
        """
        current_time = strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_time)


def main():
    """
    Run the digital clock application.
    """
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
