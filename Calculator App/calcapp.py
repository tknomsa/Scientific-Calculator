import tkinter as tk
from tkinter import *
import math
import threading


class Calculator(object):
    def __init__(self, window):
        # Creating the main window
        self.window = window
        self.window.geometry("430x435")
        self.window.title("Simple Scientific Calculator")
        self.window.config(background='grey')
        self.window.resizable(0, 0)
        self.window.bind('<Return>', lambda event: self.equal_button.invoke())

        # Creating the output frame
        self.output_frame = tk.Frame(self.window, padx=6, pady=6)
        self.output_frame.config(background='white')
        self.output_frame.pack(pady=10)

        # Formatting Screen
        self.screen_label = tk.Entry(self.output_frame)
        self.screen_label.config(background='wheat', width=40, relief=SUNKEN, bd=10, justify=LEFT)
        self.screen_label.grid(row=0, column=0, padx=5, pady=5)
        self.screen_label.insert(0, '')

        # Creating the scientific input frame
        self.scientific_input_frame = tk.Frame(self.window, padx=11, pady=8)
        self.scientific_input_frame.config(background='white')
        self.scientific_input_frame.pack(pady=2)

        # Creating the button for fraction separation
        self.fraction_separator_button = tk.Button(self.scientific_input_frame, text='/',
                                                   command=lambda: self.multithread('/'))
        self.fraction_separator_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.fraction_separator_button.grid(row=0, column=0)

        # Creating the square root button
        self.square_root_button = tk.Button(self.scientific_input_frame, text='√',
                                            command=lambda: self.multithread('√'))
        self.square_root_button.config(background='wheat', width=3, height=1, relief=RAISED)
        self.square_root_button.grid(row=0, column=1)

        # Creating the square button
        self.square_button = tk.Button(self.scientific_input_frame, text='x\u00B2',
                                       command=lambda: self.multithread('x\u00B2'))  # square operator
        self.square_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.square_button.grid(row=0, column=2)

        # Creating the Sine angle button
        self.sin_angle_button = tk.Button(self.scientific_input_frame, text='sinθ',
                                          command=lambda: self.multithread('sinθ'))
        self.sin_angle_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.sin_angle_button.grid(row=0, column=5)

        # Creating the Tangent angle button
        self.tan_angle_button = tk.Button(self.scientific_input_frame, text='tanθ',
                                          command=lambda: self.multithread('tanθ'))
        self.tan_angle_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.tan_angle_button.grid(row=0, column=4)

        # Creating the Cosine angle button
        self.cos_angle_button = tk.Button(self.scientific_input_frame, text='cosθ',
                                          command=lambda: self.multithread('cosθ'))
        self.cos_angle_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.cos_angle_button.grid(row=0, column=3)

        # Creating the negative sign button
        self.negative_sign_button = tk.Button(self.scientific_input_frame, text='(-)',
                                              command=lambda: self.click('-'))
        self.negative_sign_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.negative_sign_button.grid(row=1, column=0)

        # creating two PI button
        self.two_pi_button = tk.Button(self.scientific_input_frame, text='2π', command=lambda: self.multithread('2π'))
        self.two_pi_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.two_pi_button.grid(row=2, column=2)

        # Creating Cosine line button
        self.cos_line_button = tk.Button(self.scientific_input_frame, text='cosh',
                                         command=lambda: self.multithread('cosh'))
        self.cos_line_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.cos_line_button.grid(row=2, column=3)

        # Creating Tangent line button
        self.tangent_line_button = tk.Button(self.scientific_input_frame, text='tanh',
                                             command=lambda: self.multithread('tanh'))
        self.tangent_line_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.tangent_line_button.grid(row=1, column=4)

        # Creating Sine line button
        self.sin_line_button = tk.Button(self.scientific_input_frame, text='sinh',
                                         command=lambda: self.multithread('sinh'))
        self.sin_line_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.sin_line_button.grid(row=1, column=5)

        # Creating Degree button
        self.degree_button = tk.Button(self.scientific_input_frame, text='Deg',
                                       command=lambda: self.multithread('Deg'))
        self.degree_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.degree_button.grid(row=2, column=0)

        # Creating Radian buttonS
        self.radian_button = tk.Button(self.scientific_input_frame, text='Rad',
                                       command=lambda: self.multithread('Rad'))
        self.radian_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.radian_button.grid(row=2, column=1)

        # Creating Natural Log button
        self.log_button = tk.Button(self.scientific_input_frame, text='log',
                                    command=lambda: self.multithread('log'))
        self.log_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.log_button.grid(row=2, column=4)

        # Creating E to a power button
        self.natural_log_button = tk.Button(self.scientific_input_frame, text='ln',
                                            command=lambda: self.multithread('ln'))
        self.natural_log_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.natural_log_button.grid(row=2, column=5)

        # Creating Factorial button
        self.factorial_button = tk.Button(self.scientific_input_frame, text='x!',
                                          command=lambda: self.multithread('!'))
        self.factorial_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.factorial_button.grid(row=1, column=1)

        # Creating PI button
        self.PI_button = tk.Button(self.scientific_input_frame, text='π', command=lambda: self.multithread('π'))
        self.PI_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.PI_button.grid(row=1, column=2)

        # Creating E button
        self.e_button = tk.Button(self.scientific_input_frame, text='e',
                                  command=lambda: self.multithread('e'))
        self.e_button.config(background='wheat', width=4, height=1, relief=RAISED)
        self.e_button.grid(row=1, column=3)

        # Formatting- Scientific frame
        for button in self.scientific_input_frame.winfo_children():
            button.grid_configure(padx=3, pady=3)

        # Formatting frame for Standard Input
        self.standard_input_frame = tk.Frame(self.window, padx=10.5, pady=5)
        self.standard_input_frame.config(background='white')
        self.standard_input_frame.pack(pady=0)

        # Creating Seven button
        self.seven_button = tk.Button(self.standard_input_frame, text='7', command=lambda: self.click('7'))
        self.seven_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.seven_button.grid(row=0, column=0)

        # Creating Eight button
        self.eight_button = tk.Button(self.standard_input_frame, text='8', command=lambda: self.click('8'))
        self.eight_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.eight_button.grid(row=0, column=1)

        # Creating Nine button
        self.nine_button = tk.Button(self.standard_input_frame, text='9', command=lambda: self.click('9'))
        self.nine_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.nine_button.grid(row=0, column=2)

        #  Creating Delete button
        self.delete_button = tk.Button(self.standard_input_frame, text='DEL', command=lambda: self.multithread('Del'))
        self.delete_button.config(background='#C0C0C0', width=5, height=2, relief=RAISED)
        self.delete_button.grid(row=0, column=3)

        # Creating Clear button
        self.clear_button = tk.Button(self.standard_input_frame, text='AC', command=lambda: self.multithread('AC'))
        self.clear_button.config(background='#C0C0C0', width=5, height=2, relief=RAISED)
        self.clear_button.grid(row=0, column=4)

        # Creating Four button
        self.four_button = tk.Button(self.standard_input_frame, text='4', command=lambda: self.click('4'))
        self.four_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.four_button.grid(row=1, column=0)

        # Creating Five button
        self.five_button = tk.Button(self.standard_input_frame, text='5', command=lambda: self.click('5'))
        self.five_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.five_button.grid(row=1, column=1)

        # Creating Six button
        self.six_button = tk.Button(self.standard_input_frame, text='6', command=lambda: self.click('6'))
        self.six_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.six_button.grid(row=1, column=2)

        # Creating Multiplication button
        self.multiplication_button = tk.Button(self.standard_input_frame, text='x', command=lambda: self.click('*'))
        self.multiplication_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.multiplication_button.grid(row=1, column=3)

        # Creating Division button
        self.division_button = tk.Button(self.standard_input_frame, text='÷', command=lambda: self.click('/'))
        self.division_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.division_button.grid(row=1, column=4)

        # Creating One button
        self.one_button = tk.Button(self.standard_input_frame, text='1', command=lambda: self.click('1'))
        self.one_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.one_button.grid(row=2, column=0)

        # Creating Two button
        self.two_button = tk.Button(self.standard_input_frame, text='2', command=lambda: self.click('2'))
        self.two_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.two_button.grid(row=2, column=1)

        # Creating Three button
        self.three_button = tk.Button(self.standard_input_frame, text='3', command=lambda: self.click('3'))
        self.three_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.three_button.grid(row=2, column=2)

        # Creating Addition button
        self.addition_button = tk.Button(self.standard_input_frame, text='+', command=lambda: self.click('+'))
        self.addition_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.addition_button.grid(row=2, column=3)

        # Creating Subtraction button
        self.subtraction_button = tk.Button(self.standard_input_frame, text='-', command=lambda: self.click('-'))
        self.subtraction_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.subtraction_button.grid(row=2, column=4)

        # Creating Zero button
        self.zero_button = tk.Button(self.standard_input_frame, text='0', command=lambda: self.click('0'))
        self.zero_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.zero_button.grid(row=3, column=0)

        # Creating Point button
        self.point_button = tk.Button(self.standard_input_frame, text='.', command=lambda: self.click('.'))
        self.point_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.point_button.grid(row=3, column=1)

        # Creating Exponential button
        self.exponential_button = tk.Button(self.standard_input_frame, text='EXP',
                                            command=lambda: self.multithread('* 10 ^'))
        self.exponential_button.config(background='burlywood', width=5, height=2, relief=RAISED)
        self.exponential_button.grid(row=3, column=2)

        # Creating Answer button
        self.answer_button = tk.Button(self.standard_input_frame, text='Ans', command=lambda: self.multithread('Ans'))
        self.answer_button.config(background='#C0C0C0', width=5, height=2, relief=RAISED)
        self.answer_button.grid(row=3, column=3)

        # Creating Equal button
        self.equal_button = tk.Button(self.standard_input_frame, text='=', command=lambda: self.click('='))
        self.equal_button.config(background='#C0C0C0', width=5, height=2, relief=RAISED)
        self.equal_button.grid(row=3, column=4)

        # Formatting- Standard  frame
        for button in self.standard_input_frame.winfo_children():
            button.grid_configure(padx=3, pady=3)

    """" This method reads user input and carries out respective functions
    based on the input using the if, elif and else conditions nested within
    a try and except block"""

    def click(self, figure):
        Answers = []
        ex = self.screen_label.get()
        answer = ""
        try:
            if figure == 'Del':
                ex = self.screen_label.get()
                ex = ex[0:len(ex) - 1]
                self.screen_label.delete(0, END)
                self.screen_label.insert(0, ex)
                return

            elif figure == 'AC':
                self.screen_label.delete(0, END)

            elif figure == '√':
                answer = math.sqrt(eval(ex))
                Answers.append(answer)

            elif figure == 'π':
                answer = math.pi
                Answers.append(answer)

            elif figure == 'sinθ':
                answer = math.sin(math.radians(eval(ex)))
                Answers.append(answer)

            elif figure == 'tanθ':
                answer = math.tan(math.radians(eval(ex)))
                Answers.append(answer)

            elif figure == 'cosθ':
                answer = math.cos(math.radians(eval(ex)))
                Answers.append(answer)

            elif figure == 'sinh':
                answer = math.sinh(eval(ex))
                Answers.append(answer)

            elif figure == 'tanh':
                answer = math.tanh(eval(ex))
                Answers.append(answer)

            elif figure == 'cosh':
                answer = math.cosh(eval(ex))
                Answers.append(answer)

            # Displays an entered value to the power of two (square operator)
            elif figure == 'x\u00B2':
                answer = eval(ex) ** 2
                Answers.append(answer)

            elif figure == '2π':
                answer = 2 * math.pi
                Answers.append(answer)

            elif figure == 'Deg':
                answer = math.degrees(eval(ex))
                Answers.append(answer)

            elif figure == 'Rad':
                answer = math.radians(eval(ex))
                Answers.append(answer)

            elif figure == 'e':
                answer = math.e
                Answers.append(answer)

            elif figure == 'log':
                answer = math.log10(eval(ex))
                Answers.append(answer)

            elif figure == 'ln':
                answer = math.log2(eval(ex))
                Answers.append(answer)

            elif figure == '!':
                answer = math.factorial(eval(ex))
                Answers.append(answer)

            elif figure == '/':
                self.screen_label.insert(END, '/')
                return

            elif figure == '=':
                try:
                    answer = eval(ex)
                    Answers.append(answer)

                except ZeroDivisionError:
                    self.screen_label.delete(0, END)
                    self.screen_label.insert(END, 'Math Error')
                    return

            elif figure == 'Ans':
                self.screen_label.insert(END, Answers[-1])
                return

            else:
                self.screen_label.insert(END, figure)
                return

            self.screen_label.delete(0, END)
            self.screen_label.insert(0, answer)

        # Bringing up current exceptions
        except ValueError:
            self.screen_label.delete(0, END)
            self.screen_label.insert(END, 'Please Be Serious')
            return

        except SyntaxError:
            self.screen_label.delete(0, END)
            self.screen_label.insert(END, 'Syntax Error')
            return

        except NameError:
            self.screen_label.delete(0, END)
            self.screen_label.insert(END, 'Maybe try using numbers? Thx')
            return

    """" This method allows  the implementation on multithreading
    on some functions in the click method """

    def multithread(self, figure):
        thread = threading.Thread(target=self.click, args=(figure,))
        thread.start()


root = tk.Tk()
calc = Calculator(root)
root.mainloop()