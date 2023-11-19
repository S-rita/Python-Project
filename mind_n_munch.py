from tkinter import *
from tkinter import messagebox, Canvas, Scrollbar
from datetime import datetime
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO
import json
from abc import ABC, abstractmethod


''''''''''''' BASE FORM '''''''''''''
class BaseForm(ABC):
    def __init__(self, window, activity_type):
        self.window = window
        self.activity_type = activity_type
        self.history = []

    @abstractmethod
    def form(self):
        pass

    def confirm_exit(self, health_window):
        result = messagebox.askquestion("Confirm Exit", "Your entry has not been saved. Are you sure you want to quit?",
                                       icon='warning')
        if result == 'yes':
            health_window.destroy()


''''''''''''' MIND FORM '''''''''''''
class MindForm(BaseForm):
    def __init__(self, window):
        super().__init__(window, "Mental Health")

    def form(self):
        mental_window = Toplevel(self.window)
        mental_window.title("MIND")
        mental_window.geometry("900x500")
        
    ########## MOOD ##########
        moods_label = Label(mental_window, text="Today's Mood", font=("Comic Sans MS", 20, "bold"))
        moods_label.grid(row=0, columnspan=10, pady=(10, 5))
        moods_var = StringVar()

        image_data = [
            ("Image/mood/happy.png", "Happy"),
            ("Image/mood/calm.png", "Calm"),
            ("Image/mood/neutral.png", "Neutral"),
            ("Image/mood/sad.png", "Sad"),
            ("Image/mood/angry.png", "Angry"),
        ]

        images_mood = []

        for idx, (path, label_text) in enumerate(image_data):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_mood.append(img)

            button = Radiobutton(mental_window, image=img, variable=moods_var, value=label_text)
            button.image = img
            button.grid(row=1, column=idx+1, padx=15)

            label = Label(mental_window, text=label_text, font=("Courier", 13))
            label.grid(row=2, column=idx+1, padx=25) 

    ########## ACTIVITY ##########
        activity_label = Label(mental_window, text="Activity", font=("Comic Sans MS", 20, "bold"))
        activity_label.grid(row=4, columnspan=10, pady=(20, 5))
        activity_var = StringVar()

        image_data_activity = [
            ("Image/activity/photographing.png", "Photographing"),
            ("Image/activity/exercising.png", "Exercising"),
            ("Image/activity/gardening.png", "Gardening"),
            ("Image/activity/singing.png", "Singing"),
            ("Image/activity/travelling.png", "Travelling"),
            ("Image/activity/watching.png", "Watching"),
            ("Image/activity/playing.png", "Playing"),
            ("Image/activity/reading.png", "Reading"),
        ]

        images_activity = []

        for idx, (path, label_text) in enumerate(image_data_activity):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_activity.append(img)

            button = Radiobutton(mental_window, image=img, variable=activity_var, value=label_text)
            button.image = img
            button.grid(row=5, column=idx, padx=5)

            label = Label(mental_window, text=label_text, font=("Courier", 12))
            label.grid(row=6, column=idx, padx=10) 

    ########## WITH WHO ##########
        who_label = Label(mental_window, text="with...", font=("Comic Sans MS", 15))
        who_label.grid(row=7, columnspan=10, pady=(20, 5))
        who_var = StringVar()

        image_data_who = [
            ("Image/with_who/family.png", "Family"),
            ("Image/with_who/friend.png", "Friend"),
            ("Image/with_who/partner.png", "Partner"),
            ("Image/with_who/alone.png", "Alone"),
        ]

        images_who = []

        for idx, (path, label_text) in enumerate(image_data_who):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_who.append(img)

            button = Radiobutton(mental_window, image=img, variable=who_var, value=label_text)
            button.image = img
            button.grid(row=8, column=idx+2, padx=5)  
            label = Label(mental_window, text=label_text, font=("Courier", 13))
            label.grid(row=9, column=idx+2, padx=5)

    ########## SUMBIT & CLOSE ##########
        submit_button = Button(mental_window, text="SUBMIT", font=("Comic Sans MS", 20, "bold"), fg="green",
                               command=lambda: self.submit_mind_form(mental_window, "Mental Health",
                                                                moods_var.get(), activity_var.get(), who_var.get()))

        submit_button.grid(row=11, column=0, columnspan=10, pady=(30,0), padx=10)

        close_button = Button(mental_window, text="X", font=("Comic Sans MS", 10, "bold"), fg="red", command=lambda: self.confirm_exit(mental_window))
        close_button.place(relx=1.0, rely=0, anchor=NE)

    def submit_mind_form(self, window, activity_type, mood, activity, with_whom):
        current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        entry = {
            "Date": current_date,
            "Activity Type": activity_type,
            "Mood": mood,
            "Activity": activity,
            "with": with_whom
        }

        self.history.append(entry)

        messagebox.showinfo(f"{activity_type} Submission", f"{activity_type} registered successfully!")

        window.destroy()

    def confirm_exit(self, mental_window):
        super().confirm_exit(mental_window)
        
        
''''''''''''' MUNCH FORM '''''''''''''

class MunchForm(BaseForm):
    def __init__(self, window):
        super().__init__(window, "Physical Health")

    def form(self):
        physical_window = Toplevel(self.window)
        physical_window.title("MUNCH")
        physical_window.geometry("410x900")
        
    ########## FOOD ##########
        food_label = Label(physical_window, text="Food", font=("Comic Sans MS", 20, "bold"))
        food_label.grid(row=0, columnspan=4, pady=(5,5))
        food_var = StringVar()

        image_foods = [
            ("Image/food/breakfast.png", "Breakfast"),
            ("Image/food/lunch.png", "Lunch"),
            ("Image/food/dinner.png", "Dinner"),
            ("Image/food/snack.png", "Snack"),
        ]

        images_foods = []

        for idx, (path, label_text) in enumerate(image_foods):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_foods.append(img)

            button = Radiobutton(physical_window, image=img, variable=food_var, value=label_text)
            button.image = img
            button.grid(row=1, column=idx, padx=5)

            label = Label(physical_window, text=label_text, font=("Courier", 13))
            label.grid(row=2, column=idx, padx=5)
    
    ########## WITH WHO ##########
        who_label = Label(physical_window, text="with...", font=("Comic Sans MS", 15))
        who_label.grid(row=3, columnspan=4, pady=(10, 5))
        who_var = StringVar()

        image_data_who = [
            ("Image/with_who/family.png", "Family"),
            ("Image/with_who/friend.png", "Friend"),
            ("Image/with_who/partner.png", "Partner"),
            ("Image/with_who/alone.png", "Alone"),
        ]

        images_who_exercise = []

        for idx, (path, label_text) in enumerate(image_data_who):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_who_exercise.append(img)

            button = Radiobutton(physical_window, image=img, variable=who_var, value=label_text)
            button.image = img
            button.grid(row=4, column=idx, padx=5)

            label = Label(physical_window, text=label_text, font=("Courier", 13))
            label.grid(row=5, column=idx, padx=5)
            
    ########## WATER INTAKE ##########
        water_label = Label(physical_window, text="Water Intake", font=("Comic Sans MS", 20, "bold"))
        water_label.grid(row=6, columnspan=4, pady=(15, 5))
        water_entry = Entry(physical_window)
        water_entry.grid(row=7, columnspan=4)

        add_250ml_button = Button(physical_window, text="+250 ml", font=("Courier", 13), command=lambda: self.add_water(water_entry, 250))
        add_500ml_button = Button(physical_window, text="+500 ml", font=("Courier", 13), command=lambda: self.add_water(water_entry, 500))
        add_1000ml_button = Button(physical_window, text="+1000 ml", font=("Courier", 13), command=lambda: self.add_water(water_entry, 1000))
        add_250ml_button.grid(row=8, column=1)
        add_500ml_button.grid(row=8, column=2)
        add_1000ml_button.grid(row=9, columnspan=4)
        
    ########## EXERCISE ##########
        exercise_label = Label(physical_window, text="Exercise", font=("Comic Sans MS", 20, "bold"))
        exercise_label.grid(row=10, columnspan=4, pady=(15,5))

        exercise_var = StringVar()
        exercise_var.set("")

        exercise_choices = ["Walking", "Running", "Strength Training", "HIIT", "Swimming", "Cycling", "Yoga", "Sport", "Other"]
        exercise_dropdown = OptionMenu(physical_window, exercise_var, *exercise_choices)
        exercise_dropdown.grid(row=12, columnspan=4)
        
        duration_label = Label(physical_window, text="duration:", font=("Courier", 13))
        duration_label.grid(row=14, column=0)
        duration_entry = Entry(physical_window)
        duration_entry.grid(row=14, columnspan=4)
        
        increase_duration_button = Button(physical_window, text="+30 mins", font=("Courier", 13), command=lambda: self.adjust_exercise_duration(duration_entry, 30))
        decrease_duration_button = Button(physical_window, text="-30 mins", font=("Courier", 13), command=lambda: self.adjust_exercise_duration(duration_entry, -30))
        increase_duration_button.grid(row=16, column=1)
        decrease_duration_button.grid(row=16, column=2)
    
    ########## SLEEP ##########
        sleep_label = Label(physical_window, text="Sleep", font=("Comic Sans MS", 20, "bold"))
        sleep_label.grid(row=19, columnspan=4, pady=(15,5))
        
        sleep_hrs_label = Label(physical_window, text="time Asleep:", font=("Courier", 13))
        sleep_hrs_label.grid(row=20, column=0)
        sleep_entry = Entry(physical_window)
        sleep_entry.grid(row=20, columnspan=5)
        
        increase_sleep_button = Button(physical_window, text="+1 hrs", font=("Courier", 13), command=lambda: self.adjust_sleep(sleep_entry, 1))
        decrease_sleep_button = Button(physical_window, text="-1 hrs", font=("Courier", 13), command=lambda: self.adjust_sleep(sleep_entry, -1))
        increase_sleep_button.grid(row=22, column=1, pady=(0,10))
        decrease_sleep_button.grid(row=22, column=2, pady=(0,10))
        
        sleep_feeling_label = Label(physical_window, text="you feel:", font=("Courier", 13))
        sleep_feeling_label.grid(row=24, column=0)
        sleep_feeling = StringVar()

        image_sleep = [
            ("Image/sleep/energized.png", "Energized"),
            ("Image/sleep/sleepy.png", "Sleepy"),
        ]

        images_sleep = []

        for idx, (path, label_text) in enumerate(image_sleep):
            img = ImageTk.PhotoImage(Image.open(path).resize((60, 60)))
            images_sleep.append(img)

            button = Radiobutton(physical_window, image=img, variable=sleep_feeling, value=label_text)
            button.image = img
            button.grid(row=24, column=idx+1)

            label = Label(physical_window, text=label_text, font=("Courier", 13))
            label.grid(row=25, column=idx+1)

    ########## SUMBIT & CLOSE ##########
        submit_button = Button(physical_window, text="SUBMIT", fg='green', font=("Comic Sans MS", 20, "bold"),
                            command=lambda: self.submit_form(physical_window, "Physical Health", 
                                                            food_var.get(), who_var.get(),
                                                            water_entry.get(), exercise_var.get(),
                                                            duration_entry.get(), sleep_entry.get(),
                                                            sleep_feeling.get()))
        submit_button.grid(row=27, columnspan=4, pady=30)
        
        close_button = Button(physical_window, text="X", fg='red', font=("Comic Sans MS", 10, "bold"), command=lambda: self.confirm_exit(physical_window))
        close_button.place(relx=1.0, rely=0, anchor=NE)

    def submit_munch_form(self, window, activity_type, food_type, with_whom, water_intake, exercise_type, exercise_duration, sleep_hours, sleep_quality):
        current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        entry = {
            "Date": current_date,
            "Activity Type": activity_type,
            "Meal": food_type,
            "With": with_whom,
            "Water Intake": water_intake,
            "Exercise Type": exercise_type,
            "Exercise Duration": exercise_duration,
            "Sleep Hours": sleep_hours,
            "Sleep Quality": sleep_quality
        }

        self.history.append(entry)

        messagebox.showinfo(f"{activity_type} Submission", f"{activity_type} registered successfully!")

        window.destroy()

    def confirm_exit(self, physical_window):
        super().confirm_exit(physical_window)
        
    ########## 3 BUTTON COMMANDS ##########
    def add_water(self, entry, amount):
        current_value = entry.get()
        try:
            current_value = int(current_value.split(' ')[0]) if current_value else 0
            if current_value + amount < 0:
                raise ValueError("Water intake cannot be below 0")
            elif current_value + amount > 28000:
                raise ValueError("Excessive water intake.\nShould be less than 28,000ml/day")
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
            return
        entry.delete(0, END)
        entry.insert(0, str(current_value + amount) + " ml")

    def adjust_exercise_duration(self, entry, amount):
        current_value = entry.get()
        try:
            current_value = int(current_value.split(' ')[0]) if current_value else 0
            if current_value + amount < 0:
                raise ValueError("Exercise duration cannot be below 0.")
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
            return
        entry.delete(0, END)
        entry.insert(0, str(current_value + amount) + " mins")
        
    def adjust_sleep(self, entry, hours):
        current_value = entry.get()
        try:
            current_value = int(current_value.split(' ')[0]) if current_value else 0
            if current_value + hours < 0:
                raise ValueError("Sleep hours cannot be below 0.")
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
            return
        entry.delete(0, END)
        entry.insert(0, str(current_value + hours) + " hrs")
        
        
''''''''''''' DASHBOARD '''''''''''''

class Dashboard:
    def __init__(self, window, history):
        self.window = window
        self.history = history

    def dashboard(self):
        dashboard_window = Toplevel(self.window)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("830x800")

        user_mood_data = {}
        exercise_data = {}
        sleep_data = {}
        
    ########## COUNT ##########
        for entry in self.history:
            if entry['Activity Type'] == 'Mental Health':
                user_mood_data[entry['Mood']] = user_mood_data.get(entry['Mood'], 0) + 1
            elif entry['Activity Type'] == 'Physical Health':
                exercise_data[entry['Exercise Type']] = exercise_data.get(entry['Exercise Type'], 0) + 1
                if 'Sleep Hours' in entry:
                    sleep_duration_str = entry['Sleep Hours']
                    sleep_duration = float(sleep_duration_str.split()[0])
                    sleep_data[entry['Date']] = sleep_duration

    ########## SCROLLBAR ##########

        canvas = Canvas(dashboard_window)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        scrollbar = Scrollbar(dashboard_window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)

        frame.bind("<Configure>", on_frame_configure)
        
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)
        
    ########## MOODS BAR CHART ##########
        def plot_bar_chart(data, title, xlabel, ylabel):
            plt.figure(figsize=(8, 4))
            plt.bar(data.keys(), data.values(), color='skyblue')
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            return ImageTk.PhotoImage(Image.open(buf))
        
        mood_chart = plot_bar_chart(user_mood_data, 'Mood Distribution', 'Mood', 'Count')
        mood_chart_label = Label(frame, image=mood_chart)
        mood_chart_label.image = mood_chart
        mood_chart_label.pack()
        
    ########## EXERCISE PIE CHART ##########
        def plot_pie_chart(data, title):
            plt.figure(figsize=(8, 8))
            plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140)
            plt.title(title)
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            return ImageTk.PhotoImage(Image.open(buf))

        exercise_chart = plot_pie_chart(exercise_data, 'Exercise Distribution')
        exercise_chart_label = Label(frame, image=exercise_chart)
        exercise_chart_label.image = exercise_chart
        exercise_chart_label.pack()

    ########## SLEEP LINE GRAPH ##########
        def plot_line_graph(x_data, y_data, title, xlabel, ylabel, color='green'):
            plt.figure(figsize=(8, 4))
            plt.plot(x_data, y_data, marker='o', linestyle='-', color=color)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            return ImageTk.PhotoImage(Image.open(buf))
    
        dates = sorted(sleep_data.keys())
        sleep_values = [sleep_data[date] for date in dates]
        sleep_chart = plot_line_graph(dates, sleep_values, 'Sleep Duration Over Time', 'Date', 'Hours of Sleep')
        sleep_chart_label = Label(frame, image=sleep_chart)
        sleep_chart_label.image = sleep_chart
        sleep_chart_label.pack()
    

''''''''''''' MAIN CLASS '''''''''''''
class Mind_n_Munch:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mind & Munch")
        self.window.geometry("400x550")

        self.history = []
    
        
        menu_button = Menubutton(self.window, text="Menu", font=("Comic Sans MS", 13))
        menu_button.menu = Menu(menu_button, tearoff=0)
        menu_button["menu"] = menu_button.menu
        menu_button.menu.add_command(label="Upload", command=self.upload_data)
        menu_button.menu.add_command(label="History", command=self.show_history)
        menu_button.menu.add_command(label="Clear", command=self.clear_history)

        menu_button.pack(side=TOP, anchor=E, padx=10, pady=10)

        self.mind_health_form = MindForm(self.window)
        self.physical_health_form = MunchForm(self.window)
        self.dashboard_view = Dashboard(self.window, self.history)

        mind_png = ImageTk.PhotoImage(Image.open("Image/main_menu/mind.png").resize((300, 120)))
        munch_png = ImageTk.PhotoImage(Image.open("Image/main_menu/munch.png").resize((300, 120)))
        dashboard_png = ImageTk.PhotoImage(Image.open("Image/main_menu/dashboard.png").resize((300, 120)))
        save_png = ImageTk.PhotoImage(Image.open("Image/main_menu/save.png").resize((200, 80)))
        exit_png = ImageTk.PhotoImage(Image.open("Image/main_menu/exit.png").resize((200, 80)))
        
        mind_button = Button(self.window, image=mind_png, command=self.mind_form, borderwidth=0)
        munch_button = Button(self.window, image=munch_png, command=self.munch_form, borderwidth=0)
        dashboard_button = Button(self.window, image=dashboard_png, command=self.dashboard, borderwidth=0)
        save_button = Button(self.window, image=save_png, command=self.save_data,borderwidth=0)
        exit_button = Button(self.window, image=exit_png, command=self.exit_program, borderwidth=0)
        
        mind_button.pack(side=TOP, pady=10)
        munch_button.pack(side=TOP, pady=10)
        dashboard_button.pack(side=TOP, pady=10)
        save_button.pack(side=LEFT, pady=10)
        exit_button.pack(side=RIGHT, pady=10)
        
        self.window.mainloop()

    def mind_form(self):
        self.mind_health_form.form()

    def munch_form(self):
        self.physical_health_form.form()

    def dashboard(self):
        self.dashboard_view.dashboard()

    ########## SAVE & EXIT ##########
    def save_data(self):
        file_path = "mind_n_munch_data.json"
        try:
            with open(file_path, "w") as file:
                json.dump(self.history, file)
            messagebox.showinfo("Save", f"Data saved successfully to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {str(e)}")
    
    def exit_program(self):
        user_choice = messagebox.askyesnocancel("Exit", "Do you want to save before exiting?")

        if user_choice is not None:
            if user_choice:
                self.save_data()

            self.window.destroy()
            
    ########## UPLOAD & HISTORY & CLEAR ##########
    def upload_data(self):
        file_path = "mind_n_munch_data.json"

        try:
            with open(file_path, "r") as file:
                uploaded_data = json.load(file)

            self.history.extend(uploaded_data)

            messagebox.showinfo("Upload", "Data uploaded successfully!")
        except FileNotFoundError:
            messagebox.showinfo("Upload", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error uploading data: {str(e)}")
        
    def show_history(self):
        history_window = Toplevel(self.window)
        history_window.title("History")
        history_window.geometry("600x400")

        history_text = Text(history_window, wrap=WORD, font=("Helvetica", 12))
        history_text.pack(fill=BOTH, expand=YES)

        if self.history:
            for entry in self.history:
                history_text.insert(END, f"{entry}\n\n")
        else:
            history_text.insert(END, "No history available.")
            
    def clear_history(self):
        result = messagebox.askyesno("Clear History", "Are you sure you want to clear the history?")
        if result:
            self.history = []
            messagebox.showinfo("Clear History", "History cleared successfully!")


Mind_n_Munch()
