# How can I add css style for selected treeview item.

## Question

**Bee** asked on 28 Feb 2022

Hello Support Team, I have a Item Template for my Treeview. I want to make the background color different for my selected item and let it stick. When the user selects another item, it should highlight that selected item and other items should look normal. <TelerikTreeView Data="@DefectTreeView" @bind-ExpandedItems="@ExpandedItems" SelectionMode="TreeViewSelectionMode.Single"> <TreeViewBindings> <TreeViewBinding IdField="DefectCategoryID" ParentIdField="ParentID" TextField="DefectCategoryName" HasChildrenField="HasChildren" IconField="folder-open"> <ItemTemplate> @{
var item=context as DefectDefectCategory_TreeViewResultModel;
var chkenabled=false;
var chkvalue=false;
if (item.HasChildren==false && item.ChildrenCount==0)
{
chkenabled=true; <div style="padding-right: 4px;"> <TelerikCheckBox Enabled="chkenabled" Id="chkDelete" Title="Check to Delete Category" ValueChanged="@((bool value)=> GetSelectedTreeItemsDelete(value,item.DefectCategoryID))"> </TelerikCheckBox> </div> }
var itemname=item.DefectCategoryName.ToString() + " (" + item.ChildrenCount.ToString() + ")";
@itemname;
} </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> How do I set the css style to show the selected item. Thank you.

### Response

**Marin Bratanov** commented on 28 Feb 2022

I think that the treeview will add k-item-selected class on root HTML node of selected items so that you can cascade your CSS rules through that in order to differentiate a selected and non-selected one.

### Response

**Ben** commented on 29 Mar 2022

I'm still learning too but I just added this to my code and it worked. .k-treeview-leaf.k-selected {
background-color: #cccccc !important;
}
