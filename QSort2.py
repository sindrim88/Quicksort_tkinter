import random
from tkinter import *
import time

root = Tk()
w = Canvas(root, width=1200, height=600)

class QSort:

    def __init__(self,id):
        self.id = id
        self.arr_list = []

    def create_random_List(self, n,tempArr, width):
        for i in range(0, n):
            rand = random.randint(0,580)
            self.arr_list.append([i*width, 600-rand, i*width+width, 600])
            tempArr.append(QSort(w.create_rectangle(i*width, 600-rand, i*width+width, 600, fill="lightblue", outline = 'blue')))

    def quickSort(self, start, end, tempArr):
        if start < end:
            partitionIndex = self.partition(start, end, tempArr)
            self.quickSort(start, partitionIndex-1, tempArr)
            self.quickSort(partitionIndex+1, end, tempArr)

    def partition(self, start, end, tempArr):
        pivot = self.arr_list[end].__getitem__(1)
        i = (start-1)
        for j in range(start, end):

            if self.arr_list[j].__getitem__(1) > pivot:
                #time.sleep(0.0005)
                i = i+1

                tempSwap = self.arr_list[i]
                self.arr_list[i] = self.arr_list[j]
                self.arr_list[j] = tempSwap

                temp = tempArr[i]
                temp1 = tempArr[j]

                xmove = (w.coords(tempArr.__getitem__(j).id)[0] - w.coords(tempArr.__getitem__(i).id)[0])
                w.move(tempArr[i].id, xmove, 0)
                w.move(tempArr[j].id, -xmove, 0)

                tempArr.pop(i)
                tempArr.insert(i, temp1)
                tempArr.pop(j)
                tempArr.insert(j, temp)

                w.update()

        #time.sleep(0.0005)
        tempSwap2 = self.arr_list[i+1]
        self.arr_list[i+1] = self.arr_list[end]
        self.arr_list[end] = tempSwap2

        temp2 = tempArr[i+1]
        temp3 = tempArr[end]

        xMove =  (w.coords(tempArr.__getitem__(end).id)[0] - w.coords(tempArr.__getitem__(i+1).id)[0])
        w.move(tempArr[i+1].id, xMove, 0)
        w.move(tempArr[end].id, -xMove, 0)
        w.update()

        tempArr.pop(i+1)
        tempArr.insert(i+1, temp3)
        tempArr.pop(end)
        tempArr.insert(end, temp2)

        return i+1

if __name__ == '__main__':

    Arr = QSort("Sindris_List")
    tempArr = []
    Arr.create_random_List(600, tempArr, 2)

    w.pack()

    len = len(Arr.arr_list)
    Arr.quickSort(0, len -1, tempArr)
    w.mainloop()