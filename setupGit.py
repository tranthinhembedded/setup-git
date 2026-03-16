import os
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def generate_key():
    email = email_entry.get()
    if not email:
        messagebox.showerror("Error", "Please enter your email address.")
        return

    ssh_dir = Path.home() / ".ssh"
    key_path = ssh_dir / "id_ed25519"
    pub_key_path = key_path.with_suffix('.pub')

    ssh_dir.mkdir(parents=True, exist_ok=True)

    if key_path.exists():
        overwrite = messagebox.askyesno("Warning", "SSH key already exists. Overwrite?")
        if overwrite:
            key_path.unlink(missing_ok=True)
            pub_key_path.unlink(missing_ok=True)
        else:
            load_existing_key(pub_key_path)
            return

    try:
        subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", email, "-f", str(key_path), "-N", ""], check=True, capture_output=True)
        load_existing_key(pub_key_path)
        status_label.config(text="Status: Key generated successfully.", fg="green")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to generate key:\n{e.stderr.decode()}")

def load_existing_key(pub_key_path):
    if pub_key_path.exists():
        with open(pub_key_path, 'r') as f:
            pub_key = f.read().strip()
            key_text.delete(1.0, tk.END)
            key_text.insert(tk.END, pub_key)
            status_label.config(text="Status: Key loaded.", fg="blue")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(key_text.get(1.0, tk.END).strip())
    root.update()
    status_label.config(text="Status: Copied to clipboard!", fg="green")

def test_connection():
    status_label.config(text="Status: Testing connection...", fg="black")
    root.update()
    result = subprocess.run(
        ["ssh", "-T", "-o", "StrictHostKeyChecking=accept-new", "git@github.com"],
        capture_output=True,
        text=True,
        input="yes\n",
        timeout=15
    )
    
    if "successfully authenticated" in result.stderr or "successfully authenticated" in result.stdout:
        messagebox.showinfo("Success", result.stderr or result.stdout)
        status_label.config(text="Status: Connection successful!", fg="green")
    else:
        messagebox.showwarning("Result", result.stderr or result.stdout)
        status_label.config(text="Status: Connection test finished.", fg="black")

root = tk.Tk()
root.title("GitHub SSH Setup")
root.geometry("500x420")
root.resizable(False, False)

tk.Label(root, text="GitHub Email:").pack(pady=(15, 5))
email_entry = tk.Entry(root, width=45)
email_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate SSH Key", command=generate_key)
generate_btn.pack(pady=10)

tk.Label(root, text="Public Key (Paste this to GitHub):").pack(pady=(10, 5))
key_text = tk.Text(root, height=6, width=55)
key_text.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

tk.Label(root, text="After adding to GitHub, test your connection:").pack(pady=(15, 5))

test_btn = tk.Button(root, text="Test Connection", command=test_connection)
test_btn.pack(pady=5)

status_label = tk.Label(root, text="Status: Ready", fg="black")
status_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()