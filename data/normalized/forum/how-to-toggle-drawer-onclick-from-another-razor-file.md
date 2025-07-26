# How to toggle drawer OnClick from another razor file?

## Question

**Ote** asked on 14 Feb 2024

Hello, Am trying to toggle the drawer component from a separate razor file. I have two razor files in the following directories: \Components\Layout\SiteHeader\SiteHeader.razor \Components\Pages\Home.razor If Home.razor contains the default Drawer code: @* This example shows the basic configuration of the Drawer and how to expand or collapse a Drawer with a click of a button. *@<TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@SvgIcon.Menu">
Toggle drawer
</TelerikButton>

<TelerikDrawer Data="@Data" Mode="@DrawerMode.Push" @ref="@DrawerRef">
<DrawerContent>lorem ipsum</DrawerContent>
</TelerikDrawer>

@code {
Telerik.Blazor.Components.TelerikDrawer<DrawerItem> DrawerRef { get; set; }

IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem>
{ new DrawerItem { Text="Counter", Icon=SvgIcon.Plus }, new DrawerItem { Text="FetchData", Icon=SvgIcon.GridLayout },
}; public class DrawerItem { public string Text { get; set; } public ISvgIcon Icon { get; set; }
}
} If however I waned to move only the button portion to the SiteHeader.razor file <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@SvgIcon.Menu">
Toggle drawer
</TelerikButton> How can I get access to the DrawerRef So that I can toggle from SiteHeader.razor Is this possible? Thanks Any help be appreciated Thanks

## Answer

**Hristian Stefanov** answered on 19 Feb 2024

Hi Otemu, Here is an example I have prepared for you that demonstrates how to access the Drawer's reference within another separate razor file: REPL link. Let me know if this is what you are looking for. Regards, Hristian Stefanov Progress Telerik

### Response

**Otemu** commented on 20 Feb 2024

Hi Hristian, Great this is perfect
