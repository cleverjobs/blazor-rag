# Drawer submenus?

## Question

**Dea** asked on 21 Feb 2023

I have a need for the navmenu to be like; Option1 Option2 Option2-Subopt1 Option2-Subopt2 Then when user clicks on Option2-Subopt1 or Option2-Subopt2 it navigates to the page. Example: public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem> { new DrawerItem { Title="Home", Text="Home", Icon="home", Url="./" }, new DrawerItem { Separator=true}, new DrawerItem { Title="General Search", Text="General Search", Icon="search", Url="GeneralSearch" }, etc.... If I want to say give users 2 search options under general search, How would I set that up?

## Answer

**Dimo** answered on 24 Feb 2023

Hello Deasun, We show how to achieve this in the Hierarchical Drawer example. Another option is to place a vertical Menu component inside the Drawer Template. Regards, Dimo
