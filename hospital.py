class HospitalAppointment:

    def __init__(self):
        self.available_doctors = ["Dr. Smith", "Dr. John", "Dr. Priya"]

    def book_appointment(self, patient_name, doctor_name):
        if doctor_name in self.available_doctors:
            print("Appointment Confirmed!")
            print("Patient Name:", patient_name)
            print("Doctor Name:", doctor_name)
        else:
            print("Doctor is unavailable. Please try another doctor.")


hospital = HospitalAppointment()

hospital.book_appointment("Patient1", "Dr. Priya")
hospital.book_appointment("Patient2", "Dr. Arun")