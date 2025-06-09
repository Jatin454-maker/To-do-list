import time

def View_tasks(lst):
    if is_empty(lst):
        print("list was empty!")
    else:
        for i in range(len(lst)):
            print(i+1,lst[i])
    time.sleep(1.5)
    
def is_empty(lst):
    return len(lst) == 0

def add_task(lst,task):
    lst.append(f"{task},  [❌]")
    print("task added successfuly!\n")
    time.sleep(1.5)
    
def remove_task(lst):
    ask=int(input("Entre the task number you want to remove: "))
    if 1<=ask<= len(lst):
        removed= lst.pop(ask-1)
        print(f"Task '{removed}' has been deleted.")
    else:
        print("Entre valid input!")        
    time.sleep(1.5)
        
def Mark_task(lst):
    if len(lst)==0:
        print("No task has been assigned!")
        return
    else:
        for i,value in enumerate(lst, start=1):
            print(i,". ",value)
        try:
            mark_ask= int(input("which task you have completed? "))
            if 1 <= mark_ask <= len(lst):
                if "✅" in lst[mark_ask - 1]:
                    print("Task is already marked as done.")
                else:
                    lst[mark_ask-1]=lst[mark_ask-1].replace("  [❌]","  ✅")
        except ValueError:
            print("Please enter a valid number!")
    time.sleep(1.5)

list=[]
while True:
    print("-----TO DO LIST MENU-----")
    print("1. View Tasks\n2. Add Task\n3. Remove Task\n4. Mark Task As Done\n5.Exit\n-------------------------")
    try:
        user_choice = int(input("Enter Your Choice (1-5): "))
    except ValueError:
        print("Please enter a number!")
        continue
    time.sleep(1.5)
    if user_choice==1:
        View_tasks(list)
        continue
    elif user_choice==2:
        task=input("Enter the task: ")
        add_task(list,task)
        continue   
    elif user_choice==3:
        remove_task(list)
        continue
    elif user_choice==4:
        Mark_task(list)
        continue
    elif user_choice==5:
        print("Thanks for using the To-Do List. Goodbye!")
        break
    else:
        print("invalid value!")
        continue