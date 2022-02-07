from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
#import excelimport
#import funcionaltesting

gui = Tk()
gui.geometry("500x100")
gui.title("Funcional testing")


class Screen():
    def __init__(self, master):
        self.dfolderPath = StringVar()
        self.ifolderPath = StringVar()
        self.ofolderPath = StringVar()

        self.driver_text = Label(master, text="Vlož cestu pro driver:")
        self.driver_text.grid(row=0, column=0)

        self.dpath_field = Entry(master, textvariable=self.dfolderPath)
        self.dpath_field.grid(row=0, column=1)

        self.dfind_path = ttk.Button(master, text="Vyber driver", command=self.dfolder_path)
        self.dfind_path.grid(row=0, column=2)
        #
        self.input_text = Label(master, text="Vlož cestu s testovacími případy:")
        self.input_text.grid(row=1, column=0)

        self.ipath_field = Entry(master, textvariable=self.ifolderPath)
        self.ipath_field.grid(row=1, column=1)

        self.ifind_path = ttk.Button(master, text="Vyber složku", command=self.ifolder_path)
        self.ifind_path.grid(row=1, column=2)

        self.output_text = Label(master, text="Vlož cestu pro uložení výsledku testování:")
        self.output_text.grid(row=2, column=0)

        self.opath_field = Entry(master, textvariable=self.ofolderPath)
        self.opath_field.grid(row=2, column=1)

        self.ofind_path = ttk.Button(master, text="Vyber složku", command=self.ofolder_path)
        self.ofind_path.grid(row=2, column=2)

        # self.start_test = ttk.Button(master, text="Spustit testování", command=self.start_test)
        # self.start_test.grid(row=3, column=1)
        pass

    def ifolder_path(self):
        self.ifolder_selected = filedialog.askdirectory()
        self.ifolderPath.set(self.ifolder_selected)
        self.dir_files()

    def dfolder_path(self):
        self.file_selected = filedialog.askopenfilename()
        self.dfolderPath.set(self.file_selected)

    def ofolder_path(self):
        self.ofolder_selected = filedialog.askdirectory()
        self.ofolderPath.set(self.ofolder_selected)

    def dir_files(self):
        self.files = []
        for filename in os.listdir(self.ifolder_selected):
            f = os.path.join(self.ifolder_selected, filename)
            # checking if it is a file
            if os.path.isfile(f):
                self.files.append(f)
            else:
                pass
    # def start_test(self):
    #     for file in range(len(self.files)):
    #         funcionaltesting.Testcases().test_excecutions()
    #     pass

# if __name__ == '__main__':
#     s = Screen(gui)
#
#     gui.mainloop()
s = Screen(gui)

gui.mainloop()