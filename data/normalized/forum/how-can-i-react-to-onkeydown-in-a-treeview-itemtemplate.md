# How can I react to @onkeydown in a TreeView ItemTemplate?

## Question

**Tri** asked on 25 Oct 2023

As the title says, I am trying to use the @onkeydown Event in a TreeView ItemTamplate. The reason for doing this is so I can manipulate the default navigation behaviour of the TreeView and immediately select an item when using the Up and Down Arrows instead of having to press the Enter key. I am aware of the documentation that shows how to react to @onclick Blazor Treeview - Templates - Telerik UI for Blazor. I can get @onclick to work but not @onkeydown or any other input related events besides mouse events. Using Telerik 3.6.0 Below is a code sample which shows what I am trying to do but is not working. When debugging and setting a breakpoint in the NodeKeyDown Method, I can not reach it. <TelerikTreeView Data=“@TreeData”> <TreeViewBindings> <TreeViewBinding> <ItemTemplate> @{ TreeItem itm=context as TreeItem; <span @onkeydown=“@(_=> NodeKeyDown(_))” tabindex=“0”> Node: <strong> @itm.Text </strong> </span> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> <label id=“result”> @result </label> @code { string result { get; set; }

async Task NodeKeyDown(KeyboardEventArgs args)
{
result=$"You pressed key: {args.Code}";
}

// sample data
public IEnumerable <TreeItem> TreeData { get; set; }

public class TreeItem
{
public string Text { get; set; }
public int Id { get; set; }
public List <TreeItem> Items { get; set; }=new List <TreeItem> ();
public bool HasChildren { get; set; }
}

protected override void OnInitialized()
{
LoadHierarchical();
}

private void LoadHierarchical()
{
List <TreeItem> roots=new List <TreeItem> ()
{
new TreeItem { Text="Item 1", Id=1, HasChildren=true },
new TreeItem { Text="Item 2", Id=2, HasChildren=true }
};

roots[0].Items.Add(new TreeItem { Text="Item 1 first child", Id=3 });
roots[0].Items.Add(new TreeItem { Text="Item 1 second child", Id=4 });
roots[1].Items.Add(new TreeItem { Text="Item 2 first child", Id=5 });
roots[1].Items.Add(new TreeItem { Text="Item 2 second child", Id=6 });

TreeData=roots;
}

## Answer

**Svetoslav Dimitrov** answered on 30 Oct 2023

Hello, The onkeydown event is, as you rightfully mentioned, used for keyboard navigation. The ArrowUp and ArrowDown keys are also coded to perform specific operations. At that point, we have an open feature request for the ability to customize the keyboard shortcuts. Once this feature request is implemented you will be able to achieve the desired behavior. I have added your Vote for it and you can click the Follow button to receive email notifications on status updates. Until we release this request I am sorry to report that there is no feasibile way to make the ArrowUp and ArrowDown Keys to navigate to a different page. Regards, Svetoslav Dimitrov Progress Telerik
