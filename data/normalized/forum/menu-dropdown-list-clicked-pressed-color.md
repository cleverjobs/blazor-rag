# Menu dropdown list clicked/pressed color

## Question

**And** asked on 03 Apr 2023

Hi, I am currently using the TelerikMenu Blazor component and I am having issues with changing the color of the pressed/clicked state of a menu item. I can successfully change the coloring for the other states of the menu items e.g. selected, focused, active, hover. How would I approach this to solve my problem? This is what I have so far: MenuItems=new List<MenuItem>(); MenuItem Library_Header=new MenuItem() { Text="Library", Icon="book", Items=new List<MenuItem>() }; MenuItem Library_Item_EFT=new MenuItem() { Text="EFT Library", Icon="book", Items=new List<MenuItem>() }; MenuItem EFT_Item_Bank_View=new MenuItem() { Text="Bank view", Icon="book" }; MenuItem EFT_Item_Version_View=new MenuItem() { Text="Version view", Icon="book" }; Menu css (example of the menu's selected state being changed):.k-menu-group .k-item:focus, .k-menu-group .k-item.k-state-selected, .k-menu.k-context-menu .k-item:selection, .k-menu.k-context-menu .k-item.k-state-selected { background-color: green; //I want to change the clicked state to green }

### Response

**Nadezhda Tacheva** commented on 06 Apr 2023

Hi Andy, By design of the Menu component, it does not keep the selected state of its items. For example, when the user clicks on an item in the popup, it is indeed highlighted but it will not appear as selected the next time the popup is opened. Can you please elaborate a bit more on the exact scenario you are trying to achieve and the problems you are facing? For example, what should happen if the user clicks on the "Bank view" item? It will be best if you can share a runnable sample replicating your exact configuration, so we can explore it. Thank you in advance!
