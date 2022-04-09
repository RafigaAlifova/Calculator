import tkinter as tk

LIGHT_GRAY='#F5F5F5'
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0, 0)
        
        self.display.frame = self.create_display_frame()
        self.button.frame = self.create_button_frame()
        
    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack( fill="both", expand=True)
        return frame
    
    def create_button_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(fill="both", expand=True)
        return frame
        
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
