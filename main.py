import requests
import tkinter as tk
#from MeteoWidget import MeteoWidget, MeteoWidgetConsole
from MeteoWidget.GUI import GUI
from MeteoWidget.MeteoWidget import  MeteoWidget

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI.MeteoWidgetGUI(root)
    root.mainloop()
    # widget_console = MeteoWidgetConsole()
    # widget_console.run()