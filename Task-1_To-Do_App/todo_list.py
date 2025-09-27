to_do = [] 

def view_task():
    if not to_do:
        print("\n Your to-do list is empty! Add some tasks first.")
        return

    print("\n--- Your Current Tasks ---")
    for i, task in enumerate(to_do):
        task_number = i + 1 
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{task_number}. {status} {task['name']}")
    print("--------------------------")

def menu():
    while True: 
        print("\n*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View all Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            try:
                x = int(input("how many tasks you want to add: "))
                
                if x <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                    
                i = 1 
                while(i <= x):
                    task_name = input(f"Enter Task {i}: ")
                    new_task = {"name": task_name.strip(), "completed": False}
                    to_do.append(new_task)
                    print(f"Task '{task_name.strip()}' added.")
                    i += 1
            except ValueError:
                print("Invalid input. Please enter a valid number of tasks.")

        elif choice == 2:
            view_task()
            
        elif choice == 3:
            view_task()
            s = input("Enter task number(s) to remove (e.g., 1,3,4): ")
            
            try:
                ss = s.split(',')
                q = [int(num.strip()) for num in ss if num.strip().isdigit()]
                
                if not q:
                    print("Please enter valid task numbers separated by commas.")
                    continue
                
                q.sort(reverse=True)
                
                removed_count = 0
                for task_num in q:
                    list_index = task_num - 1
                    
                    if 0 <= list_index < len(to_do):
                        removed_task = to_do.pop(list_index) 
                        print(f"Removed task {task_num}: '{removed_task['name']}'")
                        removed_count += 1
                    else:
                        print(f"Task number {task_num} is invalid and was skipped.")
                        
                if removed_count == 0 and q:
                    print("\nNothing was removed. Check the task numbers and try again.")
                elif removed_count > 0:
                    print("\nTask removal complete.")

            except ValueError:
                 print("Invalid input format. Please use numbers separated by commas.")
                 
        elif choice == 4:
            view_task()
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                list_index = task_num - 1
                
                if 0 <= list_index < len(to_do):
                    if to_do[list_index]["completed"]:
                         print(f"Task {task_num} is already completed.")
                    else:
                        to_do[list_index]["completed"] = True
                        print(f"Task {task_num}: '{to_do[list_index]['name']}' marked as COMPLETED!")
                else:
                    print(f"Invalid task number: {task_num}.")
            except ValueError:
                print("Invalid input. Please enter a single task number.")

        elif choice == 5:
            print("\nExiting To-Do List. Goodbye!")
            break 
            
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    menu()
