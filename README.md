# Read Before You Try
ClipBoard python project <br>

This is a simple python clipboard project where you can copy "n" number of text into a clipboard created by my python program.

Usually Windows only lets us copy one item into our clipboard, in this program we can store mmultiple texts into our clipboard and access them using keys assigned to each item.

Once the program is run, the program will create a json file and add the items into it, which can be accessed whenever needed.
First you need to have a text copied in your clipboard and when you run the save command<b>from commands to use in command promp</b>, it will get added into the json file.


This program imports libraries like json, sys and pyperclip, so make sure you have these libraries downloaded.
<b>To download libraries through pip : </b><br>
pip install sys //for sys<br>
pip install json //for json<br>
pip install pyperclip //for pyperclip<br><br>

You can see multiple functions, each has a specific task to copy an item into the clipboard or to show items in the clipboard.

This is a simple python program and anyone with basic python programming experience can understand it.

<b> Commands to use in command promt</b>
<br>python clipboard.py save //to save whatever you have copied to clipboard
It will as for a key to be assigned to the item. The user can access that item using the repective key

python clipboard.py load //to load particular item from all items stored in the clipboard
This will let the user paste the selected item from the clipboard

python clipboard.py list //to show all items that are stored in clipboard
