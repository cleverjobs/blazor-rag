# Drawer Mini Mode Width - blazor

## Question

**ale** asked on 18 Apr 2024

Hi, is there a override for Drawer Width when in Mini Mode. I wanted to increase the size of my Icons outside of the default 50px. Thanks!

## Answer

**Hristian Stefanov** answered on 18 Apr 2024

Hi Alex, To increase the Drawer width in mini mode, you can use the following CSS: <style>.k-drawer-mini.k-drawer.k-drawer-wrapper { width: 75px;
} </style> <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@SvgIcon.Menu"> Toggle drawer </TelerikButton> <TelerikDrawer Data="@Data" MiniMode="true" Mode="@DrawerMode.Push" @ref="@DrawerRef"> </TelerikDrawer> @code {
public TelerikDrawer <DrawerItem> DrawerRef { get; set; }
public bool MiniMode { get; set; }=true;
public IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> {
new DrawerItem { Text="Counter", Icon=SvgIcon.Plus },
new DrawerItem { Text="FetchData", Icon=SvgIcon.GridLayout },
};

public class DrawerItem
{
public string Text { get; set; }
public ISvgIcon Icon { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik
