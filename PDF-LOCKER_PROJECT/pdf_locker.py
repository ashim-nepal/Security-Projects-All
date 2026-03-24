import tkinter as tk
from tkinter import filedialog, messagebox
import pikepdf
import os

class PDFLockerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Password Locker")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        tk.Label(
            root, text="Password-Protected PDF Locker",
            font=("Helvetica", 14, "bold")
        ).pack(pady=10)

        self.select_btn = tk.Button(root, text="Select PDF File", command=self.select_file)
        self.select_btn.pack(pady=10)

        self.file_label = tk.Label(root, text="No file selected", fg="red")
        self.file_label.pack()

        tk.Label(root, text="Enter password to lock PDF:").pack(pady=(15, 0))
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack()

        self.lock_btn = tk.Button(root, text="Lock PDF", command=self.lock_pdf)
        self.lock_btn.pack(pady=20)

        self.file_path = None

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=os.path.basename(file_path), fg="green")
        else:
            self.file_label.config(text="No file selected", fg="red")

    def check_password(self, password):
        return(len(password)>=9 and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password))

    def lock_pdf(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a PDF file first.")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return

        if not self.check_password(password):
            messagebox.showwarning(
                    "Weak Password",
                    """Password must,\n
                    -Be of atleast 9 characters\n
                    -Contain at least one uppercase letter
                    -Contain at least one number""")
            return

        save_path = filedialog.asksaveasfilename(
            title="Save Locked PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=f"locked_{os.path.basename(self.file_path)}"
        )

        if not save_path:
            messagebox.showwarning("Cancelled", "Save operation cancelled.")
            return

        try:
            with pikepdf.open(self.file_path) as pdf:
                pdf.save(
                    save_path,
                    encryption=pikepdf.Encryption(
                        owner=password,
                        user=password,
                        R=6  # AES-256
                    )
                )

            self.password_entry.delete(0, tk.END)
            self.file_path = None
            self.file_label.config(text="No file selected", fg="red")
            messagebox.showinfo("Success", f"PDF locked successfully:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to lock PDF:\n{str(e)}")
            print(e)

def main():
    root = tk.Tk()
    app = PDFLockerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
