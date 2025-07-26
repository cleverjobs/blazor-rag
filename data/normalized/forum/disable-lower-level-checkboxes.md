# Disable lower level checkboxes?

## Question

**Deb** asked on 05 Jan 2022

Hello, I want to enable the checkboxes for the top level of the treeview but disable or not show the checkboxes below that. So for your example at: [https://docs.telerik.com/blazor-ui/components/treeview/checkboxes/overview](https://docs.telerik.com/blazor-ui/components/treeview/checkboxes/overview) I want to show (or enable) the checkboxes for Project and Implementation but not for Design, Site, index.js, index.html, or styles.css. Thank you,

### Response

**Debra** commented on 10 Jan 2022

Thank you so much! I got very close to the correct code when I was experimenting with it but just couldn't get the last little bit (I was missing the singular <TreeViewBinding> before the <ItemTemplate>. This will work great. I really appreciate it.

## Answer

**Hristian Stefanov** answered on 10 Jan 2022

Hi Debra, You can achieve the desired result by using a Template. This template will allow you to implement custom checkboxes. I have prepared for you an example: <style>.check-box { margin-right: 6px;
} </style> <TelerikTreeView Data="@TreeData"> <TreeViewBindings> <TreeViewBinding> <ItemTemplate> @{
TreeItem itm=context as TreeItem;
if (itm.HasChildren)
{ <TelerikCheckBox @bind-Value="itm.Checked" Class="check-box" OnChange="_=> CheckItem(itm)"> </TelerikCheckBox> } <strong> @itm.Text </strong> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code {
public static List <TreeItem> checkedItems=new List <TreeItem> ();

public void CheckItem(TreeItem item)
{
if (item.Checked)
{
checkedItems.Add(item);
}
else
{
checkedItems.Remove(item);
}
}

public IEnumerable <TreeItem> TreeData { get; set; }

public class TreeItem
{
public string Text { get; set; }
public int Id { get; set; }
public List <TreeItem> Items { get; set; }=new List <TreeItem> ();
public bool Expanded { get; set; }
public bool HasChildren { get; set; }
public bool Checked { get; set; }
}

protected override void OnInitialized()
{
LoadHierarchical();
}

private void LoadHierarchical()
{
List <TreeItem> roots=new List <TreeItem> () {
new TreeItem { Text="Item 1", Id=1, Expanded=true, HasChildren=true, Checked=false },
new TreeItem { Text="Item 2", Id=2, HasChildren=true, Checked=false }
};

roots[0].Items.Add(new TreeItem
{
Text="Item 1 first child",
Id=3
});

roots[0].Items.Add(new TreeItem
{
Text="Item 1 second child",
Id=4
});

roots[1].Items.Add(new TreeItem
{
Text="Item 2 first child",
Id=5
});

roots[1].Items.Add(new TreeItem
{
Text="Item 2 second child",
Id=6
});

TreeData=roots;
}
} You can extend the above example to cover your app requirements. Regards, Hristian Stefanov
