# Checkable TreeView loses checks on node collapse when OnExpand event handled

## Question

**Bri** asked on 16 May 2022

I am using a TreeView control that displays checkboxes for each node and the checked state of each node seems to get lost when the parent node is collapsed and expanded again. However, this only seems to happen when the OnExpand event is handled. Remove the OnExpand event handler and everything works as expected. It doesn't seem to make a difference if the event args property ShouldRender is set to true. Happens for both flat and hierarchical data. Can't imagine that this is the desired behaviour. If it is then is there any way around it as I do need to handle the OnExpand event in my code behind. The following is test page the displays this problem... @page "/treeview"
@using System.Linq <TelerikTreeView Data="@Data" CheckBoxMode="@TreeViewCheckBoxMode.Multiple" CheckChildren="true" CheckParents="true" @bind-CheckedItems="@CheckedItems" OnExpand="@OnExpandHandler"> @*@bind-ExpandedItems="@ExpandedItems"*@<TreeViewBindings> <TreeViewBinding IdField="Id" TextField="Text" HasChildrenField="HasChildren" ItemsField="Children"> <ItemTemplate> @{
var item=context as MyTreeItem; <div> @item.Id.ToString() : @item.Text </div> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code {
private IEnumerable <MyTreeItem> Data { get; set; }
private IEnumerable <object> CheckedItems { get; set; }=Enumerable.Empty <object> ();
private IEnumerable <object> ExpandedItems { get; set; }=Enumerable.Empty <object> ();
private int LastID=0;

protected override void OnInitialized()
{
Data=CreateNodeList("one", "two", "three", 3);
}

private List <MyTreeItem> CreateNodeList(string name1, string name2, string name3, int levels=0)
{
var list=new List <MyTreeItem> ();
list.Add(CreateNode(name1, levels));
list.Add(CreateNode(name2, levels));
list.Add(CreateNode(name3, levels));
return list;
}

private MyTreeItem CreateNode(string name, int levels)
{
LastID++;
var node=new MyTreeItem { Id=LastID, Text=name };
if (levels> 0)
{
node.Children=CreateNodeList($"{name} - one", $"{name} - two", $"{name} - three", levels - 1);
}
return node;
}

private async Task OnExpandHandler(TreeViewExpandEventArgs args)
{
//await InvokeAsync(StateHasChanged);
//args.ShouldRender=true;
}

private class MyTreeItem
{
public int Id { get; set; }=0;
public string Text { get; set; }="";
public IList <MyTreeItem> Children { get; set; }=null;
public bool HasChildren=> Children is not null && Children.Count> 0;
}
}

## Answer

**Tsvetomir** answered on 17 May 2022

Hi Brian, Thank you for the provided information and example. Indeed, it is a known defect that when the OnExpand event is declared, the checked children are lost. I recommend that you subscribe to the following item so that you get notified about status updates. [https://feedback.telerik.com/blazor/1558348-treeview-checkbox-state-is-not-maintained-when-using-onexpand](https://feedback.telerik.com/blazor/1558348-treeview-checkbox-state-is-not-maintained-when-using-onexpand) As an alternative, use JavaScript to handle the click event of the expand arrows and execute logic of your choice. Let me share more details on how to achieve this: 1. Add an element in the ItemTemplate of the TreeView that holds the id of the respective item: <ItemTemplate>
@{ var item=context as MyTreeItem; <span style="display: none;" data-itemid="@item.Id.ToString()"></span> <div>@item.Id.ToString() : @item.Text</div>
}
</ItemTemplate> 2. Override the OnAfterRenderAsync event: protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender==true )
{ await JS.InvokeAsync<string>( "attachClickToIcons" );
}
} 3. Attach the click event handler to the expand icon. Within the handler, invoke a .NET function and pass the id as an argument: function attachClickToIcons ( e ) { document.addEventListener( 'click', function ( e ) { if (e.target.classList.contains( 'k-i-expand' )) { const idHolderElement=e.target.closest( 'li' ).querySelector( '[data-itemid]' ); const id=idHolderElement.dataset.itemid;
DotNet.invokeMethodAsync( 'AssemblyName', 'ExpandHandler', id)
}
});
} 4. Accept the id in a JSInvokable .NET function: [ JSInvokable ] public static void ExpandHandler ( string id ) { // execute custom logic; } Let me know if additional information is required. Kind regards, Tsvetomir

### Response

**Brian** commented on 17 May 2022

Thanks, I'll give that a go.
