import sys
import pyperclip
import json
#sssign name of the json file to a variable
savedData = "clipboard.json"

#save the item to the created clipboard
def save_item(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#load the items from the created clipboard
def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    

#take input of the user from the command promp
if(len(sys.argv))==2:
    cmd = sys.argv[1]
    data = load_items(savedData)

    if cmd == "save":
        key = input("Enter a key: ")
        data[key] = pyperclip.paste()
        save_item(savedData, data)
        print("Copied to clipboard")

    
    elif cmd == "load":
        key = input("Enter a key: ")
        if key in data:
            pyperclip.copy(data[key])
            print("data copied")
        else:
            print("Key not found")
    elif cmd == "list":
        print(data)
    
    else:
        print("Wrong command")
