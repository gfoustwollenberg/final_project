"""
Name : main.py
Author: Gabrielle Foust-Wollenberg
Created : 04/30/2024
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 11
IDE: PyCharm 2023.3
Copyright : This is my own original work
based on specifications issued by our instructor
Description : This code demonstrates the use of GUI, priority queues, and
              linked lists by obtaining information from users wanting to
              sign up for medicare plans and adding them to the queue and
              list for administrative use later.
            Input: User is responsible for adding their name, dob, and ssn.
            Output: Output includes messagebox letting the user know that
                    their entry in the queue and list is complete and lets
                    them know how large the queue is at that moment so they
                    can have awareness of how long it will take to be contacted.
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""

# imports necessary GUI materials and classes from different pages in the folder
from tkinter import *
from tkinter import messagebox

from medicare_plan_queue import PlanPriorityQueue, PlanNode
from person import Person
from person_linked_list import PersonNode, PersonLinkedList

# initializes the linked list and priority queue so all applicants can add to the same list and queue
profile_list = PersonLinkedList()
queue = PlanPriorityQueue()


# submit function obtains all info added to the gui, initializes the person class instance, each node's instance,
# adds person to the list and queue, and issues the message box for successful submission
def submit():
    first_name = f_name_entry.get()
    last_name = l_name_entry.get()
    dob = dob_entry.get()
    ssn = ssn_entry.get()
    plan_priority = x.get()
    user = Person(first_name, last_name, dob, ssn)
    profile = (PersonNode(user))
    profile_list.insert(profile)
    plan_request = PlanNode(user, plan_priority)
    queue.enqueue(plan_request)
    print("Person List Size: ", profile_list.size())
    print("Priority Queue Length: ", queue.size())
    messagebox.showinfo(title='Plan Request Status', message='Your application has been submitted successfully. '
                                                             'Please clear the box and close the window if you are '
                                                             'done or submit your next application.')


# clear function resets all fields
def clear():
    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    dob_entry.delete(0, END)
    ssn_entry.delete(0, END)
    x.set(0)


if __name__ == "__main__":
    # initializes GUI window, sets size, background, and title
    window = Tk()
    window.geometry("600x600")
    window.title("Medicare Plan Application")
    window.config(background="white")

    # creates entry fields for first name, last name, dob, and ssn
    f_name_entry = Entry(window, font=("Arial", 18), bg="white", fg="black", width=205)
    f_name_entry.insert(0, 'First Name (letters or hyphen only)')
    f_name_entry.pack()
    l_name_entry = Entry(window, font=("Arial", 18), bg="white", fg="black", width=205)
    l_name_entry.insert(0, 'Last Name (letters or hyphen only)')
    l_name_entry.pack()
    dob_entry = Entry(window, font=("Arial", 18), bg="white", fg="black", width=205)
    dob_entry.insert(0, 'Date of Birth (numbers and / only)')
    dob_entry.pack()
    ssn_entry = Entry(window, font=("Arial", 18), bg="white", fg="black", width=205)
    ssn_entry.insert(0, 'Social Security Number (numbers and - only)')
    ssn_entry.pack()

    # creates radio buttons for each plan option
    x = IntVar()
    plan_list = ["Medicare Advantage Plan", "PACE Plan"]
    for index in range(len(plan_list)):
        radio_entry = Radiobutton(window, text=plan_list[index], variable=x, value=index+1, font=("Arial", 18))
        radio_entry.pack(anchor=CENTER)

    # creates submit and clear buttons
    submit_button = Button(window, text="Submit", command=submit, font=("Arial", 24), fg="black", bg="white",
                           activeforeground="black", activebackground="white")
    submit_button.pack()
    cancel_button = Button(window, text="Clear", command=clear, font=("Arial", 24), fg="black", bg="white",
                           activeforeground="black", activebackground="white")
    cancel_button.pack()
    window.mainloop()
