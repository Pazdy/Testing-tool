from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import excelimport
import funcionaltesting
import pandas as pd







class Screen():
    def __init__(self):

        self.gui = Tk()
        self.gui.geometry("800x300")
        self.gui.title("Testing tool")
        self.gui.iconbitmap("logo.ico")

        self.dfolderPath = StringVar()
        self.ifolderPath = StringVar()
        self.ofolderPath = StringVar()

        self.left_frame = Frame(self.gui, width=400, height=300)
        self.left_frame.grid(row=0, column=0)

        self.bg = PhotoImage(file="photo.gif", width=400, height=300)
        self.bg_label = Label(self.left_frame, image=self.bg)
        self.bg_label.grid(row=0, column=0)

        self.right_frame = Frame(self.gui, width=400, height=300, bg="white")
        self.right_frame.grid(row=0, column=1)

        self.logo = PhotoImage(file="logo.gif", width=75, height=75)
        self.logo_label = Label(self.right_frame, image=self.logo, bd=0)
        self.logo_label.place(x=285, y=215)

        self.driver_text = Label(self.right_frame, text="Vlož cestu pro driver:", bg="white")
        self.driver_text.place(x=25, y=25)

        self.dpath_field = Entry(self.right_frame, textvariable=self.dfolderPath, bd=4, width=40)
        self.dpath_field.place(x=25, y=45)

        self.dfind_path = ttk.Button(self.right_frame, text="Vyber driver", command=self.dfolder_path)
        self.dfind_path.place(x=285, y=44)

        self.input_text = Label(self.right_frame, text="Vlož cestu s testovacími případy:", bg="white")
        self.input_text.place(x=25, y=90)

        self.ipath_field = Entry(self.right_frame, textvariable=self.ifolderPath, bd=4, width=40)
        self.ipath_field.place(x=25, y=110)

        self.ifind_path = ttk.Button(self.right_frame, text="Vyber složku", command=self.ifolder_path)
        self.ifind_path.place(x=285, y=109)

        self.output_text = Label(self.right_frame, text="Vlož cestu pro uložení výsledku testování:", bg="white")
        self.output_text.place(x=25, y=155)

        self.opath_field = Entry(self.right_frame, textvariable=self.ofolderPath, bd=4, width=40)
        self.opath_field.place(x=25, y=175)

        self.ofind_path = ttk.Button(self.right_frame, text="Vyber složku", command=self.ofolder_path)
        self.ofind_path.place(x=285, y=174)

        self.start_test = ttk.Button(self.right_frame, text="Spustit testování", command=self.start_test)
        self.start_test.place(x=110, y=235)

        self.gui.mainloop()
        pass

    def ifolder_path(self):
        self.ifolder_selected = filedialog.askdirectory()
        self.ifolderPath.set(self.ifolder_selected)
        self.dir_files()

    def dfolder_path(self):
        self.dfolderPath = StringVar()
        self.file_selected = filedialog.askopenfilename()
        self.dfolderPath.set(self.file_selected)

    def ofolder_path(self):
        self.ofolder_selected = filedialog.askdirectory()
        self.ofolderPath.set(self.ofolder_selected)

    def dir_files(self):
        self.files = []
        self.filenames = []
        for filename in os.listdir(self.ifolder_selected):
            self.filenames.append(filename)
            f = os.path.join(self.ifolder_selected, filename)
            # checking if it is a file
            if os.path.isfile(f):
                self.files.append(f)
            else:
                pass
#        excelimport.excel_import(self.files)

    def start_test(self):
        self.create_result = pd.DataFrame().to_excel(excel_writer=self.ofolder_selected + "/result_file.xlsx")
        for file in self.files:
            self.number = self.files.index(file)
            excelimport.e_import(file)
            self.file = excelimport.e_import.configuration
            funcionaltesting.Testcases().test_excecution(configuration=self.file, path=self.file_selected, opath=self.ofolder_selected + "/result_file.xlsx", test=self.filenames[self.number])
        quit()

# if __name__ == '__main__':
#     s = Screen(gui)
#
#     gui.mainloop()
Screen()
