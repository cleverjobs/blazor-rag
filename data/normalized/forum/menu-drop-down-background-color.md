# Menu drop-down background color

## Question

**Joe** asked on 11 Dec 2023

How do I set the background on the dropdown? <div class="container"> <div class="row justify-content-md-end text-light gsi-background-color-darkgray"> <div class="col"> </div> <div class="col-md-auto"> <TelerikMenu Data="MenuItems" OnClick="@((TelerikMenuItem item)=> OnMenuClicked(item))"> </TelerikMenu> </div> </div> </div> public class TelerikMenuItem
{
public string Text { get; set; }
public bool Disabled { get; set; }
public bool Separator { get; set; }
public string Url { get; set; }
public IEnumerable <TelerikMenuItem> Items { get; set; }
}

## Answer

**Hristian Stefanov** answered on 13 Dec 2023

Hi Joel, To change the background color of the Menu dropdown, you need to follow the same approach as with any other style customization: Use the browser's DOM inspector. See what CSS rules in our theme apply the existing styles. Override the existing styles with similar ones that have higher CSS specificity. Here is an example that you can start from that shows different menu dropdown customizations: <TelerikMenu Data="@FlatData" Class="custom-hover" /> <style> /* root Menu items */.custom-hover.k-menu-item:hover { background-color: yellow;
}.custom-hover.k-menu-item:hover.k-menu-link { color: blue;
} /* whole dropdown background color */.k-popup.k-menu-group { background-color: red; color: white;
} /* child and context Menu items */.k-popup.k-menu-group.k-item>.k-link.k-active,.k-popup.k-menu-group.k-item>.k-link:hover { background-color: lime; color: blue;
} </style> @code {
private IEnumerable <TreeItem> FlatData { get; set; }

private int TreeLevels { get; set; }=3;
private int RootItems { get; set; }=5;
private int ItemsPerLevel { get; set; }=3;
private int IdCounter { get; set; }=1;

protected override void OnInitialized()
{
FlatData=LoadFlat();
}

private List <TreeItem> LoadFlat()
{
List <TreeItem> items=new List <TreeItem> ();

PopulateChildren(items, null, 1);

return items;
}

private void PopulateChildren(List <TreeItem> items, int? parentId, int level)
{
var itemCount=level==1 ? RootItems : ItemsPerLevel;
for (int i=1; i <=itemCount; i++)
{
var itemId=IdCounter++;
items.Add(new TreeItem()
{
Id=itemId,
Text=$"Level {level} Item {i} Id {itemId}",
ParentId=parentId,
HasChildren=level <TreeLevels
});

if (level <TreeLevels)
{
PopulateChildren(items, itemId, level + 1);
}
}
}

public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentId { get; set; }
public bool HasChildren { get; set; }
}
} I hope this helps. Let me know whether the result is what you are looking for. Regards, Hristian Stefanov Progress Telerik

### Response

**Joel** commented on 13 Dec 2023

That worked, thanks.
