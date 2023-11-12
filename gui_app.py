import subprocess
import qrcode
from tkinter import *
from PIL import Image, ImageTk

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Medical Application")

        # Button to start doctor_webpage.py
        self.doctor_button = Button(master, text="START", command=self.start_doctor_webpage)
        self.doctor_button.pack(pady=10)

        # Button to start ambulance.py
        self.ambulance_button = Button(master, text="DATA ENTRY", command=self.start_ambulance_with_qr)
        self.ambulance_button.pack(pady=10)

        # Placeholder image for QR code
        self.placeholder_image = ImageTk.PhotoImage(Image.new("RGB", (100, 100), "white"))
        self.qr_label = Label(master, image=self.placeholder_image)
        self.qr_label.pack()

    def start_doctor_webpage(self):
        subprocess.Popen(["python", "doctor_webpage.py"])

    def start_ambulance_with_qr(self):
        subprocess.Popen(["python", "ambulance.py"])
        qr_image = self.generate_qr_code("http://192.168.1.108:5000/patient_details")
        self.qr_label.configure(image=qr_image)
        self.qr_label.image = qr_image

    def generate_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("patient_qr.png")
        return ImageTk.PhotoImage(Image.open("patient_qr.png"))

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
