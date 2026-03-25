import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.tasks = []
        self.setup_ui()
    
    def setup_ui(self):
        title_label = tk.Label(self.root, text="My To-Do List", font=("Helvetica", 16), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", padx= 10)
        add_button.pack(side=tk.LEFT)

        list_frame = tk.Frame(self.root, bg="#f0f4f7")
        list_frame.pack(pady=10, fill="both", expand=True)

        self.task_listbox = tk.Listbox(list_frame, font=("Helvetica", 12), bg="white", fg="#333")
        self.task_listbox.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 10), bg="#f0f0f0", fg="red")
        self.info_label.pack(pady=5)

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        mark_done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_done, bg="#2196F3", fg="white", padx=10)
        mark_done_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", padx=10)
        delete_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_tasks, bg="#9E9E9E", fg="white", padx=10)
        clear_button.pack(side=tk.LEFT, padx=5)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            display_text = f"{index}. {task["task"]} [{status}]"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            self.info_label.config(text="Please enter a task.")
            return
        self.tasks.append({"task": task_text, "done": False})
        self.task_entry.delete(0, tk.END)
        self.info_label.config(text= f"Task '{task_text}' added.")
        self.refresh_listbox()

    def get_selected_task_index(self):

    
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task.")
            return None
        return selection[0]
    
    def mark_done(self):
        index = self.get_selected_task_index()
        if index is None:
            return 
        
        self.tasks[index]["done"] = True
        self.info_label.config(text=f"Task '{self.tasks[index]['task']}' marked as done.")
        self.refresh_listbox()

    def delete_task(self):
        index = self.get_selected_task_index()
        if index is None:
            return
        
        removed_task = self.tasks.pop(index)
        task_text = removed_task["task"]
        self.info_label.config(text=f"Task '{task_text}' deleted.")
        self.refresh_listbox()

    def clear_tasks(self):
        if not self.tasks:
            self.info_label.config(text="No tasks to clear.")
            return 
        
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.info_label.config(text="All tasks cleared.")
            self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()