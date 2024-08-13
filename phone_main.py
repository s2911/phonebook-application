import re
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Initialize the phonebook
phonebook = {}

def is_valid_phone_number(phone_number):
    """Validate phone number format (10 digits)."""
    pattern = re.compile(r'^\d{10}$')
    return pattern.match(phone_number)

def is_valid_email(email):
    """Validate email format."""
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return pattern.match(email)

def is_valid_country_code(country_code):
    """Validate country code format (e.g., +1, +44)."""
    pattern = re.compile(r'^\+\d+$')
    return pattern.match(country_code)

def is_valid_date(date_str):
    """Validate birthdate format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def save_phonebook(filename):
    """Save the phonebook to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(phonebook, f, indent=4)
        print(f"Phonebook saved to {filename}.")
    except IOError as e:
        print(f"Error saving phonebook: {e}")

def load_phonebook(filename):
    """Load the phonebook from a JSON file."""
    global phonebook
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                phonebook = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading phonebook: {e}")

def format_phone_number(phone_number):
    """Format phone number to a simple 1234567890 format."""
    return ''.join(filter(str.isdigit, phone_number))

def add_contact():
    """Add or update a contact in the phonebook."""
    def submit_contact():
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()
        country_code = entry_country_code.get().strip()
        phone_number = entry_phone_number.get().strip()
        email = entry_email.get().strip()
        address = entry_address.get().strip()
        pincode = entry_pincode.get().strip()
        district = entry_district.get().strip()
        state = entry_state.get().strip()
        country = entry_country.get().strip()
        birthdate = entry_birthdate.get().strip()

        phone_number = format_phone_number(phone_number)

        if not is_valid_phone_number(phone_number):
            messagebox.showerror("Invalid Input", "Invalid phone number format. Please enter 10 digits.")
            return
        
        if not is_valid_country_code(country_code):
            messagebox.showerror("Invalid Input", "Invalid country code format. Please enter a valid code (e.g., +1).")
            return
        
        if not is_valid_email(email):
            messagebox.showerror("Invalid Input", "Invalid email format.")
            return

        if not is_valid_date(birthdate):
            messagebox.showerror("Invalid Input", "Invalid birthdate format. Please enter in YYYY-MM-DD format.")
            return

        contact_info = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "country_code": country_code,
            "email": email,
            "address": address,
            "pincode": pincode,
            "district": district,
            "state": state,
            "country": country,
            "birthdate": birthdate
        }

        full_name = f"{first_name} {last_name}"

        if full_name in phonebook:
            if messagebox.askyesno("Contact Exists", "Contact already exists. Do you want to update it?"):
                phonebook[full_name] = contact_info
                messagebox.showinfo("Success", f"Contact '{full_name}' updated.")
        else:
            phonebook[full_name] = contact_info
            messagebox.showinfo("Success", f"Contact '{full_name}' added.")

        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")

    tk.Label(add_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_first_name = tk.Entry(add_window)
    entry_first_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_last_name = tk.Entry(add_window)
    entry_last_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Country Code:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_country_code = tk.Entry(add_window)
    entry_country_code.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Phone Number:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_phone_number = tk.Entry(add_window)
    entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Email:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_email = tk.Entry(add_window)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Address:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_address = tk.Entry(add_window)
    entry_address.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Pincode:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_pincode = tk.Entry(add_window)
    entry_pincode.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(add_window, text="District:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    entry_district = tk.Entry(add_window)
    entry_district.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(add_window, text="State:").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    entry_state = tk.Entry(add_window)
    entry_state.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Country:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
    entry_country = tk.Entry(add_window)
    entry_country.grid(row=9, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Birthdate (YYYY-MM-DD):").grid(row=10, column=0, padx=10, pady=5, sticky="e")
    entry_birthdate = tk.Entry(add_window)
    entry_birthdate.grid(row=10, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Submit", command=submit_contact).grid(row=11, column=0, columnspan=2, pady=10)

def search_contact():
    """Search for a contact by name or phone number."""
    def search():
        search_type = search_type_var.get().strip()
        search_value = entry_search_value.get().strip()

        if search_type == "name":
            if search_value in phonebook:
                contact = phonebook[search_value]
                contact_details = f"First Name: {contact['first_name']}\n" \
                                  f"Last Name: {contact['last_name']}\n" \
                                  f"Phone number: {contact['phone_number']}\n" \
                                  f"Country code: {contact['country_code']}\n" \
                                  f"Email: {contact['email']}\n" \
                                  f"Address: {contact['address']}, {contact['district']}, {contact['state']}, {contact['pincode']}, {contact['country']}\n" \
                                  f"Birthdate: {contact['birthdate']}\n"
                messagebox.showinfo("Contact Found", contact_details)
            else:
                messagebox.showinfo("Search Result", "Contact not found.")
        elif search_type == "phone":
            phone_number = format_phone_number(search_value)
            found = False
            for full_name, contact in phonebook.items():
                if contact['phone_number'] == phone_number:
                    contact_details = f"Full Name: {full_name}\n" \
                                      f"First Name: {contact['first_name']}\n" \
                                      f"Last Name: {contact['last_name']}\n" \
                                      f"Country code: {contact['country_code']}\n" \
                                      f"Email: {contact['email']}\n" \
                                      f"Address: {contact['address']}, {contact['district']}, {contact['state']}, {contact['pincode']}, {contact['country']}\n" \
                                      f"Birthdate: {contact['birthdate']}\n"
                    messagebox.showinfo("Contact Found", contact_details)
                    found = True
                    break
            if not found:
                messagebox.showinfo("Search Result", "Contact not found.")
        else:
            messagebox.showerror("Invalid Input", "Invalid search type. Please choose 'name' or 'phone'.")

        search_window.destroy()

    search_window = tk.Toplevel(root)
    search_window.title("Search Contact")

    tk.Label(search_window, text="Search by:").grid(row=0, column=0, padx=10, pady=5)
    search_type_var = tk.StringVar(value="name")
    tk.Radiobutton(search_window, text="Name", variable=search_type_var, value="name").grid(row=0, column=1, padx=10, pady=5)
    tk.Radiobutton(search_window, text="Phone", variable=search_type_var, value="phone").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(search_window, text="Search Value:").grid(row=1, column=0, padx=10, pady=5)
    entry_search_value = tk.Entry(search_window)
    entry_search_value.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

    tk.Button(search_window, text="Search", command=search).grid(row=2, column=0, columnspan=3, pady=10)

def delete_contact():
    """Delete a contact by name."""
    def submit_delete():
        full_name = entry_full_name.get().strip()

        if full_name in phonebook:
            del phonebook[full_name]
            messagebox.showinfo("Success", f"Contact '{full_name}' deleted.")
        else:
            messagebox.showinfo("Delete Result", "Contact not found.")

        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Contact")

    tk.Label(delete_window, text="Full Name (First Last):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_full_name = tk.Entry(delete_window)
    entry_full_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(delete_window, text="Delete", command=submit_delete).grid(row=1, column=0, columnspan=2, pady=10)

def list_contacts():
    """List all contacts in the phonebook."""
    contacts_window = tk.Toplevel(root)
    contacts_window.title("Contacts List")

    # Create Treeview for displaying contacts in tabular form
    tree = ttk.Treeview(contacts_window, columns=("Name", "Phone", "Country Code", "Email", "Address", "Pincode", "District", "State", "Country", "Birthdate"), show='headings')
    tree.heading("Name", text="Full Name")
    tree.heading("Phone", text="Phone Number")
    tree.heading("Country Code", text="Country Code")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.heading("Pincode", text="Pincode")
    tree.heading("District", text="District")
    tree.heading("State", text="State")
    tree.heading("Country", text="Country")
    tree.heading("Birthdate", text="Birthdate")

    tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    # Configure the grid row and column to expand
    contacts_window.grid_rowconfigure(0, weight=1)
    contacts_window.grid_columnconfigure(0, weight=1)

    if phonebook:
        sorted_contacts = sorted(phonebook.items())
        for full_name, contact in sorted_contacts:
            tree.insert("", tk.END, values=(
                full_name,
                contact['phone_number'],
                contact['country_code'],
                contact['email'],
                f"{contact['address']}, {contact['district']}, {contact['state']}, {contact['pincode']}, {contact['country']}",
                contact['pincode'],
                contact['district'],
                contact['state'],
                contact['country'],
                contact['birthdate']
            ))
    else:
        tree.insert("", tk.END, values=("No contacts to display", "", "", "", "", "", "", "", "", ""))

def exit_application():
    """Exit the application."""
    save_phonebook("phonebook.json")
    root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Phonebook Application")

tk.Button(root, text="Add Contact", command=add_contact).pack(padx=10, pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(padx=10, pady=5)
tk.Button(root, text="List Contacts", command=list_contacts).pack(padx=10, pady=5)
tk.Button(root, text="Exit", command=exit_application).pack(padx=10, pady=5)

load_phonebook("phonebook.json")

root.mainloop()
