# Hierarchal Drawer with children of children

## Question

**Abh** asked on 20 Mar 2022

Hi, I am trying to modify the existing code for the Hierarchical Drawer so I can have a nested nav menu in the drawer. Right now, when I add a level 2 child to a level 1 child, the level 2 child is not aligned properly; it is in line with the first original level when it should be indented. How can I fix this? @inject IFacilityService FacilityService
@inject ILocationService LocationService


<div class="custom-toolbar">
<TelerikButton OnClick="@ToggleDrawer" Icon="menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"></TelerikButton>
<span style="margin-left: 20px; font-weight: bold; font-size: 17px;">Wilder Fields Sensor Dashboard</span>
</div>

<TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="false" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded">
<Template>
<div class="k-drawer-items" role="menubar" aria-orientation="vertical">
<LoginDisplay />
<ul>
@foreach ( var item in context)
{ var selectedClass=item==SelectedItem ? "k-state-selected": string.Empty;
<li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass">
<div class="k-level-@(item.Level)">
<TelerikIcon Icon="@item.Icon"></TelerikIcon>
<span class="k-item-text">@item.Text</span>
</div>

@if (item.Expanded && (item.Children?.Any() ?? false ))
{
<span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span>
} else if (!item.Expanded && (item.Children?.Any() ?? false ))
{
<span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span>
}
</li>
}

</ul>
</div>
</Template>
<DrawerContent>
@SelectedItem?.Description
</DrawerContent>
</TelerikDrawer>



<!--- <NotAuthorized>
<a href="authentication/login">Log in </a>
</NotAuthorized>-->

@code { protected override async Task OnParametersSetAsync ( ) { await base.OnParametersSetAsync();


} public TelerikDrawer<DrawerItem> Drawer { get; set; } public DrawerItem SelectedItem { get; set; } public bool Expanded { get; set; }=true; public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem>
{ new DrawerItem { Text="R2D2", Icon="question",
Children=new List<DrawerItem>()
{ new DrawerItem { Text="Room 1", Icon="grid", Level=1,
Children=new List<DrawerItem>()
{ new DrawerItem { Text="Room 1", Icon="grid", Level=2 }, new DrawerItem { Text="Calendar", Icon="calendar-date", Level=2, Description="The Calendar component allows the user to scroll through a calendar and select one or more dates. " }, new DrawerItem { Text="Menu", Icon="menu", Level=2, Description="The Menu component displays data (flat or hierarchical) in a traditional menu-like structure." },
}



},

}





}, new DrawerItem {
Text="Components",
Icon="categorize",
Description="Blazor is still a new technology and the component suite is young. We are constantly working on adding new features and components. Tell us which components you want implemented and how you intend to use them, and Blazor, at our

## Answer

**Svetoslav Dimitrov** answered on 23 Mar 2022

Hello Abhay, If your desired layout is Root-level item=> level 1 child=> level 2 child, you can follow the same styling convention as in the example you are using as a base. In it you can see a padding-left defined for the k-level-1 (matching the level 1 child): .k-level- 1 { padding-left: 20px;
} In order to indent the level 2 children further to the right, you can define a similar style to this one: .k-level- 2 { padding-left: 40px;
} I hope this helps you move forward with your application. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Abhay** commented on 23 Mar 2022

Thank you for your help, Svetoslav, I really appreciate you getting back to me so quickly.
