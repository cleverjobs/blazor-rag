# Treelist blazor popup does not close after update

## Question

**ITG** asked on 05 Jul 2021

Hello Team In Treelist the popup does not close after the update is something wrong with this code ? <TelerikTreeList Data=@vm.Model IdField="Id" ParentIdField="ParentId" Sortable=true Pageable=true EditMode="@TreeListEditMode.Popup" SelectionMode="@TreeListSelectionMode.Single" OnCreate="@CreateItem" OnUpdate="@UpdateItem" OnDelete="@DeleteItem"> <TreeListToolBar> <TreeListCommandButton Command="Add" Icon="add">Add</TreeListCommandButton> </TreeListToolBar> <TreeListColumns> <TreeListColumn Field=@nameof(ModelHierarchyInfo.Name) Expandable="true" Width="250px"></TreeListColumn> <TreeListColumn Field=@nameof(ModelHierarchyInfo.Designation)></TreeListColumn> <TreeListCommandColumn Width="220px"> <TreeListCommandButton Command="Add" Icon="add"></TreeListCommandButton> <TreeListCommandButton Command="Edit" Icon="edit"></TreeListCommandButton> <TreeListCommandButton Command="Delete" Icon="delete"></TreeListCommandButton> <TreeListCommandButton Command="Save" Icon="save" ShowInEdit="true"></TreeListCommandButton> <TreeListCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"></TreeListCommandButton> </TreeListCommandColumn> </TreeListColumns> </TelerikTreeList>

### Response

**Marin Bratanov** commented on 07 Jul 2021

Could you check if you are getting the circular reference exception described here: [https://feedback.telerik.com/blazor/1526681-navigable-causes-circular-reference-exception?](https://feedback.telerik.com/blazor/1526681-navigable-causes-circular-reference-exception?) If not, please open a support ticket and post a runnable project that showcases the problem with the latest version (2.25.0 at the time of writing), because this demo that runs on it seems to work fine for me: [https://demos.telerik.com/blazor-ui/treelist/editing-popup.](https://demos.telerik.com/blazor-ui/treelist/editing-popup.) With the provided information, I could only guess that there is some application exception in places like the OnUpdate or OnCreate handlers.
