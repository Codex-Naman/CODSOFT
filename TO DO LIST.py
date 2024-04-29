import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(master, width=50,bg="orange")
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(master, text="Add Task",bg="sky blue", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(master, width=50,bg="orange")
        self.task_listbox.pack(pady=10)
        
        self.mark_button = tk.Button(master, text="Mark Completed",bg="green", command=self.mark_completed)
        self.mark_button.pack(pady=10)

        self.unmark_button = tk.Button(master, text="Mark Uncompleted",bg="maroon", command=self.mark_uncompleted)
        self.unmark_button.pack(pady=10)
        
        self.delete_button = tk.Button(master, text="Delete Task",bg="red", command=self.delete_task)
        self.delete_button.pack(pady=10)
        
        self.load_tasks()
    
    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
    
    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = f"[✓] {task}"
            self.load_tasks()
    def mark_uncompleted(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = f"[X] {task}"
            self.load_tasks()
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.load_tasks()

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
