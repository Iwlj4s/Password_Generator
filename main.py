import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as CTk
from PIL import Image

import random
import password_gen


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Settings --- #
        self.geometry("500x550")
        self.title(" --- Password Generator --- ")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("logo.png"), size=(500, 129))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)


class AppWidgets(App):
    def __init__(self):
        super().__init__()

        # --- Password Entry Frame --- #
        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        # --- Password Entry --- #
        self.password_entry = CTk.CTkEntry(master=self.password_frame, width=330, height=90)
        self.password_entry.grid(row=0, column=0, padx=(20, 20), pady=(35, 35))

        # -- Button For Generate Password --- #

        self.button_for_gen_password = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                                     command=self.get_password)
        self.button_for_gen_password.grid(row=0, column=1)

        # --- Password Settings Frame --- #
        self.password_settings_frame = CTk.CTkFrame(master=self)
        self.password_settings_frame.grid(row=2, column=0, padx=(15, 25), pady=(20, 0), sticky="nsew")

        # --- Slider For Length Password --- #
        self.password_length_slider = CTk.CTkSlider(master=self.password_settings_frame, from_=0, to=50,
                                                    number_of_steps=100, command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.password_settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        # --- Check Boxes --- #
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.password_settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10, pady=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.password_settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1, padx=10, pady=10)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.password_settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2, padx=10, pady=10)

        self.cb_punctuation_var = tkinter.StringVar()
        self.cb_punctuation = CTk.CTkCheckBox(master=self.password_settings_frame, text="!#$@",
                                              variable=self.cb_punctuation_var, onvalue=punctuation, offvalue="")
        self.cb_punctuation.grid(row=2, column=3, padx=10, pady=10)

    def get_characters(self):
        char = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() +
                       self.cb_upper_var.get() + self.cb_punctuation_var.get())

        characters = list(char)
        random.shuffle(characters)

        return characters

    def get_password(self):
        pass

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))


if __name__ == '__main__':
    app = AppWidgets()
    app.mainloop()
