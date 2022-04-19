# Sets the Display Color of all children to the Display Color of root (selected)

import c4d
from c4d import gui

def main():
    gui.MessageDialog('Synchronizing colors of children')
    doc.StartUndo()

    DRV_color = c4d.Vector(.45,.4,1)
    GEO_color = c4d.Vector(.8,.4,.1)
    DEF_color = c4d.Vector(.85,.1,.1)
    RIG_color = c4d.Vector(.25,.6,.5)
    CTRL_color = c4d.Vector(1,1,1)
    Site_color = c4d.Vector(.5,.5,.5)

    for root in doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER):
        children = UnfoldRig(root)
        for child in children:
            # Check name for prefix and pick the hardcoded color
            color = c4d.Vector() # init
            if child.GetName()[:4] == "DRV_":
                color = DRV_color
            elif child.GetName()[:4] == "GEO_":
                color = GEO_color
            elif child.GetName()[:4] == "DEF_":
                color = DEF_color
            elif child.GetName()[:4] == "RIG_":
                color = RIG_color
                #child[c4d.ID_BASEOBJECT_XRAY] = False
            elif child.GetName()[:5] == "CTRL_":
                color = CTRL_color
                child[c4d.ID_BASEOBJECT_USECOLOR] = 2
            elif child.GetName() == "Site":
                color = Site_color
                # Hide Site too
                child[c4d.ID_BASEOBJECT_XRAY] = False
                child[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
                child[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
            else:
                color = GEO_color
            # Set color
            doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, child)
            child[c4d.ID_BASEOBJECT_COLOR] = color

    doc.EndUndo()
    c4d.EventAdd()
    return


# Utility
def UnfoldRig(root):
    """Returns an object and its children as a python list."""
    objlist = []
    objlist.append(root)
    if root.GetDown() != None:
        UnfoldRig_recurse(root.GetDown(), objlist)
    return objlist
def UnfoldRig_recurse(root, objlist):
    objlist.append(root)

    if root.GetDown() != None:
        objlist = UnfoldRig_recurse(root.GetDown(), objlist)

    if root.GetNext() != None:
        objlist = UnfoldRig_recurse(root.GetNext(), objlist)

    return objlist

if __name__=='__main__':
    main()