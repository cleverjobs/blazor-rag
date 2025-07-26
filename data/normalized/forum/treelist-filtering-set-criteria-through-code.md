# TreeList Filtering: Set criteria through Code

## Question

**Joe** asked on 15 Jul 2025

How do I set the TreeList filter through code? So, can I put a value in the criteria field from code behind? My TreeList <TelerikTreeList @ref=@TreeListRef Data="@Groups" SelectedItems="@SelectedGroups" IdField="@nameof(Group.Id)" ParentIdField="@nameof(Group.ParentId)" OnStateInit="((TreeListStateEventArgs<Group> args)=> OnStateInitHandler(args))" Pageable="true" PageSize="@GroupPageSize" Height="100%" Sortable="false" SelectionMode="TreeListSelectionMode.Single" FilterMode="@TreeListFilterMode.FilterMenu" @bind-Page="@GroupCurrentPage" SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Group> m)=> OnGroupSelected(m))"> <TreeListColumns> <TreeListColumn Field="Name" Title="Group Filter" Expandable="true"> <Template> @{
var item=context as Gsi.Customer.Models.Group; <img height="32" width="32" src="@item.ImageUrl" /> @item.Name
} </Template> </TreeListColumn> </TreeListColumns> </TelerikTreeList>

## Answer

**Georgi** answered on 17 Jul 2025

Hello Joel, Thanks for reaching out about programmatically setting filter criteria for the TelerikTreeList component. I'm providing an example using the Telerik Blazor REPL platform so you can easily view, run, and modify the code as needed. It demonstrates how to programmatically apply filters. You can also find a similar example and more details in the TelerikTreeList component documentation. This resource should provide everything you need to get started. I hope this helps. If you have any questions, please do not hesitate to reach out. Regards, Georgi Progress Telerik

### Response

**Joel** commented on 17 Jul 2025

Yep, thanks.
