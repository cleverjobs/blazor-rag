# Pass context to Click Handler

## Question

**Joe** asked on 11 Mar 2020

How can I pass the context of a TreeView's ItemTemplate to a click handler? This is what I have: <TelerikTreeView Data="@TreeData"> <TreeViewBindings> <TreeViewBinding IdField="Id" TextField="Text"> <ItemTemplate> @{ <TelerikButton OnClick="@OnClickHandler">@((context as TreeItem).Text)</TelerikButton> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code { public class TreeItem { public string Id { get; set; }=$"{Guid.NewGuid()}"; public string Text { get; set; } public ObservableCollection<TreeItem> Items { get; set; }=new ObservableCollection<TreeItem>(); public bool Expanded { get; set; } public bool HasChildren { get; set; } public bool Selected { get; set; } } private void OnClickHandler(TreeItem context) { }

## Answer

**Svetoslav Dimitrov** answered on 12 Mar 2020

Hello Joel, In the ItemTemplate you can directly pass the context as delegate. I have created a code snippet based on the demo you provided: @using System.Collections.ObjectModel

<TelerikTreeView Data="@TreeData">
<TreeViewBindings>
<TreeViewBinding IdField="Id" TextField="Text">
<ItemTemplate>
@{ var myContext=context as TreeItem; <TelerikButton OnClick="@(()=> OnClickHandler(myContext)) ">@myContext.Text</TelerikButton>
}
</ItemTemplate>
</TreeViewBinding>
</TreeViewBindings>
</TelerikTreeView>

@code { public ObservableCollection<TreeItem> TreeData { get; set; } public class TreeItem { public string Id { get; set; }=$" {Guid.NewGuid()} "; public string Text { get; set; } public ObservableCollection<TreeItem> Items { get; set; }=new ObservableCollection<TreeItem>(); public bool Expanded { get; set; } public bool HasChildren { get; set; } public bool Selected { get; set; }
} private void OnClickHandler ( TreeItem currentContext ) {

}

} Regards, Svetoslav Dimitrov
