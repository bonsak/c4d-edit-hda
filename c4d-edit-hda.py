import c4d
from c4d import gui
from c4d import documents
import subprocess


def main():
    # Check if theres a document present
    if documents.GetActiveDocument() is None: 
        gui.MessageDialog("No document!")
        return False
    
    doc = documents.GetActiveDocument()
    
    # Check if the user has selected an object
    if doc.GetActiveObject() is None: 
        gui.MessageDialog("Please select a Houdini Asset")
        return False
    
    o = doc.GetActiveObject()
    
    # Check if the object is an H asset
    if o.GetType() != 1032271: 
        gui.MessageDialog("Please select a Houdini Asset")
        return False
    
    print o.GetType()    
    bc = o.GetDataInstance()
    
    # Set this to your Houdini install path
    houdini = "/Applications/Houdini 14.0.400/Houdini FX.app/Contents/MacOS/houdinifx"
    hda = ""
    
    # Find the Basecontainer key 3000 to get the hda path
    for key, val in bc:
        if key == 3000:
            hda = val
            print key, val

    # Start Houdini and pass in the path to the HDA
    subprocess.call([houdini, hda])
    
if __name__=='__main__':
    main()