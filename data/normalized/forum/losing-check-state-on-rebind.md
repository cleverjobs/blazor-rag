# Losing Check State on rebind?

## Question

**Tho** asked on 19 Apr 2024

I have the following page: @page "/test"
@using System.Collections.ObjectModel <TelerikToolBar Class="toolbar-size" Adaptive="false"> <ToolBarButton Icon="@SvgIcon.FileAdd" OnClick="@OnAdd"> Add </ToolBarButton> </TelerikToolBar> <TelerikSplitter Height="500px"> <SplitterPanes> <SplitterPane Size="20%" Collapsible="true"> <TelerikTreeView Data="@Items" @bind-CheckedItems="@CheckedItems" CheckBoxMode="TreeViewCheckBoxMode.Multiple"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentIdValue"> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> </SplitterPane> <SplitterPane Collapsible="true"> </SplitterPane> </SplitterPanes> </TelerikSplitter> @code {

public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentIdValue { get; set; }
public bool HasChildren { get; set; }
public ISvgIcon Icon { get; set; }
}

public ObservableCollection <TreeItem> Items { get; set; }=new ObservableCollection <TreeItem> ();
public IEnumerable <object> CheckedItems { get; set; }=new List <object> ();

private int counter;

private void OnAdd()
{
this.Items.Add(new TreeItem { Id=counter, Text=$"test {counter}" });
counter++;
}
} If I add some items with the add button, then check some items, and then add some more items, the check state seems to be lost. However, if I collapse and expand the split panel, the items get checked again. Is this a bug, or what am I doing wrong?

## Answer

**Hristian Stefanov** answered on 24 Apr 2024

Hi Thomas, A bug report has already been submitted on our public feedback portal that covers the described behavior: TreeView does not respect any overriden implementation of "Equals" on the model. I voted for it on your behalf and raised its priority. You can also subscribe to receive email notifications for further status updates. Regards, Hristian Stefanov Progress Telerik
