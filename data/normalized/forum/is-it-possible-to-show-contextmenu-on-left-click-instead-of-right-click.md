# Is it possible to show ContextMenu on left click instead of right click?

## Question

**Ale** asked on 27 Feb 2022

Or is there is some alternate control I can use? Thanks!

## Answer

**Marin Bratanov** answered on 28 Feb 2022

Hi Alex, You can show it on any event you need by using its ShowAsync method: [https://docs.telerik.com/blazor-ui/components/contextmenu/integration](https://docs.telerik.com/blazor-ui/components/contextmenu/integration) Regards, Marin Bratanov Progress Telerik

### Response

**Chris** commented on 30 Mar 2023

Are there any examps of showing a ContextMenu from a "LEFT" click on a GridCommandButton? The OnClick event passes a GridCommandEventArgs, but the ContextMenu.ShowAsync() needs X and Y coordinates. How do you get the XY coordinates of the command button pressed?

### Response

**Hristian Stefanov** commented on 03 Apr 2023

Hi Chris, I'm pasting here the answer I gave you in the private ticket so the community can benefit from it.==To achieve the desired result, you can wrap the command column you want into an HTML div element and use its onclick event MouseEventArgs. I have prepared an example for you that shows the above approach: @using System.Collections.Generic
@using System.Collections.ObjectModel

@using Telerik.FontIcons <TelerikContextMenu @ref="@ContextMenuRef" Data="@MenuItems" OnClick="@((MenuItem item)=> ContextMenuClickHandler(item))"> </TelerikContextMenu> <TelerikGrid Data="@GridData" @ref="@GridRef" EditMode="@GridEditMode.Incell" Height="500px" Pageable="true"> <GridToolBarTemplate> <div onclick="@( (MouseEventArgs e)=> ShowContextMenu(e) )"> <GridCommandButton Command="Test" Icon="@FontIcon.Plus"> Custom Command for test </GridCommandButton> </div> </GridToolBarTemplate> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" /> <GridColumn Field=@nameof(SampleData.Name) /> </GridColumns> </TelerikGrid> @code {
ObservableCollection <SampleData> GridData { get; set; }
List <MenuItem> MenuItems { get; set; }
TelerikContextMenu <MenuItem> ContextMenuRef { get; set; }
TelerikGrid <SampleData> GridRef { get; set; }
SampleData LastClickedItem { get; set; }

public class MenuItem
{
public string Text { get; set; }
public FontIcon? Icon { get; set; }
public Action Action { get; set; }
public string CommandName { get; set; }
} async Task ShowContextMenu(MouseEventArgs e)
{
await ContextMenuRef.ShowAsync(e.ClientX, e.ClientY);
} async Task ContextMenuClickHandler(MenuItem clickedItem)
{
// handle the command from the context menu by using the stored metadata
if (!string.IsNullOrEmpty(clickedItem.CommandName) && LastClickedItem !=null)
{
Console.WriteLine($"The programm will now perform the {clickedItem.CommandName} operation for {LastClickedItem.Name}");
}
LastClickedItem=null;
}

protected override void OnInitialized()
{
MenuItems=new List <MenuItem> ()
{
new MenuItem(){ Text="Select", Icon=FontIcon.CheckboxChecked, CommandName="ToggleSelect" },
new MenuItem(){ Text="Edit", Icon=FontIcon.Pencil, CommandName="BeginEdit" },
new MenuItem(){ Text="Delete", Icon=FontIcon.Trash, CommandName="InvokeDelete" }
};

GridData=new ObservableCollection <SampleData> ();
var rand=new Random();

for (int i=0; i <100; i++)
{
GridData.Add(new SampleData()
{
ID=i,
Name="Employee " + i.ToString(),
});
}
}

public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
}
}==Kind Regards, Hristian

### Response

**Chris** commented on 03 Apr 2023

For anyone finding this, I ended up getting this to work using the context of the GridCommandColumn and passing it in addition to the MouseEventArgs recommended above. <GridCommandColumn Width="@CommandColumnWidth()" Locked="true" Context="dataItem"> @{ var selectedrow=dataItem as ExpandoObject; } <div onclick="@((MouseEventArgs m)=> ShowContextMenu(selectedrow, m))"> <GridCommandButton Icon="@FontIcon.ChevronDown"></GridCommandButton> </div> </GridCommandColumn>
