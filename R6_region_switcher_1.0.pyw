from tkinter import *
from tkinter import ttk
import os
from tkinter.messagebox import showinfo

path = f"{os.getenv('userprofile')}/Documents/My Games/Rainbow Six - Siege"
folder = os.listdir(f"{os.getenv('userprofile')}/Documents/My Games/Rainbow Six - Siege")[0]

data = open(f"{path}/{folder}/GameSettings.ini", "r").read()
configs = data.split("\n")
for i, config in enumerate(configs):
    if "DataCenterHint=" in config:
        value = config.replace("DataCenterHint=", "")
        index = i
        break

def BtnSaveListener():
    global configs
    global combobox
    configs[i] = f"DataCenterHint={combobox.get()}"
    open(f"{path}/{folder}/GameSettings.ini", "w").write("\n".join(configs))
    showinfo("Done", "Config saved.")
    

window = Tk()
window.title("")
window.resizable(False, False)
window.geometry("200x60")

dataCenterList = (  "default",
                    "playfab/australiaeast",
                    "playfab/brazilsouth",
                    "playfab/centralus",
                    "playfab/eastasia",
                    "playfab/eastus",
                    "playfab/japaneast",
                    "playfab/northeurope",
                    "playfab/southafricanorth",
                    "playfab/southcentralus",
                    "playfab/southeastasia",
                    "playfab/uaenorth",
                    "playfab/westeurope",
                    "playfab/westus"
                )




combobox = ttk.Combobox(window, textvariable="text", values=dataCenterList,width=25)
combobox.grid(column=0, row=0)
combobox.current(dataCenterList.index(value))
btnsave = ttk.Button(window, text="Save", command=BtnSaveListener)
btnsave.grid(column=0,row=1)
window.mainloop()
