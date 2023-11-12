import qrcode
from tkinter import *
from tkinter import messagebox

def generate_qr_code(data):
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
    messagebox.showinfo("QR Code Generated", "Patient details saved and QR code generated.")

def get_patient_details():
    root = Tk()
    root.title("Patient Details Entry")

    # Create variables to store entry values
    name_var = StringVar()
    age_var = StringVar()
    dob_var = StringVar()
    gender_var = StringVar()
    allergies_var = StringVar()
    symptoms_var = StringVar()
    disease_history_var = StringVar()
    temperature_var = StringVar()
    pulse_rate_var = StringVar()
    respiration_rate_var = StringVar()
    blood_pressure_var = StringVar()
    blood_oxygen_var = StringVar()
    weight_var = StringVar()
    blood_glucose_var = StringVar()

    # Function to save details and generate QR code
    def save_and_generate_qr():
        patient_details = {
            "Name": name_var.get(),
            "Age": age_var.get(),
            "Date of Birth": dob_var.get(),
            "Gender": gender_var.get(),
            "Allergies": allergies_var.get(),
            "Current Symptoms": symptoms_var.get(),
            "Disease History": disease_history_var.get(),
            "Body Temperature": temperature_var.get(),
            "Pulse Rate": pulse_rate_var.get(),
            "Respiration Rate": respiration_rate_var.get(),
            "Blood Pressure": blood_pressure_var.get(),
            "Blood Oxygen": blood_oxygen_var.get(),
            "Weight": weight_var.get(),
            "Blood Glucose Level": blood_glucose_var.get(),
        }

        # Save patient details to a file
        with open("patient_details.txt", "w") as file:
            for key, value in patient_details.items():
                file.write(f"{key}: {value}\n")

        # Generate QR code with a link to the webpage
        webpage_url = "http://192.168.1.108:5000/patient_details"
        generate_qr_code(webpage_url)

        root.destroy()

    # GUI for data entry
    Label(root, text="Name:").grid(row=0, column=0)
    Entry(root, textvariable=name_var).grid(row=0, column=1)
    
    Label(root, text="Age:").grid(row=1, column=0)
    Entry(root, textvariable=age_var).grid(row=1, column=1)
    
    Label(root, text="Date of Birth (dd-mm-yyyy):").grid(row=2, column=0)
    Entry(root, textvariable=dob_var).grid(row=2, column=1)
    
    Label(root, text="Gender:").grid(row=3, column=0)
    Entry(root, textvariable=gender_var).grid(row=3, column=1)
    
    Label(root, text="Allergies:").grid(row=4, column=0)
    Entry(root, textvariable=allergies_var).grid(row=4, column=1)
    
    Label(root, text="Current Symptoms:").grid(row=5, column=0)
    Entry(root, textvariable=symptoms_var).grid(row=5, column=1)
    
    Label(root, text="Disease History:").grid(row=6, column=0)
    Entry(root, textvariable=disease_history_var).grid(row=6, column=1)
    
    Label(root, text="Body Temperature:").grid(row=7, column=0)
    Entry(root, textvariable=temperature_var).grid(row=7, column=1)
    
    Label(root, text="Pulse Rate:").grid(row=8, column=0)
    Entry(root, textvariable=pulse_rate_var).grid(row=8, column=1)
    
    Label(root, text="Respiration Rate:").grid(row=9, column=0)
    Entry(root, textvariable=respiration_rate_var).grid(row=9, column=1)
    
    Label(root, text="Blood Pressure:").grid(row=10, column=0)
    Entry(root, textvariable=blood_pressure_var).grid(row=10, column=1)
    
    Label(root, text="Blood Oxygen:").grid(row=11, column=0)
    Entry(root, textvariable=blood_oxygen_var).grid(row=11, column=1)
    
    Label(root, text="Weight:").grid(row=12, column=0)
    Entry(root, textvariable=weight_var).grid(row=12, column=1)
    
    Label(root, text="Blood Glucose Level:").grid(row=13, column=0)
    Entry(root, textvariable=blood_glucose_var).grid(row=13, column=1)

    Button(root, text="Save and Generate QR Code", command=save_and_generate_qr).grid(row=14, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    get_patient_details()
