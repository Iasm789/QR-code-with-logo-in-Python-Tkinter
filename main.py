import qrcode
import PIL.Image
from tkinter import *

ws = Tk()
ws.title('QR generation_iasm')
ws.geometry('400x300')
ws.config(bg='#f25252')

logo = PIL.Image.open('Frame 91.png')


def generate_qr():
    global logo
    basic = 150
    width_percentage = (basic / float(logo.size[0]))
    height_size = int((float(logo.size[1]) * float(width_percentage)))
    logo = logo.resize((basic, height_size), PIL.Image.ANTIALIAS)
    qrc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qrc.add_data(msg.get())
    qrc.make()
    gen_img = qrc.make_image(
        fill_color='#000000',
        bg_color="#fff"
    ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2,
                (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    gen_img.save(save_name.get() + '.png')

    lbl.config(text='File saved with logo')


frame = Frame(ws, bg='#f25252')
frame.pack(expand=True)

Label(frame, text='Enter URL ', bg='#f25252').grid(row=0, column=0)
msg = Entry(frame)
msg.grid(row=0, column=1)

Label(frame, text='File Name', bg='#f25252').grid(row=1, column=0)
save_name = Entry(frame)
save_name.grid(row=1, column=1)

btn = Button(
    frame,
    text='Generate',
    command=generate_qr
)
btn.grid(row=2, columnspan=3, pady=10)

lbl = Label(ws, fg='black', bg='#f25252')
lbl.pack()

ws.mainloop()
