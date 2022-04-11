from re import S
import tkinter as tk
from unittest.mock import DEFAULT

LIGHT_GRAY='#ebebeb' #bg
LABEL_COLOR='#000e75' #num and char color
WHITE='#ffffff' #digits bg
OFF_WHITE="#f5f5f5" #operator bg
LIGHT_BLUE='#99ccff' #equal bg

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
        
        self.total_expression = ""
        self.current_expression = ""
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
        self.create_square_button()
        self.create_sqrt_button()
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
    
    def add_to_expression(self, digit):
        self.current_expression += str(digit)
        self.update_label()
    
    def create_digit_buttons(self):
        for key, value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(key), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=key: self.add_to_expression(x))
            button.grid(row=value[0], column=value[1], sticky=tk.NSEW)
    
    def append_operator(self, operator):
        self.total_expression += self.current_expression + operator
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    
    def create_operator_buttons(self):
        i=0
        for key, value in self.operations.items():
            button = tk.Button(self.buttons_frame, text=value, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,command=lambda x=key: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    
    def clear(self):
        self.total_expression = ""
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
    
    def square(self):
        self.current_expression = str(eval(self.current_expression)**2)
        self.update_label()
    
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)
      
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression=str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()
         
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)
             
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(fill="both", expand=True)
        return frame
       
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression)  
     
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
