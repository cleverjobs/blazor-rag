# Drawer Separator

## Question

**Twa** asked on 12 Feb 2021

Hi, I'm trying to add a Separator to a TelerikDrawer but it doesn't work as is expected: no separator is added. Instead, an common item is shown that when clicked, an exception is thrown. I'm using the default DrawerItem class definition. Here is my code: public class DrawerItem { public string Text { get; set; } public string Url { get; set; } public string Icon { get; set; } public bool IsSeparator { get; set; } } /* Items */ public List<DrawerItem> NavigablePages { get; set; }=new List<DrawerItem> { new DrawerItem { Text="System Overview", Url=Constants.Navigation.HOME, Icon="toggle-full-screen-mode" }, new DrawerItem { IsSeparator=true, Url=string.Empty }, // --> don't work new DrawerItem { Text="Add Container", Url=Constants.Navigation.CONTAINERFORM, Icon="plus-outline" }, new DrawerItem { Text="Show App Logs", Url=Constants.Navigation.LOGMONITOR, Icon="paste-plain-text" }, new DrawerItem { Text="Options", Url=Constants.Navigation.OPTIONS, Icon="gear" } }; /* Drawer component definition */ <TelerikDrawer Data="@NavigablePages" @bind-Expanded="@DrawerExpanded" MiniMode="true" Mode="@DrawerMode.Push" @ref="@DrawerRef" @bind-SelectedItem="@SelectedItem" Width="auto"> <Template> <div class="k-drawer-items"> <ul> @foreach (var item in NavigablePages) { @* stop the propagation of the onclick event to prevent the drawer from collapsing *@@* Use onclick to handle manual item selection and toggle the selected class *@<li @onclick:stopPropagation @onclick="@(()=> SelectAndNavigate(item))" class="k-drawer-item @GetSelectedItemClass(item)" style="white-space:nowrap"> <span class="k-icon k-i-@item.Icon" style="margin-right: 8px;"></span> @if (DrawerExpanded) { <span class="k-item-text">@item.Text</span> } </li> } </ul> </div> </Template> <Content> @Body </Content> </TelerikDrawer> Any suggestion on what's going on? Thanks. Twain.

## Answer

**Nadezhda Tacheva** answered on 16 Feb 2021

Hello Marcos, When using Drawer Template the built-in features of the drawer are disabled and should be handled by the application. The drawer will expand and collapse as usual, but the content has to be controlled by the application entirely, including the separator. If you want to use the built-in Drawer functionalities, you should stick to the default structure of the Drawer. An example of a Drawer with separator you can find in this article for Drawer as Navigation. In the meantime, if you want to use a Template, the application should be modified to handle the customization you need - for example, separator could be managed by some custom CSS ( this article might be helpful to easily find the relevant elements in the DOM. The Drawer also has a Class parameter which you can use to add custom CSS class and set a stronger selector). Regarding the exception, as you've mentioned that it is thrown on click, one possible reason behind this could stem from the SelectAndNavigate method - for example the item it accepts does not have url defined and the page cannot be navigated to. If you have tried all of the above options and you are still experiencing some difficulties, you can send us a runnable example where the issue is reproduced, so we can investigate further and provide a solution. Regards, Nadezhda Tacheva

### Response

**Twain** answered on 16 Feb 2021

Hi Nadezhda. I've modified the template to avoid the propagation of the event that collapse the drawer when an item in pressed. So, in order to keep this I'll have to take the manually approach and create the separator myself. Thanks you very much for you answer. Regards.

### Response

**Nadezhda Tacheva** answered on 18 Feb 2021

Hi Marcos, I'm glad you've managed to resolve it. If any additional questions appear, please do not hesitate to contact us. Regards, Nadezhda Tacheva
