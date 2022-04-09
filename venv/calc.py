import tkinter as tk

LIGHT_GRAY='#F5F5F5'
LABEL_COLOR='#25265E'
SMALL_FONT_STYLE=('Arial', 16)
LARGE_FONT_STYLE=('Arial', 40, 'bold')

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0, 0)
        
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        
        self.total_label, self.label = self.create_display_labels()
        self.button_frame = self.create_button_frame()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, font=SMALL_FONT_STYLE, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24)
        total_label.pack( fill="both", expand=True)
        
        label = tk.Label(self.display_frame, text=self.current_expression, font=LARGE_FONT_STYLE, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24)
        label.pack( fill="both", expand=True)
        
        return total_label, label
        
    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(fill="both", expand=True)
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
    
