from tkinter import *
from tkinter.ttk import *

next_free_id = 0
class globalvars:
    itemCount=1
var=globalvars()

class Location:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Item:
    locationid = -1
    def __init__(self, name, id):
        self.name = name
        self.id = id

items = []
locations = []
#Load Settings
settings = open("settings", "r")
paramaters=settings.read().split("\n")
settings.close()

HOST=paramaters[0]
PORT=paramaters[1]

root=Tk()
root.title("Sound and Lights Inventory Sy stem")
root.minsize(width=700, height=420)

frame = Frame(root)
def save():
    print("Saving")
    itemfile=open("items.csv", "w")
    for item in items:
        itemfile.write(item.name+",")
        itemfile.write(str(item.id)+",")
        itemfile.write(str(item.locationid)+"\n")
    itemfile.close()
def savebind(event):
    save()
def load():
    itemfile=open("items.csv", "r")
    rows=itemfile.read().split("\n")
    itemfile.close()
    for row in rows:
        values=row.split(",")
        if not values==['']:
            items.append(Item(values[0],values[1]))
            items[var.itemCount-1].locationid=values[2]
    for item in items:
        valid=False
        trycount=0
        addtext=""
        while not valid:
            try:
                itemlist.insert("", var.itemCount, text=item.name + addtext,values=(item.id))
            except TclError:
                trycount+=1
                addtext=str(trycount)
            else:
                var.itemCount+=1
                valid=True
def newItem(event):
    items.append(Item("New Item", next_free_id))
    itemlist.insert("", var.itemCount, text=items[var.itemCount-1].name,values=(items[var.itemCount-1].id))
    var.itemCount+=1
def getItemIndexByName(name):
    ga=0
    for item in items:
        if(item.name==name):
            return ga
        else:
            ga+=1
def select(event):
    print("Selected Menu Item")
    selected = itemlist.item(itemlist.selection()[0])["text"]
    theItem = items[getItemIndexByName(selected)]
    itemNameEntry.delete(0,"end")
    itemNameEntry.insert(0,theItem.name)



#Begin UI Initialisation
#Itemlist
itemlist=Treeview(root)
itemlist.heading("#0", text="Name")
itemlist["columns"]=("1")
itemlist.column("1",width=50)
itemlist.heading("1",text="id")
itemlist.bind("<Double-1>", select)
itemlist.grid(row=2,column=1,padx=10,pady=10)
#Name tag
Label(root,text="Name:").grid(row=3,column=0)
#Save Button
saveButton=Button(text="Save")
saveButton.bind("<Button-1>",savebind)
saveButton.grid(row=1,column=0)
#Add New button
newItemButton=Button(text="New Event")
newItemButton.bind("<Button-1>",newItem)
newItemButton.grid(row=0,column=1)
#Name Entry
itemNameEntry=Entry(root,width=25)
itemNameEntry.grid(row=3,column=1)
#Begin loading
load()
#Starting UI
root.mainloop()