from tkinter import*

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title = "Flashy"
window.config(padx=60, pady=60, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="C:/Users/ankit/PycharmProjects/flash_card/images/card_front.png")
back_card = PhotoImage(file="C:/Users/ankit/PycharmProjects/flash_card/images/card_back.png")
right_sign = PhotoImage(file="C:/Users/ankit/PycharmProjects/flash_card/images/right.png")
wrong_sign = PhotoImage(file="C:/Users/ankit/PycharmProjects/flash_card/images/wrong.png")

canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title")
canvas.create_text(400, 300, text="Word")

right_button = Button(image=right_sign, highlightthickness=0)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_sign, highlightthickness=0)
wrong_button.grid(column=1, row=1)

window.mainloop()