# Open a window when drawer item is clicked.

## Question

**Bla** asked on 04 Mar 2021

Hello. I wanted to know if it is possible that clicking on an item in the Drawer instead of navigating to a new page opens a window or a dialog box? Regards.

## Answer

**Svetoslav Dimitrov** answered on 05 Mar 2021

Hello Ludwig, You can take advantage of the ItemTemplate for the Drawer. It gives you control over the rendering of the Drawer items. Below, I have added a code snippet on how this behavior can be implemented. You can use it as a base and extend it in your application with, for example - open the model on click on the Icon when the drawer is collapsed. <TelerikWindow Modal="true" @bind-Visible="@isModalVisible"> <WindowTitle> <strong> The Title </strong> </WindowTitle> <WindowContent> I am modal so the page behind me is not available to the user. </WindowContent> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> </TelerikWindow> <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="menu" /> <TelerikDrawer @bind-Expanded="@Expanded" Data="@Data" MiniMode="true" Mode="@DrawerMode.Push" @bind-SelectedItem="@SelectedItem" @ref="@DrawerRef"> <ItemTemplate Context="item"> <span class="k-icon k-i-@item.Icon" style="margin-right: 8px;"> </span> @if (Expanded)
{
if (item.Text !="Open Window")
{ <div class="@( item.Icon.ToLowerInvariant()==" gear " ? " text-danger ": " text-info " )"> <div style="font-weight:bold;"> @item.Text </div> </div> }
else
{ <div @onclick="@( _=> isModalVisible=true )"> <div> @item.Text </div> </div> }
} </ItemTemplate> <Content> <strong> @SelectedItem?.Description </strong> </Content> </TelerikDrawer> @code {
bool isModalVisible { get; set; }

public TelerikDrawer <DrawerItem> DrawerRef { get; set; }
public DrawerItem SelectedItem { get; set; }
public bool Expanded { get; set; }=true;
public IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> {
new DrawerItem {Text="Shopping Cart", Icon="cart", Description="Items in shopping cart"},
new DrawerItem {Text="Notifications", Icon="notification", Description="My profile notifications"},
new DrawerItem {Text="Calendar", Icon="calendar", Description="My events"},
new DrawerItem {Text="Settings", Icon="gear", Description="My profile settings"},
new DrawerItem {Text="Open Window", Icon="window", Description="Open Modal Window"},
};

public class DrawerItem
{
public string Text { get; set; }
public string Icon { get; set; }
public string Description { get; set; }
}
} I hope this helps you move forward with your application. If you need any further assistance do not hesitate to contact us again! Regards, Svetoslav Dimitrov

### Response

**Blazorist** answered on 11 Mar 2021

Thank you Svetoslav for your answer. I will try your solution. Blazorist

### Response

**Svetoslav Dimitrov** answered on 11 Mar 2021

Hello Ludwig, Sure, take your time. If you need any further assistance let us know! Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Blazorist** answered on 11 Mar 2021

I just realized that <Template> and <ItemTemplate> cannot use together. I've already modified the template to prevent the drawer from collapsing when clicked. I will try to find an alternative to have the two functionalities together. Thank you again.

### Response

**Blazorist** answered on 11 Mar 2021

I found a good solution modifying the drawer Template instead of the ItemTemplate. In this way, I have the two desired functionalities together (prevent collapse on click and show a window when an item is clicked). I leave the code below in case someone needs it. Greetings. <!-- Window --> <TelerikWindow Modal="true" @bind-Visible="@isModalVisible"> <WindowTitle> <strong>The Title</strong> </WindowTitle> <WindowContent> I am modal so the page behind me is not available to the user. </WindowContent> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> </TelerikWindow> <!-- Drawer --> <TelerikDrawer Data="@NavigablePages" @bind-Expanded="@DrawerExpanded" MiniMode="true" Mode="@DrawerMode.Push" @ref="@DrawerRef" @bind-SelectedItem="@SelectedItem" Width="auto"> <Template> <div class="k-drawer-items"> <ul> @foreach (var item in NavigablePages) { @* stop the propagation of the onclick event to prevent the drawer from collapsing *@@* Use onclick to handle manual item selection and toggle the selected class *@<li @onclick:stopPropagation @onclick="@(()=> DrawerNavigateTo(item))" class="k-drawer-item @GetSelectedItemClass(item)" style="white-space:nowrap"> <span class="k-icon k-i-@item.Icon" style="margin-right: 8px;"></span> @if (DrawerRef.Expanded) { <span class="k-item-text">@item.Text</span> } </li> } </ul> </div> </Template> <Content> @Body </Content> </TelerikDrawer> <!-- Code (Just for the example. I prefer C# code in.cs file apart) --> @code { bool isModalVisible { get; set; } public class DrawerItem { public string Text { get; set; } public string Url { get; set; } public string Icon { get; set; } public bool IsSeparator { get; set; }=false; public string Description { get; set; } public bool IsWindow { get; set; }=false; } //Drawer definition public IEnumerable<DrawerItem> NavigablePages { get; set; }=new List<DrawerItem> { new DrawerItem { Text="Page1", Url=Constants.Navigation.PAGE1, Icon="toggle-full-screen-mode" }, new DrawerItem { Text="Page2", Url=Constants.Navigation.PAGE2, Icon="plus-outline" }, new DrawerItem { Text="Page3", Url=Constants.Navigation.PAGE3 Icon="paste-plain-text" }, new DrawerItem { Text="Options Window", Url=string.Empty, Icon="gear", IsWindow=true } }; private void DrawerNavigateTo(DrawerItem item) { if (SelectedItem !=item) //swallow { if (!item.IsWindow) { SelectedItem=item; NavigationManager.NavigateTo(SelectedItem.Url); } else { isModalVisible=true; } } } }
