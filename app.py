from tkinter import *
from tkinter import simpledialog, filedialog


# Create main window
root = Tk()
root.title("17330118 - Mustafa Guner")
root.resizable(False, False)
root.geometry("800x500")


leftSection = Frame(width=300, height=600, bg="#267DFF")
leftSection.pack(side=LEFT, fill="both", expand=False)

introductionTitle = Label(
    leftSection, text="Welcome to Python GUI App!", fg="#fff", bg="#267DFF", font=("arial", 15, "bold"))
introductionTitle.pack(padx=30,  pady=(90, 10))

introductionDescription = Label(
    leftSection, wraplengt=280, font=("arial", 11), fg="#fff", bg="#267DFF", text="By using this app, you can display your input and save as your input as a text file to read in the future! Enjoy while using it!", justify=LEFT)
introductionDescription.pack(padx=10)

howToUserTItle = Label(
    leftSection, text="How To Use?", fg="#fff", bg="#267DFF", font=("arial", 15, "bold"))
howToUserTItle.pack(padx=30,  pady=(30, 10), anchor="w")

howToUseInstructions = introductionDescription = Label(
    leftSection, wraplengt=280, font=("arial", 11), fg="#fff", bg="#267DFF", text="Click on the input button and enter your input. You will see it is going to be displayed in the UI. Then you can save it as a file by clicking the next button.", justify=LEFT)
introductionDescription.pack(padx=10)

rightSection = Frame(width=300, height=600, bg="#FCFCFC")

# Create label and button


title = Label(root, text="Output:",
              fg="#52538A", font=("arial", 15, "bold"))
title.pack(pady=(30, 10), padx=(90, 0), anchor="w")

label = Label(root, fg="#52538A", font=("arial", 12, "bold"))
label.pack(pady=(30, 10), padx=(90, 0), anchor="w")


def clickOnInputBtn():
    # Display message box with input field
    message = simpledialog.askstring("Input", "Enter a message:")
    # Update label with user's input
    label.config(text=message, wraplength=400)


leftButtonContainer = Frame(width=100, height=200)
leftButtonContainer.pack(side=LEFT, fill="y", expand=False, padx=(90, 0))


button = Button(leftButtonContainer, text="Enter your input",
                command=clickOnInputBtn, padx=10, pady=10,  wraplengt=100, font=("arial", 9))

button.pack()

# Create button to save message to text file


def saveInputOnClick():
    # Open save file dialog
    save_file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    # Write message to file
    save_file.write(label.cget("text"))
    save_file.close()


rightButtonContainer = Frame(width=100, height=50)
rightButtonContainer.pack(side=RIGHT, fill="y", expand=False, padx=(0, 90))


saveButton = Button(rightButtonContainer, text="Save message as file", padx=10, pady=10,
                    font=("arial", 9, "bold"), bg="#267DFF", fg="#fff",
                    command=saveInputOnClick)


saveButton.pack()

root.mainloop()
