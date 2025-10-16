import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("800x600")

        self.files = []

        self.label = tk.Label(root, text="Selected PDFs:")
        self.label.pack(pady=5)

        self.listbox = tk.Listbox(root, width=100, height=20)
        self.listbox.pack(pady=5)

        self.add_button = tk.Button(root, text="Add PDFs", command=self.add_files)
        self.add_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear List", command=self.clear_list)
        self.clear_button.pack(pady=5)

    def add_files(self):
        new_files = filedialog.askopenfilenames(
            title="Select PDF files", filetypes=[("PDF files", "*.pdf")]
        )
        for f in new_files:
            if f not in self.files:
                self.files.append(f)
                self.listbox.insert(tk.END, os.path.basename(f))

    def merge_pdfs(self):
        if not self.files:
            messagebox.showerror("Error", "No PDF files selected!")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not output_path:
            return

        try:
            merger = PdfWriter()
            for pdf in self.files:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

    def clear_list(self):
        self.files = []
        self.listbox.delete(0, tk.END)


def main():
    """Entry point for the PDF merger application."""
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
