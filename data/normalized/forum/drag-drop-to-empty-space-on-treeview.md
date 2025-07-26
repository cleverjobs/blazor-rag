# Drag & Drop to empty space on TreeView

## Question

**And** asked on 28 Jun 2022

Hello, The Drag & Drop operation between treeviews is difficult when the tree is empty or mostly empty. The only valid drop targets are existing nodes. I would like to see the empty space in a treeview also available as a drop target. Can we log this as a request? In the meantime is it possible to drop a node on an empty treeview? Thank You, -Andy

## Answer

**Nadezhda Tacheva** answered on 01 Jul 2022

Hi Andrew, By design of the TreeView, valid drop targets are indeed only the component items. To handle dropping in an empty TreeView, you may add a dummy node to serve as a drop target. You may find more details in the following article - It is not possible to drop item to empty TreeView. A possible option to have a larger drop target is to create a custom one. You can use an ItemTemplate to override the default rendering of the items. If the TreeView data has only the dummy item, you may conditionally render a larger container for it. Regards, Nadezhda Tacheva Progress Telerik
