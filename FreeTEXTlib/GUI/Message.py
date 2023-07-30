import tkinter as tk
from FreeTEXTlib.Base import Formatter


class ShowFormatterMeta:
    def __init__(self, run_now: bool, formatter: Formatter):
        self.root = tk.Tk()
        self.root.title("Formatter Meta Information")
        self.root.geometry("300x180")

        meta = [
            f"Creator: {formatter.data.header.creator.lastname}, {formatter.data.header.creator.firstname}",
            f"Created at: {formatter.data.header.date}",
            f"Library Version: {formatter.data.footer.libVersion}",
            f"Program Version: {formatter.data.footer.programVersion}",
            f"Formatter Version: {formatter.data.footer.formatterVersion}"
        ]

        for i in meta:
            lbl = tk.Label(self.root, text=i)
            lbl.pack()

        btn_close = tk.Button(self.root, text="Close", command=self.close_window)
        btn_close.pack()

        if run_now:
            self.run()

    def run(self):
        print("Running Meta Message")
        self.root.mainloop()
        print("Closed Meta Message")

    def close_window(self):
        self.root.quit()