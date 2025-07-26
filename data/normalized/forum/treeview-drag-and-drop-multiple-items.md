# TreeView drag and drop multiple items

## Question

**Ale** asked on 05 Jul 2021

seems even having multiple selection we just can drag and drop items one by one, am I right? basically having access to selected items & grop event i can code workaround & move them myself, but hope that we have it out of the box, do we?

### Response

**Marin Bratanov** commented on 06 Jul 2021

The item selection and item dragging are generally slightly separate features, one does not really require the other. I am not sure I completely understand the issue, though, so I would encourage you to edit the opener post to provide some more details on the problematic scenario.

### Response

**Aleksandr** commented on 06 Jul 2021

set treeview selection type to multiple, select several items, try to drag, just one item will be dragged despite having several selected

## Answer

**Hristian Stefanov** answered on 09 Jul 2021

Hello Aleksandr, Thanks to your question, we have opened a feature request for the described functionality in our public

### Response

**Andrew** answered on 28 Jun 2022

Aleksandr, I have the same requirement and was able to support it with minimal effort. In the drop event use this technique. If the tree selection contains the dragged item then the user dragged the entire selection and you can use TreeSelection (property bound to SelectedItems) as the list of what was dragged. If on the otherhand TreeSelection does NOT contain the drag item, then the user made a selection but dragged a different node. In this scenario the dragged node (from arg.Item) is the only item that was dragged. var selectedItems=TreeSelection.OfType<TreeViewModel>().ToList(); var draggedItem=arg.Item as TreeViewModel; if (!selectedItems.Contains(draggedItem)) selectedItems=new List<TreeViewModel>() { draggedItem }; Good luck, -Andy
