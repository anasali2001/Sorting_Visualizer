from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import random
from colors import *
from random import randint
from tkinter import font
import tkinter as tk

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.bucketSort import bucketSort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort


# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = LIGHT_GRAY)


N = 10

algorithm_name = StringVar()
file_name = StringVar()
data = []
file_list = ['Small File', 'Medium File', 'High File']
algo_list = ['Bubble Sort', 'Insertion Sort', 'Bucket Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 4
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 310
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


def set_speed():
    return 0.5


def GenerateFiles():
        # GENERATE THREE FILES
        print("Generating Files.....")

        f1 = open("small.txt", "w")
        for i in range(10):
            i = randint(100, 150)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        f1 = open("medium.txt", "w")
        for i in range(1000):
            i = randint(100, 999)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        f1 = open("high.txt", "w")
        for i in range(1000000):
            i = randint(100000, 999999)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        print("Small, Medium and High files generated successfully.....")

canvas = Canvas(window, width=800, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=10, pady=5)


def openfile():
    global data
    timeTick = set_speed()
    filepath = filedialog.askopenfilename()
    read = open(filepath,"r")
    data = []
    for N in read:
            data.append(int(N))
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
        val = str(len(data) * len(data))
        complexity = "Complexity = O(N*N) = " + val
        canvas.create_text(400, 40, text=complexity, fill=WHITE, font=('Helvetica','15','bold'))
    elif algo_menu.get() == 'Bucket Sort':
        bucketSort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)
    


### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg=LIGHT_GRAY)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=LIGHT_GRAY)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list, width=115, height=15)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l1 = Label(UI_frame, text="File Size: ", bg=LIGHT_GRAY)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
file_menu = ttk.Combobox(UI_frame, textvariable=file_name, values=file_list, width=115, height=15)
file_menu.grid(row=1, column=1, padx=5, pady=5)
file_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=10, pady=5)
    

b2 = Button(UI_frame, text="Select File",command=openfile, bg=LIGHT_GRAY)
b2.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Files",command=GenerateFiles, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()