import tkinter as tk
from tkinter import filedialog, messagebox

# Function to count words
def count_words():
    file_path = filedialog.askopenfilename(
        title="Select Text File",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

            # Split text into words
            words = text.split()
            word_count = len(words)

            result_label.config(
                text=f"Total Words: {word_count}"
            )

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "File not found!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{e}"
        )

# Create window
window = tk.Tk()
window.title("Word Counter")
window.geometry("400x300")
window.configure(bg="lightblue")

# Title
title = tk.Label(
    window,
    text="📄 Word Counter",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=20)

# Button
select_button = tk.Button(
    window,
    text="Select Text File",
    font=("Arial", 12),
    command=count_words
)
select_button.pack(pady=20)

# Result Label
result_label = tk.Label(
    window,
    text="Total Words: 0",
    font=("Arial", 14),
    bg="lightblue"
)
result_label.pack(pady=20)

# Run app
window.mainloop()