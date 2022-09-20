"""Assignment 2: User Interface

CSC148, Winter 2022

This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of this
code, whether as given or with any changes, are expressly prohibited.

Authors: Sadia Sharmin, Diane Horton, Dina Sabie, Sophia Huynh, and
         Jonathan Calver.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Sadia Sharmin, Diane Horton, Dina Sabie, Sophia Huynh, and
                   Jonathan Calver

=== Module description ===
This module contains code to create an interface using the
classes specified in society_hierarchy.py and the client code in
client_code.py.

You should NOT modify this code.

You do not need to understand any of the code in this file in order to complete
the assignment. You may find it useful to run this file as one way to check that
your code is working, but you should also develop pytests to fully test your
solution.
"""
from typing import Optional, List, Callable
from tkinter import *
from tkinter import filedialog as fd, messagebox, ttk
from society_hierarchy import Citizen
from client_code import SocietySimulator


def get_citizen_ids() -> List[str]:
    """A helper function to get a list of each Citizen's cid"""
    return get_citizen_attributes('cid')


def get_citizen_jobs() -> List[str]:
    """A helper function to get a list of all unique jobs in the current
    society"""
    return get_citizen_attributes('job')


def get_citizen_attributes(attrib: str) -> List[str]:
    """A helper function to get a list of all unique values of the given
    attribute <attrib> in the current society
    Precondition: attrib is a valid Citizen attribute
    """
    if not simulation.current_society.get_head():
        return []
    subords = simulation.current_society.get_head().get_all_subordinates()
    attribs = [getattr(sub, attrib) for sub in subords]
    attribs = [getattr(simulation.current_society.get_head(),
                       attrib)] + attribs
    s = list(set(attribs))  # get unique job names
    s = sorted(s)  # sort before converting to strings to ensure proper order
    s = list(map(str, s))  # convert to strings
    return s


def format_superior(superior: Optional[Citizen] = None) -> str:
    """Return a string matching the current superior's ID for the View Superior
    button.
    """
    if superior:
        return f"View Superior (ID: {superior.cid})"

    return "View Superior (N/A)"


def display_citizen_list(citizens: List[Citizen], label: str) -> None:
    """Opens a window that lists all the IDs of the citizens in citizens.
    """
    list_window = Toplevel(main_window)
    main_label = Label(list_window, text=label, anchor=W)
    main_label.grid(column=0, row=0, sticky=NSEW)

    for i in range(len(citizens)):
        citizen = citizens[i]
        citizen_label = f"ID: {citizen.cid}"
        current_label = Label(list_window, text=citizen_label, anchor=W)
        current_label.grid(column=0, row=i + 1, sticky=NSEW)


def update_subordinates() -> None:
    """Update the list of subordinates.
    """
    if simulation.displaying_direct:
        display_direct_btn.configure(state=DISABLED)
        display_all_btn.configure(state=NORMAL)
    else:
        display_direct_btn.configure(state=NORMAL)
        display_all_btn.configure(state=DISABLED)

    subordinates_list.delete(0, END)
    subordinates = simulation.current_subordinates

    for subordinate in subordinates:
        subordinate_string = f"ID: {subordinate.cid}"
        if subordinate.get_all_subordinates():
            subordinate_string += ' [has subordinates]'
        subordinates_list.insert(END, subordinate_string)


def update_society() -> None:
    """Updates the society to the current_society"""
    current_society_content['text'] = str(simulation.current_society)


def update_citizen() -> None:
    """Updates the displayed citizen to show current_citizen's details.
    """

    update_society()

    (id_, manufacturer, model_year, rating, job, district) = \
        simulation.get_current_citizen_details()

    superior_button_text = format_superior(simulation.get_current_superior())
    view_superior_btn.configure(text=superior_button_text)

    # Disable buttons if current citizen is None:
    none_citizens_buttons = [common_superior_btn,
                             switch_leader_citizen_btn,
                             district_citizens_btn,
                             change_district_name,
                             view_head_btn,
                             find_job_btn,
                             view_citizen_btn
                             ]

    if simulation.current_citizen is None:
        st = DISABLED
    else:
        st = NORMAL
    for btn in none_citizens_buttons:
        btn.configure(state=st)

    if superior_button_text == "View Superior (N/A)":
        view_superior_btn.configure(state=DISABLED)
    else:
        view_superior_btn.configure(state=NORMAL)

    if simulation.is_district_leader():
        switch_leader_citizen_btn.configure(text="Become a citizen")
        change_district_name.configure(state=NORMAL)
        district_citizens_btn.configure(state=NORMAL)
    else:
        switch_leader_citizen_btn.configure(text="Become a district leader")
        district_citizens_btn.configure(state=DISABLED)

    citizen_id_display.configure(text=id_)
    citizen_manufacturer_display.configure(text=manufacturer)
    citizen_model_year_display.configure(text=model_year)
    citizen_rating_display.configure(text=rating)
    citizen_job_display.configure(text=job)
    citizen_district_display.configure(text=district)

    # Update the list of subordinates
    if simulation.displaying_direct:
        display_direct_subordinates_button()
    else:
        display_all_subordinates_button()


def create_single_prompt_window(instruction: str, button_label: str,
                                to_call: Callable[[str], None]) -> None:
    """Opens a window with instruction and button_label to prompt the user.
    Upon pressing the button with button_label, passes the entered data
    to to_call as a string.
    """
    new_window = Toplevel(main_window)

    def on_button_click() -> None:
        """Retrieve the entered text and calls to_call, closing this window.
        """
        entered_data = prompt_txt.get().strip()

        to_call(entered_data)
        new_window.destroy()

    # Instructions
    instructions_lbl = Label(new_window, text=instruction, anchor=W,
                             wraplength=300)
    instructions_lbl.grid(column=0, row=0, columnspan=2,
                          sticky=NSEW)

    # Prompt for the user
    prompt_txt = Entry(new_window)
    prompt_txt.grid(column=0, row=1, sticky=NSEW)

    # Add the button
    citizen_window_add_btn = Button(new_window, text=button_label,
                                    command=on_button_click)
    citizen_window_add_btn.grid(column=1, row=1, sticky=NSEW)


def create_single_dropdown_window(instruction: str, button_label: str,
                                  to_call: Callable[[str], None],
                                  options: List[str]) -> None:
    """Opens a window with instruction and button_label to prompt the user.
    Upon pressing the button with button_label, passes the entered data
    to to_call as a string. The options are displayed in a dropdown
    """
    new_window = Toplevel(main_window)

    def on_button_click() -> None:
        """Retrieve the entered text and calls to_call, closing this window.
        """
        entered_data = optVariable.get().strip()

        to_call(entered_data)
        new_window.destroy()

    # Instructions
    instructions_lbl = Label(new_window, text=instruction, anchor=W,
                             wraplength=300)
    instructions_lbl.grid(column=0, row=0, columnspan=2,
                          sticky=NSEW)

    optVariable = StringVar(new_window)
    optVariable.set(options[0])  # default value
    opts = OptionMenu(new_window, optVariable, *options)
    opts.grid(column=0, row=1, sticky=NSEW)

    # Add the button
    citizen_window_add_btn = Button(new_window, text=button_label,
                                    command=on_button_click)
    citizen_window_add_btn.grid(column=1, row=1, sticky=NSEW)


def prompt_with_ids(instruction: str, button_label: str,
                    to_call: Callable[[Optional[str]], None]) -> None:
    """Opens a window with instruction and button_label to prompt the user.
    Upon pressing the button with button_label, passes the entered data
    to to_call as a string. The options are displayed in a dropdown, but
    if there are no citizens in the society, a warning is displayed instead
    of the window.
    """
    ids = get_citizen_ids()
    if not ids:
        messagebox.showwarning(title=None,
                               message="society contains no citizens!")
    else:
        create_single_dropdown_window(instruction, button_label,
                                      to_call, ids)


# === Button handlers ===
def view_head_button() -> None:
    """Updates the display to the head of the Society when clicked.
    """
    simulation.current_citizen = simulation.get_society_head()
    update_citizen()


def view_superior_button() -> None:
    """Updates the display to the superior of the citizen when clicked.
    """
    superior = simulation.get_current_superior()
    if superior:
        simulation.current_citizen = superior
    update_citizen()


def display_direct_subordinates_button() -> None:
    """Updates the display of the subordinates to list direct subordinates only.
    """
    simulation.display_direct_subordinates()
    update_subordinates()


def display_all_subordinates_button() -> None:
    """Updates the display of the subordinates to list all subordinates.
    """
    simulation.display_all_subordinates()
    update_subordinates()


def add_citizen_button() -> None:
    """Open the 'add citizen' window to prompt the user for citizen details.
    """
    citizen_window = Toplevel(main_window)

    def create_citizen() -> None:
        """Creates a new citizen, reading in data from citizen_window.
        """
        try:
            cid = int(citizen_window_id_txt.get().strip())
            manufacturer = citizen_window_manufacturer_txt.get().strip()
            model_year = int(citizen_window_model_year_txt.get().strip())
            job = citizen_window_job_txt.get().strip()
            rating = int(citizen_window_rating_txt.get().strip())
            superior = citizen_window_superior_txt.get().strip()
            if not superior:
                superior = 0
            else:
                superior = int(superior)

            simulation.create_citizen(cid, manufacturer, model_year, rating,
                                      job, superior)
        except ValueError:
            messagebox.showwarning(title=None,
                                   message="VALUE ERROR\n\n" +
                                           "Ensure model year and "
                                           "rating are integers, "
                                           "and citizen ID is > 0 "
                                           "and doesn't already exist "
                                           "in this society")
        finally:
            update_citizen()
            citizen_window.destroy()

    # Instructions
    instructions = ("Enter the citizen details below."
                    "\n\nIf Superior ID is 0, this citizen will become the "
                    "head of the Society.")
    citizen_window_instructions = Label(citizen_window, text=instructions,
                                        anchor=W, wraplength=300)
    citizen_window_instructions.grid(column=0, row=0, columnspan=2,
                                     sticky=NSEW)

    # Label for their id number
    citizen_window_id_lbl = Label(citizen_window, text="ID", anchor=W)
    citizen_window_id_lbl.grid(column=0, row=1, sticky=NSEW)

    citizen_window_id_txt = Entry(citizen_window)
    citizen_window_id_txt.grid(column=1, row=1, sticky=NSEW)

    # Label for their manufacturer
    citizen_window_manufacturer_lbl = Label(citizen_window,
                                            text="Manufacturer", anchor=W)
    citizen_window_manufacturer_lbl.grid(column=0, row=2, sticky=NSEW)

    citizen_window_manufacturer_txt = Entry(citizen_window)
    citizen_window_manufacturer_txt.grid(column=1, row=2, sticky=NSEW)

    # Label for their model year
    citizen_window_model_year_lbl = Label(citizen_window, text="Model Year",
                                          anchor=W)
    citizen_window_model_year_lbl.grid(column=0, row=3, sticky=NSEW)

    citizen_window_model_year_txt = Entry(citizen_window)
    citizen_window_model_year_txt.grid(column=1, row=3, sticky=NSEW)

    # Label for the rating
    citizen_window_rating_lbl = Label(citizen_window, text="Rating",
                                      anchor=W)
    citizen_window_rating_lbl.grid(column=0, row=4, sticky=NSEW)

    citizen_window_rating_txt = Entry(citizen_window)
    citizen_window_rating_txt.grid(column=1, row=4, sticky=NSEW)

    # Label for their job
    citizen_window_job_lbl = Label(citizen_window, text="Job",
                                   anchor=W)
    citizen_window_job_lbl.grid(column=0, row=5, sticky=NSEW)

    citizen_window_job_txt = Entry(citizen_window)
    citizen_window_job_txt.grid(column=1, row=5, sticky=NSEW)

    # Label for their superior id
    citizen_window_superior_lbl = Label(citizen_window, text="Superior (ID)",
                                        anchor=W)
    citizen_window_superior_lbl.grid(column=0, row=6, sticky=NSEW)

    citizen_window_superior_txt = ttk.Combobox(citizen_window)
    citizen_window_superior_txt['values'] = ['0'] + get_citizen_ids()
    citizen_window_superior_txt['state'] = 'readonly'
    citizen_window_superior_txt.set('0')

    citizen_window_superior_txt.grid(column=1, row=6, sticky=NSEW)

    # Add citizen button
    citizen_window_add_btn = Button(citizen_window, text="Add Citizen",
                                    command=create_citizen)
    citizen_window_add_btn.grid(column=0, row=7, columnspan=2,
                                sticky=NSEW)


# the event parameter is to make this compatible as both a button event
# handler and a double click event handler
def view_selected_subordinate_button(event=None) -> None:
    """Display the selected subordinate.
    """
    if subordinates_list.curselection():
        index = subordinates_list.curselection()[0]
        selected_citizen = simulation.current_subordinates[index]
        simulation.display_citizen(selected_citizen.cid)
        update_citizen()


def common_superior_button(result: Optional[str] = None) -> None:
    """Prompt the user for another citizen's ID and display their common
    superior.
    """
    instruction = ("Enter the ID for the citizen you want to find a "
                   "common superior with for the current displayed citizen.")
    button_label = "Find Superior"
    if not result:
        # get list of citizen IDs, excluding current citizen
        ids = get_citizen_ids()
        ids.remove(str(simulation.current_citizen.cid))

        create_single_dropdown_window(instruction, button_label,
                                      common_superior_button, ids)
    else:
        label = "Displaying the closest common _superior of the citizens " \
                f"with IDs {result} and {simulation.current_citizen.cid}"
        display_citizen_list([simulation.get_common_superior(int(result))],
                             label)


def change_citizen_role(result: Optional[str] = None) -> None:
    """Change the Citizen into a DistrictLeader (prompting for a district name)
    OR if the Citizen is already a DistrictLeader, changes them into a Citizen.
    """
    if simulation.is_district_leader():
        simulation.become_citizen()
        update_citizen()
    else:
        if result:
            if result in simulation.get_all_district_names():
                messagebox.showwarning(message=f"{result} is already a"
                                               f" district,"
                                               f" the current citizen was not"
                                               f" updated.")
            else:
                simulation.become_district_leader(result)
                update_citizen()
        else:
            instruction = "Enter the name of the district to be created."
            button_label = "Create District"
            create_single_prompt_window(instruction, button_label,
                                        change_citizen_role)


def district_citizens_button() -> None:
    """Display a list of the manufacturer and IDs of citizens in the district.
    """
    district = simulation.get_current_citizen_district()
    label = f"Displaying the citizens in the {district} district."
    citizens = simulation.find_district_citizens()
    display_citizen_list(citizens, label)


def change_district_name_button(result: Optional[str] = None) -> None:
    """Prompt the user for a new district name and changes the name of the
    DistrictLeader's district.
    """
    if result:
        # ensure the district name is unique
        if result in simulation.get_all_district_names():
            messagebox.showwarning(message=f"{result} is already a district,"
                                           f" the name has not been changed")
        else:
            simulation.rename_current_district(result)
            update_citizen()
    else:
        if not simulation.current_citizen or not \
                simulation.current_citizen.get_district_name():
            messagebox.showwarning(message="Current citizen is not"
                                           " in a district!")
        else:
            instruction = "Enter the new name of the district."
            button_label = "Change Name"
            create_single_prompt_window(instruction, button_label,
                                        change_district_name_button)


def view_citizen_button(result: Optional[str] = None) -> None:
    """Prompt the user for an ID and display the citizen with that ID.
    """
    if result:
        simulation.display_citizen(int(result))
        update_citizen()
    else:
        instruction = "Enter the ID of the citizen to display."
        button_label = "Display"
        prompt_with_ids(instruction, button_label,
                        view_citizen_button)


def delete_citizen_button(result: Optional[str] = None) -> None:
    """Prompt the user for an ID and delete the citizen with that ID.
    """
    if result:
        simulation.delete_citizen(int(result))
        update_citizen()
    else:
        instruction = "Enter the ID of the citizen to delete."
        button_label = "Delete"
        prompt_with_ids(instruction, button_label,
                        delete_citizen_button)


def find_citizens_with_job_button(result: Optional[str] = None) -> None:
    """Prompt the user for a job and display a list of citizens with
    that job.
    """
    if result:
        label = f"Displaying citizens with the job {result}."
        citizens = simulation.find_citizens_with_job(result)
        display_citizen_list(citizens, label)
    else:
        instruction = "Enter the job of the citizens to find."
        button_label = "Find citizens"
        jobs = get_citizen_jobs()
        if not jobs:
            messagebox.showwarning(title=None,
                                   message="society contains no citizens!")
        else:
            create_single_dropdown_window(instruction, button_label,
                                          find_citizens_with_job_button,
                                          jobs)


def load_from_file_button(result: Optional[str] = None) -> None:
    """Prompt the user for a filename and load that file as the current
    Society.

    Displays the head of the Society afterwards.
    """

    result = fd.askopenfilename(
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
        title="Choose a file.")

    if result:
        simulation.file_to_society(result)
        update_citizen()


def promote_citizen_button(result: Optional[str] = None) -> None:
    """Promote the given citizen.
    """
    if result:
        simulation.promote_citizen(int(result))
        update_citizen()
    else:
        instruction = "Enter the ID of the citizen to promote."
        button_label = "Promote"
        prompt_with_ids(instruction, button_label,
                        promote_citizen_button)


# === Initial set-up of the Society Simulator ===
simulation = SocietySimulator()

# === Set up for the UI layout ===
# Set up the main window
main_window = Tk()
main_window.title("Society Management System")

# Create the left column of buttons (current citizen view)
view_superior_btn = Button(main_window, text="View Superior (N/A)",
                           command=view_superior_button, state=DISABLED, )
view_superior_btn.grid(column=0, row=0, columnspan=2, sticky=NSEW)

citizen_header_label = Label(main_window, text="Citizen", anchor=W)
citizen_header_label.grid(column=0, row=1, columnspan=2,
                          sticky=NSEW)

# Citizen ID
citizen_id_label = Label(main_window, text="    ID", anchor=W)
citizen_id_label.grid(column=0, row=2, sticky=NSEW)

citizen_id_display = Label(main_window, text="", relief="groove",
                           anchor=W)
citizen_id_display.grid(column=1, row=2, sticky=NSEW)

# Citizen Manufacturer Name
citizen_name_label = Label(main_window, text="    Manufacturer", anchor=W)
citizen_name_label.grid(column=0, row=3, sticky=NSEW)

citizen_manufacturer_display = Label(main_window, text="", relief="groove",
                                     anchor=W)
citizen_manufacturer_display.grid(column=1, row=3, sticky=NSEW)

# Citizen model year
citizen_model_year_label = Label(main_window, text="    Model Year", anchor=W)
citizen_model_year_label.grid(column=0, row=4, sticky=NSEW)

citizen_model_year_display = Label(main_window, text="", relief="groove",
                                   anchor=W)
citizen_model_year_display.grid(column=1, row=4, sticky=NSEW)

# Citizen Rating
citizen_rating_label = Label(main_window, text="    Rating", anchor=W)
citizen_rating_label.grid(column=0, row=5, sticky=NSEW)

citizen_rating_display = Label(main_window, text="", relief="groove",
                               anchor=W)
citizen_rating_display.grid(column=1, row=5, sticky=NSEW)

# Citizen Job
citizen_salary_label = Label(main_window, text="    Job",
                             anchor=W)
citizen_salary_label.grid(column=0, row=6, sticky=NSEW)

citizen_job_display = Label(main_window, text="", relief="groove",
                            anchor=W)
citizen_job_display.grid(column=1, row=6, sticky=NSEW)

# Citizen District
citizen_district_label = Label(main_window, text="    District", anchor=W)
citizen_district_label.grid(column=0, row=7, sticky=NSEW)

citizen_district_display = Label(main_window, text="", relief="groove",
                                 anchor=W)
citizen_district_display.grid(column=1, row=7, sticky=NSEW)

# Subordinates
subordinates_label = Label(main_window, text="Subordinates", anchor=W)
subordinates_label.grid(column=0, row=8, columnspan=2, sticky=NSEW)

# Display direct subordinates button
display_direct_btn = Button(main_window,
                            text="Display Direct\nSubordinates",
                            command=display_direct_subordinates_button)
display_direct_btn.grid(column=0, row=9, sticky=NSEW)

# Display all subordinates button
display_all_btn = Button(main_window, text="Display All\nSubordinates",
                         command=display_all_subordinates_button)
display_all_btn.grid(column=1, row=9, sticky=NSEW)

# View selected subordinate button
view_selected_btn = Button(main_window, text="View Selected Subordinate",
                           command=view_selected_subordinate_button)
view_selected_btn.grid(column=0, row=10, columnspan=2, sticky=NSEW)

# List of subordinates
subordinates_list = Listbox(main_window, selectmode=SINGLE)
subordinates_list.grid(column=0, row=11, columnspan=2, rowspan=6,
                       sticky=NSEW)
# allow user to alternatively double-click to navigate to subordinate
subordinates_list.bind('<Double-Button-1>', view_selected_subordinate_button)

# ===
# Draw a border for padding
separator_label = Label(main_window, text="  ")
separator_label.grid(column=2, row=0, rowspan=10, sticky=NSEW)

# Set up the second column (Citizen Controls)
citizen_controls_label = Label(main_window, text="Citizen/District Leader "
                                                 "Controls",
                               anchor=W)
citizen_controls_label.grid(column=3, row=0, sticky=NSEW)

# Get common _superior button
common_superior_btn = Button(main_window, text="Find common superior",
                             command=common_superior_button)
common_superior_btn.grid(column=3, row=1, sticky=NSEW)

# Become DistrictLeader button -- Switches to "Become a citizen" if the current
# citizen is a DistrictLeader
switch_leader_citizen_btn = Button(main_window, text="Become a district leader",
                                   command=change_citizen_role)
switch_leader_citizen_btn.grid(column=3, row=2, sticky=NSEW)

# Get district citizens button
district_citizens_btn = Button(main_window, text="Find district citizens",
                               command=district_citizens_button)
district_citizens_btn.grid(column=3, row=3, sticky=NSEW)

# Change district name button
change_district_name = Button(main_window, text="Change district name",
                              command=change_district_name_button)
change_district_name.grid(column=3, row=4, sticky=NSEW)

# Deletion-related buttons
citizen_controls_label = Label(main_window, text="Deletion Controls",
                               anchor=W)
citizen_controls_label.grid(column=3, row=6, sticky=NSEW)

# Delete citizen button
delete_citizen_btn = Button(main_window, text="Delete citizen",
                            command=delete_citizen_button)
delete_citizen_btn.grid(column=3, row=7, sticky=NSEW)

# ===
# Draw a border for padding
separator_label = Label(main_window, text="  ")
separator_label.grid(column=4, row=0, rowspan=10, sticky=NSEW)

# Society control buttons
citizen_name_label = Label(main_window, text="Basic Society Controls",
                           anchor=W)
citizen_name_label.grid(column=5, row=0, columnspan=2, sticky=NSEW)

# View society head button
view_head_btn = Button(main_window, text="View society head",
                       command=view_head_button)
view_head_btn.grid(column=5, row=1, columnspan=2, sticky=NSEW)

# Add citizen button
add_citizen_btn = Button(main_window,
                         text="Add citizen to society",
                         command=add_citizen_button)
add_citizen_btn.grid(column=5, row=2, columnspan=2, sticky=NSEW)

# View citizen button
view_citizen_btn = Button(main_window, text="View citizen",
                          command=view_citizen_button)
view_citizen_btn.grid(column=5, row=3, columnspan=2, sticky=NSEW)

# Find citizens with job button
find_job_btn = Button(main_window,
                      text="Find citizens with job",
                      command=find_citizens_with_job_button)
find_job_btn.grid(column=5, row=4, columnspan=2, sticky=NSEW)

# Promotion-related button
citizen_controls_label = Label(main_window, text="Promotion Controls",
                               anchor=W)
citizen_controls_label.grid(column=5, row=6, columnspan=2, sticky=NSEW)

current_society_label = Label(main_window, text="Current Society",
                              anchor=W, justify=LEFT)
current_society_label.grid(column=3, row=10, columnspan=4, sticky=NSEW)
current_society_content = Label(main_window, text="None",
                                anchor=W, justify=LEFT)
current_society_content.grid(column=3, row=11, columnspan=4, sticky=NSEW)

# Promotion button
promote_btn = Button(main_window, text="Promote citizen",
                     command=promote_citizen_button)
promote_btn.grid(column=5, row=7, sticky=NSEW)

# Load from file button
load_from_file_btn = Button(main_window,
                            text="Load society from file",
                            command=load_from_file_button)
load_from_file_btn.grid(column=5, row=9,
                        sticky=NSEW)

update_citizen()

if __name__ == "__main__":
    main_window.mainloop()
