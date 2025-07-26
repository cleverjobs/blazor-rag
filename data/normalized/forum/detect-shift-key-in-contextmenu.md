# Detect SHIFT key in ContextMenu

## Question

**Kei** asked on 19 Mar 2024

I'm using a "hierarchical" TelerikContextMenu (example below). I want to detect if the SHIFT key was depressed when an item (i.e., ItemA1 or ItemB2) is clicked (detecting the difference between click and SHIFT-click). I can detect if the shift key is depressed in the @oncontextmenu event, but that is for the click invoking the context menu. I want a similar capability when selecting an item IN the context menu. Any suggestions? The context menu is structured like this: ItemA
ItemA1
ItemA2
ItemB
ItemB1
ItemB2

## Answer

**Hristian Stefanov** answered on 21 Mar 2024

Hi Keith, To detect whether the SHIFT key was depressed upon item click, use the ContextMenu's ItemTemplate. Then, inside of it, wrap the item within an HTML span element and handle its onclick event. I have prepared an example for you: <div class="menuTarget"> right click this context menu target </div> <TelerikContextMenu Data="@MenuItems" Selector=".menuTarget"> <ItemTemplate> @{ <span @onclick="@HandleShiftClick"> @context.Text </span> } </ItemTemplate> </TelerikContextMenu> @code {
private List <ContextMenuItem> MenuItems { get; set; }
private TelerikContextMenu <ContextMenuItem> TheContextMenu { get; set; } private void HandleShiftClick(MouseEventArgs e)
{
if (e.ShiftKey)
{
Console.WriteLine("Shift + Click detected!");
// Add your logic here to handle the Shift + Click event
}
else
{
Console.WriteLine("Regular click detected.");
// Handle regular click event if necessary
}
} // generate sample data for the listview and the menu
protected override void OnInitialized()
{
MenuItems=new List <ContextMenuItem> ()
{
new ContextMenuItem
{
Text="More Info",
Url="about"
},
new ContextMenuItem
{
Text="Lorem Ipsum",
Metadata="special"
}
};

base.OnInitialized();
}

public class ContextMenuItem
{
public string Text { get; set; }
public string Url { get; set; }
public string Metadata { get; set; }
}
} <style>.menuTarget { width: 100px; background: yellow; margin: 50px;
} </style> Let me know if this is what you are looking for. Regards, Hristian Stefanov Progress Telerik
