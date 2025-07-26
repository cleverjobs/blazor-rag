# Children null vs empty

## Question

**Dat** asked on 04 Oct 2019

If the children property is not null then the expand children arrow will display. It displays even if the children is an empty array. This may be a feature but seems more like a bug to me. <TelerikMenu Data="@MenuItems" Orientation="MenuOrientation.Vertical" UrlField="@nameof(MenuItem.Url)" ItemsField="@nameof(MenuItem.Children)" TextField="@nameof(MenuItem.Text)" ImageUrlField="@nameof(MenuItem.Image)"> </TelerikMenu> public class MenuItem { public string Text { get; set; }=""; public string Url { get; set; }=""; public string Image { get; set; }=""; public MenuItem[] Children { get; set; } // Arrow will show on all items if:=Array.Empty<MenuItem>(); }

## Answer

**Marin Bratanov** answered on 07 Oct 2019

Hello Patrick, You can set the HasChildren property to override that if you want: [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview#treeview-item-features.](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview#treeview-item-features.) On null children vs empty collection - this is needed for the lazy loading (load on demand). Initially, an item may not have child items, but it may have to show an expand arrow so the user has a way to load them. The HasChildren field, again, allows you to override that. You can find examples of how empty collections must provide you with expand arrows in this demo: [https://demos.telerik.com/blazor-ui/treeview/lazy-loading](https://demos.telerik.com/blazor-ui/treeview/lazy-loading) - if the expand arrows are not there, you can't see the details. Another example is available in the documentation that shows using the HasChildren field to control this, and using null fields: [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/load-on-demand.](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/load-on-demand.) Regards, Marin Bratanov
