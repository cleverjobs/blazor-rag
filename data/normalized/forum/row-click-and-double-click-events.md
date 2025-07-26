# Row click and double click events

## Question

**Nic** asked on 04 Jul 2019

Hi, Does the grid support click/double click events or is there any way I can support it on a given column. I'm building the columns dynamically as I am binding to custom types. The grid is only ever in read-only mode. I also have some columns that have anchors/links in them which is working fine. But when I double click anywhere other than a link I want to do an action using the context of the row. Thanks, Nick.

## Answer

**Nick** answered on 04 Jul 2019

I have gotten around this by implementing a row template and using ondblclick on the <td> elements!

### Response

**Marin Bratanov** answered on 08 Jul 2019

Hi Nick, At the moment, such events are not available and the solution you found is the way to do this. Of course, using a column template may also suffice if you want this action only for certain columns and not for the entire row. That said, a few hours before your request we received another that was literally the same, so I made this page so you can Follow the implementation of such events: [https://feedback.telerik.com/blazor/1417387-row-click-and-double-click-events.](https://feedback.telerik.com/blazor/1417387-row-click-and-double-click-events.) Your vote is already in. Regards, Marin Bratanov

### Response

**Andriy** answered on 12 Jul 2019

Tell me please, how I can use your controls without so important events? It's not about grid only. For example, what about TreeView? User clicks on node element and want to see the data in right part. Where I can take info about clicked node if you don't provide any event?

### Response

**Andriy** answered on 12 Jul 2019

I found solution for TreeView, may be it will be usefull for Grid also. Full fragment: <TelerikTreeView @ref="TreeView" Data="@TreeItems"> <TelerikTreeViewBindings> <TelerikTreeViewBinding IdField="Id" ParentIdField="TopId" ExpandedField="IsExpanded" TextField="ItemName" HasChildrenField="HasChildren"> <ItemTemplate Context="item"> @{ var inventoryTreeItem=item as InventoryTreeItemProxy; } <span @key=@inventoryTreeItem.Id @onclick=@((e)=> OnTreeItemClick(e, inventoryTreeItem))><strong>@inventoryTreeItem.ItemName</strong></span> </ItemTemplate> </TelerikTreeViewBinding> </TelerikTreeViewBindings> </TelerikTreeView> As a temporary solution will works.

### Response

**Marin Bratanov** answered on 15 Jul 2019

Hi Andriy, Templates in Blazor are much more powerful than templates in MVC or jQuery, because there is no longer such a great distinction between a server and a client and rendering on each. At the moment, using templates to wire up events like click, doubleclick, mouseover and so on is the correct approach. We are still considering whether it will make sense to expose them explicitly through our components, because, on the other hand, the usage of custom templates is likely to break built-in events by removing the markup we attach handlers internally. That said, feel free to add a public feature request for events you don't see yet in our

### Response

**Andriy** answered on 15 Jul 2019

Hi, Marin. Thank you very much for your answer.

### Response

**Marin Bratanov** answered on 17 Jul 2019

Hello Andriy, We just received another request for a built-in click event and I made now a public page you can Follow for status updates: [https://feedback.telerik.com/blazor/1418731-node-click-event.](https://feedback.telerik.com/blazor/1418731-node-click-event.) I've already added your vote so all you need to do is click Follow. I can't say at this point whether using templates will remain the preferred approach in the future, but you can get notifications from that page. Regards, Marin Bratanov

### Response

**hazelinesnow** answered on 06 May 2020

For blazor grid, we prefer "whole row" double click event, instead of using ondblclick on the <td> elements as Nick suggested. For example, the following: [https://docs.telerik.com/devtools/aspnet-ajax/controls/grid/client-side-programming/events/onrowdblclick](https://docs.telerik.com/devtools/aspnet-ajax/controls/grid/client-side-programming/events/onrowdblclick) Thanks

### Response

**Marin Bratanov** answered on 06 May 2020

Hello, At the moment, it is likely that click and doubleClick events will be exposed for the row, and if a specific cell needs a click - that would be handled through its own template. Regards, Marin Bratanov
