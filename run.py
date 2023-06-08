import customtkinter as ctk
from tkinter import messagebox
import smtplib
import validators
import random
# import tkinter as tk

root = ctk.CTk()
root.geometry("300x300")
root.resizable(False, False)
ctk.set_appearance_mode("light")


def dark():
    ctk.set_appearance_mode("dark")


def light():
    ctk.set_appearance_mode("light")


dark_mode_button = ctk.CTkButton(
    root, text="Dark Mode", width=30, height=20, fg_color="black", command=dark)
dark_mode_button.place(x=140, y=5)
light_mode_button = ctk.CTkButton(
    root, text="Light Mode", width=30, height=20, command=light)
light_mode_button.place(x=220, y=5)
# Email Label
email_label = ctk.CTkLabel(
    root, text="Enter Valid Email", font=("sans serif", 15))
email_label.place(x=105, y=40)
# Email entry box
email_entry_box = ctk.CTkEntry(
    root, placeholder_text="Enter Valid Email", width=160)
email_entry_box.place(x=80, y=65)
# Send Otp Callback Function


def send_otp():
    entered_email = email_entry_box.get()
    # To check wheather the entered email address is valid or not
    isValid = validators.email(entered_email)
    if isValid:
        try:
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.ehlo()
            connection.starttls()  # Standard Encryption
            sender_email_address = "example@gmail.com"
            sender_email_password = "yourpasswordhere"
            connection.login(sender_email_address, sender_email_password)
            # List Comprehension to generate random number for otp
            otp = ''.join([str(random.randrange(0, 9, 1)) for i in range(4)])
            connection.sendmail(
                "ilovepython46@gmail.com", f"{entered_email}", f"Subject: Regarding OTP \n\nYour One time Password is {otp}\nDo not share it with others\nif you have not requested for otp ignore it.")
        except:
            messagebox.showerror("Error", "Failed to Send Email")
        else:
            send_otp_button.destroy()
            otp_entry_field = ctk.CTkEntry(
                root, placeholder_text="Enter OTP", width=160)
            otp_entry_field.place(x=80, y=100)
            # Verify Call Back Function

            def verify():
                otp_generated_by_system = otp
                otp_entered_by_user = otp_entry_field.get()
                if otp_entered_by_user == otp_generated_by_system:
                    messagebox.showinfo("Verified", "OTP Verified")
                    root.destroy()
                else:
                    messagebox.showerror(
                        "Failed", "Falied to Verify OTP Wrong OTP")
                    otp_entry_field.delete(0, ctk.END)
            verify_button = ctk.CTkButton(
                root, text="Verify OTP", width=160, command=verify)
            verify_button.place(x=80, y=140)
    else:
        messagebox.showerror(
            "Invalid Email", "Please Provide a Valid Email Address")


# send otp button
send_otp_button = ctk.CTkButton(
    root, text="Send OTP", width=160, command=send_otp)
send_otp_button.place(x=80, y=100)
root.mainloop()
