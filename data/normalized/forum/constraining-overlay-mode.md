# Constraining Overlay Mode

## Question

**Gra** asked on 09 Mar 2021

Is there a way of constraining the drawer when in Overlay mode to its parent <div>? I see it being done in your demo page [https://demos.telerik.com/blazor-ui/drawer/display-modes](https://demos.telerik.com/blazor-ui/drawer/display-modes) thanks

## Answer

**Svetoslav Dimitrov** answered on 10 Mar 2021

Hello Gray, You can see the code we have used for the demo from the View Source tab. We have added absolute positions to the div that contains the drawer (class="k-drawer") and the div that represents the overlay (class="k-overlay"). The parent element of the Drawer should have a relative position (class="k-drawer-container"). For your convenience, I have added an example below. <style>.k-overlay { position: absolute;
}.k-drawer-container.k-drawer-overlay.k-drawer { position: absolute;
}.k-drawer-container { position: relative; width: 100%; height: 100%;
}
</style> <div style=" width: 400 px; height: 400 px; border: solid 0.5px black;">
<TelerikDrawer @bind-Expanded=" @Expanded "
Data="@Data" MiniMode="true" Mode="@DrawerMode.Overlay" @bind-SelectedItem="@selectedItem" @ref="@DrawerRef">
<Content>
<div class="pl-5">
<TelerikButton OnClick="@OnClick" Icon="menu"></TelerikButton>
</div>
<div class="text-info pl-4">
The drawer is expanded: @Expanded
<br />
Content for the @selectedItem?.Text
</div>
</Content>
</TelerikDrawer>
</div>

@code { private void OnClick ()
{
DrawerRef.ToggleAsync();
StateHasChanged();
} public TelerikDrawer <DrawerItem> DrawerRef { get; set; } public DrawerItem selectedItem { get; set; } public bool Expanded { get; set; }=true; public IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem>
{
new DrawerItem { Text="Counter", Icon="plus"}, new DrawerItem { Text="FetchData", Icon="grid-layout"},
}; public class DrawerItem {
public string Text { get; set; } public string Icon { get; set; }
}
} Regards, Svetoslav Dimitrov
