# Telerik Drawer items text clipped at 240px

## Question

**Wal** asked on 19 Dec 2023

We are start using Blazor in a major redevelopment of our Angular App. We are looking at the Drawer to create a side navigation component that will display Hierarchical data. At the moment with just two levels the description of the items is clipped and shows the three dots at the end e.g. "Financial Comparis..." How do I resize the drawer sidebar width to more than the default 240px so that text is not clipped and ends with ....?

## Answer

**Hristian Stefanov** answered on 20 Dec 2023

Hi Walter, I'm glad to see that you are exploring our Blazor Drawer. To resize the Drawer sidebar width, the component exposes a "Width" parameter that you can use. I have prepared an example for you that demonstrates its usage: @using Telerik.SvgIcons <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@SvgIcon.Menu"> Toggle drawer </TelerikButton> <TelerikDrawer Data="@Data" Mode="@DrawerMode.Push" Width="450px" @ref="@DrawerRef"> <DrawerContent> lorem ipsum </DrawerContent> </TelerikDrawer> @code {
private TelerikDrawer <DrawerItem> DrawerRef { get; set; }

private IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> {
new DrawerItem { Text="Counter", Icon=SvgIcon.Plus },
new DrawerItem { Text="FetchData", Icon=SvgIcon.GridLayout },
};

public class DrawerItem
{
public string Text { get; set; }
public ISvgIcon Icon { get; set; }
}
} Let me know whether this is what you are looking for. Regards, Hristian Stefanov Progress Telerik
