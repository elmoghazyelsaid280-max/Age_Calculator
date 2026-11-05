from tkinter import  Tk, Label, Entry, Button, END
window = Tk()
window.title("Welcome to Quick Age Calculator")
window.geometry("600x600")
window.configure(bg="lightblue")
def Calculate_age():
    try:
        birth_year = int(age.get())
        current_year = 2026
        if birth_year > current_year or birth_year < 1900:
            result.config(text="Please enter a valid year")
            age.delete(0, END)
        else:
            age_value = current_year - birth_year
            result.config(text=f"Your Age is: {age_value}")
    except ValueError:
        result.config(text="Please enter numeric value")
        age.delete(0, END)

label=Label(window , text ="Enter your Birth Year ", font=("Arial",20,"bold"),bg="#a8b5c3",fg="#130c9b")
label.pack(pady=10)
age = Entry (window, width =25 ,font=("Arial",16),bg="white",fg="black")
age.pack(pady=10)
button=Button(window , text ="calculate age" , font=("Arial",16), command=Calculate_age,bg="#A9A2BB",fg="#FF0000")
button.pack (pady=10)
result=Label(window , text ="Your Age is :", font=("Arial",16),bg="#C6C4DF",fg="#0300a0")
result.pack(pady=10)

window.mainloop()