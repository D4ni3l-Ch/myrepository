
# FIX PARA EJECUTAR DESDE VIEW 
import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../..")
)


sys.path.append(ROOT_DIR)



import tkinter as tk                          
from tkinter import messagebox, ttk           

# Importación del controlador (MVC)
from ec.edu.espe.schoolsystem.controller.student_controller import StudentController



# VISTA PRINCIPAL (VIEW)

class StudentForm(tk.Tk):

    def __init__(self):
        super().__init__()

        # Se crea una instancia del controlador
        
        self.controller = StudentController()

        # Configuración básica de la ventana
        self.title("School System - Students")
        self.geometry("560x430")
        self.resizable(False, False)

        # Se crean los componentes gráficos
        self.create_widgets()

        # Se cargan los datos de la base en la tabla
        self.load_table()

    
    # UI
    
    def create_widgets(self):

        # ---------- CAMPOS DE ENTRADA ----------
        tk.Label(self, text="Name:").place(x=30, y=30)
        self.txt_name = tk.Entry(self)
        self.txt_name.place(x=120, y=30)

        tk.Label(self, text="Grade:").place(x=30, y=70)
        self.txt_grade = tk.Entry(self)
        self.txt_grade.place(x=120, y=70)

        tk.Label(self, text="Tuition:").place(x=30, y=110)
        self.txt_tuition = tk.Entry(self)
        self.txt_tuition.place(x=120, y=110)

        # ---------- BOTONES ----------
        # Cada botón llama a un método de la vista
        tk.Button(self, text="Add", width=10,
                  command=self.add_student).place(x=30, y=150)

        tk.Button(self, text="Delete", width=10,
                  command=self.delete_student).place(x=140, y=150)

        tk.Button(self, text="Total Income", width=15,
                  command=self.show_total).place(x=250, y=150)

        
        # TABLA (TREEVIEW)
        # Se usa Treeview para mostrar los estudiantes
        # Incluye ID entero autoincremental
        
        self.table = ttk.Treeview(
            self,
            columns=("id", "name", "grade", "tuition"),
            show="headings",        # Oculta la columna fantasma
            height=10
        )

        # Encabezados de la tabla
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("grade", text="Grade")
        self.table.heading("tuition", text="Tuition")

        # Ancho y alineación de columnas
        self.table.column("id", width=60, anchor="center")
        self.table.column("name", width=150)
        self.table.column("grade", width=80)
        self.table.column("tuition", width=80)

        self.table.place(x=30, y=200)

    
    # ACCIONES DE LOS BOTONES
    
    def add_student(self):
        """
        Registra un estudiante en MongoDB
        """
        try:
            name = self.txt_name.get()
            grade = self.txt_grade.get()
            tuition = float(self.txt_tuition.get())

            # Validación básica
            if not name or not grade:
                messagebox.showwarning("Warning", "All fields are required")
                return

            # Se delega la creación al controlador
            self.controller.create_student(name, grade, tuition)

            # Se actualiza la tabla
            self.load_table()

            # Se limpian los campos
            self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid tuition value")

    def delete_student(self):

        """
        Elimina el estudiante seleccionado usando su ID
        """
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a student to delete")
            return

        # Se obtiene el ID desde la tabla (columna 0)
        student_id = self.table.item(selected[0])["values"][0]

        # Eliminación delegada al controlador
        self.controller.delete_student(student_id)

        # Se refresca la tabla
        self.load_table()

    def show_total(self):
        """
        Calcula y muestra el total de pensiones
        """
        total = self.controller.calculate_total_income()
        messagebox.showinfo("Total Income", f"Total income: ${total:.2f}")

    
    # MANEJO DE LA TABLA
    # Limpia la tabla y vuelve a cargar los datos desde MongoDB

    def load_table(self):
        
        # Se eliminan filas anteriores
        for row in self.table.get_children():
            self.table.delete(row)

        # Se cargan los estudiantes desde el controlador
        for student in self.controller.get_all_students():
            self.table.insert(
                "",
                tk.END,
                values=(student.id, student.name, student.grade, student.tuition)
            )

    
    # Limpia los campos de entrada
      
    def clear_fields(self):
        
        self.txt_name.delete(0, tk.END)
        self.txt_grade.delete(0, tk.END)
        self.txt_tuition.delete(0, tk.END)



# PUNTO DE ENTRADA DEL PROGRAMA
# Permite ejecutar directamente desde la vista

if __name__ == "__main__":
    app = StudentForm()
    app.mainloop()
