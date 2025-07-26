# Drawer Item tooltip?

## Question

**Dea** asked on 04 Nov 2022

Anyway to add a tooltip hint to the drawer item? Popsup when the mouse hovers over it!

## Answer

**Deasun** answered on 10 Nov 2022

My answer in the comment above.

### Response

**Dimo** answered on 09 Nov 2022

Hi Deasun, Yes, you can integrate the Tooltip component with the Drawer items. The question is what to show in it. The Tooltip works with title and data attributes of its target and the Drawer items don't have these. So you can use a Drawer ItemTemplate or a Template to render the information that you will then use inside the Tooltip. Regards, Dimo

### Response

**Deasun** commented on 10 Nov 2022

I ended up doing the following: Theres the hint in action, from the code below. public class DrawerItem { public string Title { get; set; } // this becomes the popup hint I was looking for. public string Text { get; set; } public string Icon { get; set; } public string Url { get; set; } public bool Separator { get; set; } public IEnumerable<(string, string)> AdditionalData { get; set; } } public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem> { new DrawerItem { Title="Home", Text="Home", Icon="home", Url="./" }, new DrawerItem { Separator=true}, new DrawerItem { Title="CostTN Search", Text="CostTN Search", Icon="search", Url="TNSearch" }, new DrawerItem { Title="RevIOTN Search", Text="RevIOTN Search", Icon="search", Url="RevIOTNSearch" }, new DrawerItem { Title="TN Mapping", Text="TN Mapping", Icon="subreport", Url="TNMapping" }, new DrawerItem { Title="Load Stats", Text="Load Stats", Icon="subreport", Url="LoadStats" }, new DrawerItem { Separator=true}, };
