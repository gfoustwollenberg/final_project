"""

"""

from tkinter import *
from tkinter import messagebox

from medicare_plan_queue import PlanPriorityQueue, PlanNode
from person import Person
from person_linked_list import PersonNode, PersonLinkedList


profile_list = PersonLinkedList()
queue = PlanPriorityQueue()


def submit():
    first_name = f_name_entry.get()
    last_name = l_name_entry.get()
    dob = dob_entry.get()
    ssn = ssn_entry.get()
    plan_priority = x.get()
    user = Person(first_name, last_name, dob, ssn)
    profile = (PersonNode(user))
    profile_list.insert(profile)
    plan_request = PlanNode(user)
    queue.enqueue(plan_request)
    print(profile_list.size())
    print(queue.size())
    messagebox.showinfo(title='Plan Request Status', message='Your application has been submitted successfully. '
                                                             'Please clear the box and close the window if you are '
                                                             'done or submit your next application.')


def clear():
    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    dob_entry.delete(0, END)
    ssn_entry.delete(0, END)
    x.set(0)


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x600")
    window.title("Medicare Plan Application")
    window.config(background="white")

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

    x = IntVar()
    plan_list = ["Medicare Advantage Plan", "PACE Plan"]
    for index in range(len(plan_list)):
        radio_entry = Radiobutton(window, text=plan_list[index], variable=x, value=index+1, font=("Arial", 18))
        radio_entry.pack(anchor=CENTER)

    submit_button = Button(window, text="Submit", command=submit, font=("Arial", 24), fg="black", bg="white",
                           activeforeground="black", activebackground="white")
    submit_button.pack()
    cancel_button = Button(window, text="Clear", command=clear, font=("Arial", 24), fg="black", bg="white",
                           activeforeground="black", activebackground="white")
    cancel_button.pack()
    window.mainloop()
