# Drawer data not binding

## Question

**Der** asked on 24 Apr 2025

I'm having trouble with data binding in the drawer component. In order to help isolate + demonstrate the issue I've created a simple test page containing a drawer component with minimal configuration:- @layout TelerikLayout
@page "/test" <TelerikDrawer @bind-SelectedItem="SelectedItem" Data="Data">
<DrawerContent><p>Hello</p></DrawerContent>
</TelerikDrawer>

@code { private class DrawerItem { public FontIcon Icon { get; set; } public bool Separator { get; set; } public string Text { get; set; } public string Url { get; set; }
} private List<DrawerItem> Data { get; set; }=new List<DrawerItem> { new DrawerItem { Icon=FontIcon.CaretTr, Text="Hello" } }; private DrawerItem? SelectedItem { get; set; }
} And here is the resulting markup. The drawer component is rendered and so is the drawer content, but no drawer items:- <div class="k-drawer-container k-drawer-overlay"> <!--!--> <!--!--> <div class="k-drawer telerik-blazor k-drawer-start" data-id="2ccfd37c-d109-485f-80e7-654bf55cb5c7" dir="ltr"> <!--!--> <!--!--> <!--!--> <div class="k-drawer-wrapper" style="width: 0; transition-duration: 0ms;"> <!--!--> </div> <!--!--> </div> <!--!--> <div class="k-drawer-content"> <!--!--> <!--!--> <p> Hello </p> </div> <!--!--> </div> I've tried using IEnumerable instead of List, making SelectedItem not nullable, and removing SelectedItem altogether, and the result is the same. I'm on Telerik UI for Blazor version 8.1.1 and all other components appear to be working fine. Any help would be appreciated.

## Answer

**Marco** answered on 24 Apr 2025

Hy Derek, you don't see the item because the "Expanded" property of the TelerikDrawer component is set to "false" by default. Try setting the property to true as in the example at this link: Blazor Drawer Data Binding - Telerik UI for Blazor
