import tkinter as tk
from unittest.mock import DEFAULT

LIGHT_GRAY='#F5F5F5'
LABEL_COLOR='#25265E'
WHITE='#FFFFFF'
OFF_WHITE='#F8FAFF'
LIGHT_BLUE="#ccedff"
SMALL_FONT_STYLE=('Arial', 16)
LARGE_FONT_STYLE=('Arial', 40, 'bold')
DIGITS_FONT_STYLE=('Arial', 24, 'bold')
DEFAULT_FONT_STYLE=('Arial', 20)

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
        
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.operations={"/":"\u00F7", "*":"\u00D7", "+":"+", "-":"-"}
        self.buttons_frame = self.create_buttons_frame()
        
        self.buttons_frame.rowconfigure(0,weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
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
    
    def create_digit_buttons(self):
        for key, value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(key), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=value[0], column=value[1], sticky=tk.NSEW)
    
    def create_operator_buttons(self):
        i=0
        for key, value in self.operations.items():
            button = tk.Button(self.buttons_frame, text=value, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1,columnspan=3, sticky=tk.NSEW)
       
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)
             
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(fill="both", expand=True)
        return frame
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
