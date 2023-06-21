import tkinter as tk
from MeteoWidget.GUI import GUI

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI.MeteoWidgetGUI(root)
    root.mainloop()
