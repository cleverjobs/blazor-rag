# How Do I Dynamically Create a TelerikContextMenu in Blazor?

## Question

**KenKen** asked on 10 Nov 2021

While data binding is great for a lot of reasons, I am building a series of images on a page that each need their own context menu. In addition, based on the JSON I am reading from, some menu items will be disabled and/or have different icons. To this end, on the Razor frontend page, I need to manually build the TelerikContextMenu out but I cannot figure out how to do so. I have the following, based on my destruction of a perfect valid Telerik online example, but I do not know what to add into the ItemTemplate nor do I understand how to map that, whatever it is, back to the public class. { var menuCounter=0; var targetName=""; var targetNameWithDot=""; var menuId=""; @foreach (Device thisDevice in CurrentSystem.LocalDevices)
{
menuCounter++;
targetName="target" + @menuCounter;
targetNameWithDot="." + @targetName;
menuId="contextMenu" + @menuCounter; <TelerikContextMenu IdField="@menuId" Selector="@targetNameWithDot" Data="@MenuItems" OnClick="@((MenuItem item)=> OnItemClick(item, @thisDevice.DeviceIDHash))"> <ItemTemplate> </ItemTemplate> </TelerikContextMenu> <div style="width: 100%" class="target-wrapper @CssClass"> <div class="@targetName"> <p class="placeholder"> Right-click to open Context menu </p> </div> </div> <tr> <td> @thisDevice.DeviceName </td> <td> @thisDevice.DeviceIDHash </td> </tr> }
}
} Any help would be GREATLY appreciated!

### Response

**Ken** commented on 10 Nov 2021

I made some progress(?) however the context menus are still not writing to the screen. { var menuCounter=0; var targetName=""; var targetNameWithDot=""; var menuId=""; @foreach (Device thisDevice in CurrentSystem.LocalDevices)
{
menuCounter++;
targetName="target" + @menuCounter;
targetNameWithDot="." + @targetName;
menuId="contextMenu" + @menuCounter; <TelerikContextMenu IdField="@menuId" Selector="@targetNameWithDot" Data="@MenuItems" OnClick="@((MenuItem item)=> OnItemClick(item, @thisDevice.DeviceIDHash))"> <Template> @{
var dataSource=context as List <MenuItem>;
if (thisDevice.UsingEncryption)
{
dataSource[3].Text="Enable Encryption";
dataSource[3].Icon="k-icon k-i-lock";
}
if (thisDevice.CurrentAlerts==null || thisDevice.CurrentAlerts.Count==0)
{
dataSource[4].Disabled=true;
dataSource[4].Icon="k - icon k - i - exception style='color: grey;' ";
}
} </Template> </TelerikContextMenu> <div style="width: 100%" class="target-wrapper @CssClass"> <div class="@targetName" style="text-align:right"> <span class="material-icons-outlined md-light"> menu </span> </div> <br /> <div> @thisDevice.DeviceName </div> </div> }
}

### Response

**Dimo** commented on 11 Nov 2021

Hi Ken, <Template> should iterate and render the menu items, which does not happen in this case. Check our ContextMenu Templates example.
