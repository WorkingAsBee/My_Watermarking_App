import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

BACKGROUND_COLOR = "#EAF6F6"
AZUR = "#66BFBF"
PINK = "#FF0063"


def upload_file():
    global img
    global image
    global file
    global image_for_canvas

    file_types = [('Jpg files', '*.jpg')]
    file = filedialog.askopenfilename(title="Select an Image", filetypes=file_types)
    fixed_height = 300
    image = Image.open(file)
    if image.mode != "RGB":
        image = image.convert("RGB")
    height_percent = fixed_height / float(image.height)
    width_size = int((float(image.width) * float(height_percent)))
    image = image.resize((width_size, fixed_height))

    img = ImageTk.PhotoImage(image)
    image_for_canvas = canvas.create_image(300, 150, image=img)
    return image_for_canvas


def add_watermark():
    global img_with_wm
    global new_image_for_canvas
    print(image.size) #300/300
    # Get Watermark Text
    wm_text = entry_for_watermark.get()
    # Draw on Image
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Arial.ttf', 26)
    # Coordinates Where Text Goes
    x, y = int(image.width/2), int(image.height/2)
    # Add Watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_fill='#222', anchor='ms')

    img_with_wm = ImageTk.PhotoImage(image)
    new_image_for_canvas = canvas.itemconfig(image_for_canvas, image=img_with_wm)
    return new_image_for_canvas


def save_image():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    image.save(filename)


window = Tk()
window.title("My Watermark App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

welcome_label = tkinter.Label(text="Welcome to Watermarking App", fg=AZUR, font=('Courier', 32, 'bold'), bg=BACKGROUND_COLOR)
welcome_label.grid(row=0, column=0, pady=20)

upload_button = Button(text="Upload Your Image", fg=AZUR, highlightbackground=BACKGROUND_COLOR, command=upload_file)
upload_button.grid(column=0, row=1)

canvas = Canvas(window, height=300, width=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=2, pady=30)

add_wm_text_label = tkinter.Label(text="Add Watermark Text", fg=AZUR, font=('Courier', 18), bg=BACKGROUND_COLOR)
add_wm_text_label.grid(row=3, column=0)

entry_for_watermark = Entry(width=30, bg='white', border=1, highlightthickness=0)
entry_for_watermark.config(insertbackground=PINK, foreground=PINK)
entry_for_watermark.focus()
entry_for_watermark.grid(column=0, row=4, pady=20)

add_watermark_button = tkinter.Button(text="Add Watermark", fg=AZUR, highlightbackground=BACKGROUND_COLOR, command=lambda: add_watermark())
add_watermark_button.grid(column=0, row=5, pady=10)

save_image_button = tkinter.Button(text="Save Your Image", fg=AZUR, highlightbackground=BACKGROUND_COLOR, command=save_image)
save_image_button.grid(column=0, row=6, pady=10)

window.mainloop()