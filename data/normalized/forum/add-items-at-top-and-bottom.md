# Add items at top and bottom

## Question

**Dan** asked on 03 Jan 2023

Hi I wonder if it is possible to add a kind of footer to the drawer. For example, whe could have the navigation buttons on the top (like usual) and some buttons on the bottom ( ex : admin and user profile ) here is an example How can i archieve this ? Thanks

## Answer

**Twain** answered on 03 Jan 2023

Hi Daniel. I've achieved that modifying the drawer template. I have three types of items, Pages (when you click on it change the drawer content), Separator (add an horizontal line in the drawer) and Filler (this one is what you need to implement). <TelerikDrawer Data="@NavigablePages" MiniMode="true" Mode="@DrawerMode.Push" @ref="@_drawerRef" @bind-SelectedItem="@_selectedItem" Width="auto"> <Template> <div class="h-100 k-d-flex-col"> <div class="k-drawer-items"> <ul class="h-100"> @foreach (var item in NavigablePages)
{
if (item.IsPage))
{
@* stop the propagation of the onclick event to prevent the drawer from collapsing *@@* Use onclick to handle manual item selection and toggle the selected class *@<li @onclick:stopPropagation @onclick="@(()=> DrawerNavigateTo(item))" class="k-drawer-item @GetSelectedItemClass(item) k-text-nowrap"> <span class="k-icon k-i-@item.Icon" title="@item.Title"> </span> @if (_drawerRef.Expanded)
{ <span class="k-item-text"> @item.Text </span> } </li> }
else
{
if (item.IsFiller())
{ <li class="h-100 d-block"> </li> }
else //it's a separator
{ <li class="k-drawer-item k-drawer-separator"> </li> }
}
} </ul> </div> </div> </Template> <Content> /* Drawer content */ </Content> </TelerikDrawer> In the code behind you just need to define the items list and its properties. public List<DrawerItem> NavigablePages { get; set; } private DrawerItem _selectedItem; private TelerikDrawer<DrawerItem> _drawerRef; private async Task BuildNavigationBar ( ) { var state=await AuthenticationStateTask; var username=state.User.Identity.Name ?? string.Empty;

NavigablePages=new List<DrawerItem>
{ new DrawerItem()
{
Index=5,
Text="Some text",
Target=Constants.Navigation.SOMEVALUE,
Icon="Some icon" }, new DrawerItem()
{
Index=10,
ItemType=DrawerItem.DRAWER_SEPARATOR,
}, new DrawerItem()
{
Index=20,
Text="Some text",
Target=Constants.Navigation.SOMEVALUE,
Icon="Some Icon" }, new DrawerItem()
{
Index=90,
ItemType=DrawerItem.DRAWER_FILLER,
}, // items after the filler will be at the bottom of the drawer new DrawerItem()
{
Index=100,
Text="Some text",
Icon="Some icon" }, new DrawerItem()
{
Index=120,
Text=username,
Icon="user",
},
};
}

NavigablePages.Sort((p, q)=> p.Index.CompareTo(q.Index));
} Well, that's pretty much it. I hope it serves as a guide for your implementation. Best regards. Twain.

### Response

**Daniel** commented on 03 Jan 2023

thanks for the quick answer, i'll try this ...
