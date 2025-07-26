# TelerikTreeList Hierarchy Datasource Expand all items when reloading data

## Question

**Dew** asked on 09 May 2025

I'm using a TelerikTreeList to display a hierarchical data source. This data source has 5+- levels. The first time the TreeList loads, all the items are expanded as we want. When the user changes their search criteria of the data and I reload the data, the TreeList items are collapsed. We would like them to be expanded. I've tried the TreeListRef.SetStateAsync(expandedState) example, but it only shows the items expanded to the second node. I've verified I have a new object reference to the data source and I've tried an observable collection. I've used the TreeListRef.Rebind() method. I'm using Telerik.UI.for.Blazor 8.1.1. Thanks! below is the code I'm using: this is my TreeList <TelerikTreeList @ref="@TreeListRef" Data="@TreeData" ItemsField="@(nameof(Leaf.Children))" HasChildrenField="@(nameof(Leaf.HasChildren))" Width="900px"> <TreeListColumns> <TreeListColumn Expandable="true" Field="Text" Title="Text" /> <TreeListColumn Field="Code" Title="Code" Width="100px" /> <TreeListColumn Field="Description" Title="Description" Width="250px" /> </TreeListColumns> </TelerikTreeList> this is my method that loads the data. It is used for the first time as well as all subsequent searches. protected async Task SearchOrg() { var data=await _service.GetData(this.SelectedMemberId, this.TextBoxValue); TreeData=new List<Leaf>(data); // var expandedState=new TreeListState<Leaf>() // { // ExpandedItems=new List<Leaf>(data) // }; // await TreeListRef.SetStateAsync(expandedState); // TreeListRef.Rebind(); } this is my item class public class Leaf { public List<Leaf> Children { get; set; } public Leaf? Parent { get; private set; } //public int Id { get; set; } //public int? ParentId=> Parent?.Id; public string? Text { get; set; } public string? Code { get; set; } public string? Description { get; set; } public int Depth { get; private set; } public bool HasChildren=> Children.Any(); public Leaf(Leaf? parent) { this.Parent=parent; this.Children=new List<Leaf>(); if (parent==null) this.Depth=0; else this.Depth=parent.Depth+1; } }

## Answer

**Dimo** answered on 14 May 2025

Hello Dewayne, Indeed, this is a known issue. A possible easy workaround is to override the Equals () method of the Leaf class. In general, you can also control the TreeList expanded items at any time thorough the TreeList state. Regards, Dimo Progress Telerik

### Response

**Dewayne** commented on 14 May 2025

Thanks Dimo!! Overriding the Equals method worked. Dewayne
