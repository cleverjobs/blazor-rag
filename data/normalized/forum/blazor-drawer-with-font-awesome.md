# Blazor Drawer with font awesome

## Question

**Dan** asked on 27 Jan 2022

Hello, I'm trying to use font-awesome in the Blazor Drawer. I can use the font anywhere except with the Drawer. For my test, you can look at the first MenuItem for Trucks. Thanking you in advance. Daniel Legare @inherits LayoutComponentBase <TelerikRootComponent> <TelerikDrawer @ref="SidebarLeft" Data="menuItems" MiniMode="true" Mode="@DrawerMode.Push" @bind-SelectedItem="SelectedItem"> <DrawerContent> <div class="main"> <div class="top-row px-4"> <TelerikButton OnClick="@ToggleDrawer" Icon="menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"></TelerikButton> <a href="[http://blazor.net"](http://blazor.net") target="_blank" class="ml-md-auto">About</a> </div> <div class="content px-4"> @Body </div> </div> </DrawerContent> </TelerikDrawer> </TelerikRootComponent> @code { public TelerikDrawer<MenuItem> SidebarLeft { get; set; } public MenuItem SelectedItem { get; set; } public async Task ToggleDrawer()=> await SidebarLeft.ToggleAsync(); private IEnumerable<MenuItem> menuItems=> new List<MenuItem> { new MenuItem {Text="Trucks", Url="/truck", Icon="<i class='fa-solid fa-truck' />" }, new MenuItem {Text="Clients", Url="client", Icon="myspace"}, new MenuItem {Text="Earth", Url="/earth", Icon="globe"}, new MenuItem {Text="Contacts", Url="/contact", Icon="user"}, }; }

## Answer

**Chuck** answered on 27 Jan 2022

I've done something like what you are doing by the following method. I'm not saying it's the only way, but it works for me. I'm using Font Awesome 5 Pro, so you may need to adjust the font-family if you are using something different. You can globalize this by adding to a css file or focus this on the page in question but the end effect is the same. This sample will show you the page method. I've also attached the sample text file in case I missed something in the description here. In your page file, add a <style></style> section to add a a class for the font as shown below. <style> .k-i-truck::before { content: "\f0d1"; font-family: "Font Awesome 5 Pro"; } </style> Then, when you create the menuitem for the truck entry, do so like this: new MenuItem {Text="Trucks", Url="/truck", Icon=" truck" } That should let you do what you are looking for. Thanks, Chuck

### Response

**Daniel** commented on 28 Jan 2022

Thank you very much, Chuck. Your sample.txt work's perfectly and it's easy to apply. It took me a while to notice the difference from your answer and your sample. new MenuItem { Text=" Trucks ", Url=" /truck ", Icon=" truck " } instead of new MenuItem { Text=" Trucks ", Url=" /truck ", Icon=" <truck' /> " } I really appreciated it. Regards,

### Response

**Chuck** commented on 28 Jan 2022

oops, copy/paste error! I've edited the original reply. Really glad I added the code file along with the answer. Thanks, Chuck
