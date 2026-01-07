import tkinter as tk
from tkinter import messagebox

from ec.edu.espe.schoolsystem.controller.student_controller import StudentController


class FrmStudent:

    def __init__(self):
        self.controller = StudentController()

        self.window = tk.Tk()
        self.window.title("School System")
        self.window.geometry("300x220")
        self.window.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        # Title
        lbl_title = tk.Label(self.window, text="School System", font=("Arial", 14))
        lbl_title.pack(pady=10)

        # ID
        tk.Label(self.window, text="ID:").pack()
        self.txt_id = tk.Entry(self.window)
        self.txt_id.pack()

        # Name
        tk.Label(self.window, text="Name:").pack()
        self.txt_name = tk.Entry(self.window)
        self.txt_name.pack()

        # Pension
        tk.Label(self.window, text="Pension:").pack()
        self.txt_pension = tk.Entry(self.window)
        self.txt_pension.pack()

        # Button
        btn_register = tk.Button(
            self.window,
            text="Register",
            command=self.register_student
        )
        btn_register.pack(pady=15)

    def register_student(self):
        try:
            student_id = int(self.txt_id.get())
            name = self.txt_name.get()
            pension = float(self.txt_pension.get())

            self.controller.create_student(student_id, name, pension)

            messagebox.showinfo("Success", "Student saved")
            self._clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid data")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _clear_fields(self):
        self.txt_id.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.txt_pension.delete(0, tk.END)

    def run(self):
        self.window.mainloop()
