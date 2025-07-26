# Multiple @Body

## Question

**EdEd** asked on 04 Dec 2020

I'm new to Blazor with Telerik and i'm having trouble creating a "top-level" notification layout. I'm using a Drawer for a menu and would like a top-level notification component at the same level or above this Drawer component. I'm using this as an example: [https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app](https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app) But when I try to implementation something similar I end up with multiple @Body fragments in my MainLayout as seen below and in turn the content is duplicated. Although the cascading Notification stuff works nice :) I figure I'm missing something basic perhaps about encapsulating these into Blazor components? or something related to layouts? Thanks, Ed <TelerikRootComponent> <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@IconName.Menu"></TelerikButton> <img src="[https://www.qat.com/wp-content/uploads/2015/03/qat-global-logo-s.png"](https://www.qat.com/wp-content/uploads/2015/03/qat-global-logo-s.png") align="middle" /> <CultureChooser /> <TelerikNotification @ref="@Notification.Instance" HorizontalPosition="@NotificationHorizontalPosition.Right" VerticalPosition="@NotificationVerticalPosition.Top" Class="big-notification"> </TelerikNotification> <CascadingValue IsFixed="true" Value="@Notification"> <div class="content px-4"> @Body </div> </CascadingValue> <TelerikDrawer @ref="@DrawerRef" Data="@NavigablePages" Expanded="@Expanded" MiniMode="true" Mode="@DrawerMode.Push" SelectedItemChanged="((DrawerItem item)=> SelectedItemChangedHandler(item))" ExpandedChanged="((bool newValue)=> ExpandedChangedHandler(newValue))"> <Content> @Body </Content> </TelerikDrawer> </TelerikRootComponent>

## Answer

**Ed** answered on 05 Dec 2020

After a little more reading and a good nights rest I figured it out. I learned when it comes to the CascadingValue element, everything rendered within that element will have access to the value specified. So I wrapped the rest of my content under the CascadingValue element which allowed the Notification reference to be accessible from lower level components. Thanks, Ed <TelerikNotification @ref="@Notification.Instance" HorizontalPosition="@NotificationHorizontalPosition.Right" VerticalPosition="@NotificationVerticalPosition.Top" Class="big-notification"> </TelerikNotification> <CascadingValue IsFixed="true" Value="@Notification"> <TelerikDrawer @ref="@DrawerRef" Data="@NavigablePages" Expanded="@Expanded" MiniMode="true" Mode="@DrawerMode.Push" SelectedItemChanged="((DrawerItem item)=> SelectedItemChangedHandler(item))" ExpandedChanged="((bool newValue)=> ExpandedChangedHandler(newValue))"> <Content> @Body </Content> </TelerikDrawer> </CascadingValue>

### Response

**Nadezhda Tacheva** answered on 08 Dec 2020

Hello Ed, I am glad that you managed to figure out the CascadingValue component's behavior since it is really useful to apply in such scenarios. Indeed, if you want its specified value to be accessible from other components, they should be rendered inside the CascadingValue component. As for the multiple @Body fragments you were experiencing, this is due to the @Body fragment being declared two times - once in the CascadingValue component and once more in the Drawer component. Only one instance of the @Body fragment has to be implemented as per your second example. Regards, Nadezhda
