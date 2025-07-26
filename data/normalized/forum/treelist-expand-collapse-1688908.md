# TreeList Expand/Collapse

## Question

**Joe** asked on 28 May 2025

I copied this example and got it working: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/treelist-expand-nodes-programmatically](https://www.telerik.com/blazor-ui/documentation/knowledge-base/treelist-expand-nodes-programmatically) Can you tell me how to default my TreeList to have everything expanded when my page loads? It seems running the SetTreeListExpandedItems after loading my data does not expand everything automatically... which is confusing to me. <TelerikCard> <CardBody Class="gsi-padding-0"> <TelerikButton OnClick="@SetTreeListExpandedItems" Class="gsi-width-100pct"> Expand/Collapse Groups </TelerikButton> </CardBody> </TelerikCard> <TelerikTreeList @ref=TreeListRef Data="@Groups" SelectedItems="@SelectedGroups" IdField="@nameof(Gsi.Customer.Models.Group.Id)" ParentIdField="@nameof(Gsi.Customer.Models.Group.ParentId)" OnStateInit="((TreeListStateEventArgs<Gsi.Customer.Models.Group> args)=> OnStateInitHandler(args))" Pageable="false" Sortable="false" SelectionMode="TreeListSelectionMode.Single" FilterMode="@TreeListFilterMode.FilterMenu" SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Group> m)=> OnGroupSelected(m))"> <TreeListColumns> <TreeListColumn Field="Name" Title="Group Filter" Expandable="true"> <Template> @{
var item=context as Gsi.Customer.Models.Group; <img height="32" width="32" src="@item.ImageUrl" /> @item.Name
} </Template> </TreeListColumn> </TreeListColumns> </TelerikTreeList>

## Answer

**Justin** answered on 30 May 2025

Hello Joel, Thank you for the question. I can first point out that, it is the default behavior of the TreeList, to have all Expandable nodes expanded when the component first initializes. In the example you have referenced, this default behavior is changed, when in the OnStateInit method, the ExpandedItems collection is set to a new empty list. I can also point out that the example you are referencing uses Hierarchical Data where as it seems your code below uses Flat Data. That said, I suggest looking through the Flat Data documentation to ensure that the model properties Id and ParentId are set up correctly. Then check to ensure that, in the OnStateInit, you are not setting a new empty list to the ExpandedItems collection. This should result in the all of the Nodes of the TreeList being expanded by default. Additionally, because the logic from the example in the SetTreeListExpandedItems method is dependent on the Hierarchical Data Binding model, this would need to be adjusted to get the same effect when binding to Flat Data. In this case, it should be sufficient to simply set the ExpandedItems collection to all items in the Data. This worked for me locally. However, it would be more accurate to include a HasChildren field to the Model and then only add the items where HasChildren=true to the ExpandedItems collection. I hope this helped. Regards, Justin Progress Telerik

### Response

**Joel** commented on 13 Jun 2025

If the "default" expanded behavior acted consistently then I wouldn't have gone down this road. It seems on first load it is as you say, expanded. However, any modification to the list and even requesting a Rebind on the control leaves the list closed.

### Response

**Justin** answered on 16 Jun 2025

Hi Joel, Indeed, the issue you are running into is considered a bug as described in the Feedback Portal item: Rebinding collapses TreeList. Please see the Portal Item for more details. I have added your vote to the item to increase its priority and so that you will be notified when changes are made to its status. Regards, Justin Progress Telerik

### Response

**Joel** commented on 16 Jun 2025

Okay. Well... here is my method in case anyone is interested. Whenever I reload my backing data, I call this with a "true" parameter: private async Task SetTreeListExpandedItems(bool? expand=null)
{
if (TreeListRef.IsNotNull())
{
if (!(TreeListRef.GetState().ExpandedItems.Count> 0) ||
expand.HasValue && expand.Value)
{
List <Group> toExpand=new List <Group> ();
foreach (Group item in Groups)
{
toExpand.Add(item);
if (item.Children.Any())
{
foreach (Group child in item.Children)
{
toExpand.Add(child);
}
}
}

var expandedState=new TreeListState <Group> ()
{
ExpandedItems=new List <Group> (toExpand)
};

await TreeListRef.SetStateAsync(expandedState);
}
else
{
var expandedState=new TreeListState <Group> ()
{
ExpandedItems=new List <Group> ()
};

await TreeListRef.SetStateAsync(expandedState);
}
}
}
