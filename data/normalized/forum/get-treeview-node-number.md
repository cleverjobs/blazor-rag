# Get Treeview node number

## Question

**Chr** asked on 07 Dec 2023

I need to get the node number of the tree view. I know there is a TreeItem that has the Level property but I can't figure out how to get it. I tried using an Item Template and that is where I am stuck. I couldn't figure out how to get the item info. Here is my current tree view which works fine but I can't get the level. <div> This is the tree view <br /> <TelerikTreeView Data="TreeViewList"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentId" IdField="Id" HasChildrenField="HasChildren" TextField="Name"> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> </div>

## Answer

**Craig** answered on 08 Dec 2023

To get the level of a node in a TelerikTreeView, you can use the Level property of the TreeViewItem. Here’s an example of how to get the level of the selected item in a TelerikTreeView: private void TreeView_SelectedItemChanged(object sender, RoutedPropertyChangedEventArgs<object> e) { Telerik.Windows.Controls.RadTreeViewItem selectedItem=e.NewValue as Telerik.Windows.Controls.RadTreeViewItem; int level=selectedItem.Level; // Do something with the level... } In this example, the TreeView_SelectedItemChanged event is used to get the selected item in the TelerikTreeView. The Level property of the selected item is then used to get the level of the item. You can then use the level to perform any additional actions you need. blossom word game

### Response

**Chris** commented on 08 Dec 2023

Thanks for that but I don't have any user actions to trigger it. I need it on load and I can't find an "OnLoad" event for the control. Sorry I didn't specify that. I did look at the item "onclick" and "onrender" events but it only passes back the item object. I an set up a template for every level but that requires that I know how many levels there are and I have to hardcode all that which is yucky. I don't get how I can test the level number in the binding but I cant read it! <TreeViewBinding Level="2" TextField="ProductName"> <ItemTemplate> @{
TreeViewDTO item=context as TreeViewDTO;
@string.Concat("2 ", item.Name);
} </ItemTemplate> </TreeViewBinding>
