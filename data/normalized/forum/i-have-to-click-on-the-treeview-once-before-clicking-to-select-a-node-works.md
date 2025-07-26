# I have to click on the TreeView once before clicking to select a node works

## Question

**Ros** asked on 01 Jun 2022

I have a simple project with a dropdownlist of items and a treeview. When an item is selected in the dropdownlist the treeview is populated. When I select an item from the dropdownlist, my tree populates as expected, but when I click on a node in the tree, nothing happens. If I click on the node again, then it selects the node as expected. Note that first click can be anywhere on the treelist component - its like I have to click on the component to seemingly "focus" it before the TreeView responds to clicks to select a node. I am using SelectionMode as Single and TreeView.OnItemClick to detect the selection, but it is clear the first click is ignored because the built-in selection highlighting does nothing on the first click and correctly changes the selection on subsequent clicks. Is there some way I can get the TreeView to simply accept clicks for selection without clicking on the component to "focus" it first? Here is my treeview reference: <TelerikTreeView Data="@treeItems" SelectedItems="SelectedTreeItems" SelectionMode="@TreeViewSelectionMode.Single" OnItemClick="@(args=> InvokeSelectedViewChanged((WellTreeItem)args.Item))"> <TreeViewBindings> <TreeViewBinding TextField="Name" ItemsField="Subitems"></TreeViewBinding> <TreeViewBinding Level="1" TextField="Name"></TreeViewBinding> </TreeViewBindings> </TelerikTreeView>

### Response

**Hristian Stefanov** commented on 03 Jun 2022

Hi Ross, The described behavior sounds indeed like an issue with the focus. I carefully followed the scenario and tried to mimic it in this REPL link. As a result, the TreeView selection seems to work on the first click on my machine. Please run and test it to see if the result you get is the same. Maybe the above example I prepared misses detail from the configurations in the actual application. If the problem is still there and if it's convenient, modify the example from the REPL link to reproduce the behavior and send it back here. This will allow me to investigate further and suggest next steps. I look forward to your reply.
