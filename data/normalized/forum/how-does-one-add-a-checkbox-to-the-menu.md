# How does one add a checkbox to the menu?

## Question

**Dou** asked on 25 Apr 2023

I've been weighing using the toolbar vs. the menu. I like that the menu allows for easy hierarchies, but the toolbar seems to be the way to go for including other elements like the checkbox. Any thoughts?

### Response

**Doug** commented on 25 Apr 2023

My code: <TelerikMenu Data="@MenuItems" ParentIdField="@nameof(MenuItem.SectionId)" IdField="@nameof(MenuItem.Id)" TextField="@nameof(MenuItem.Section)" UrlField="@nameof(MenuItem.Page)" DisabledField="@nameof(MenuItem.IsDisabled)" SeparatorField="@nameof(MenuItem.IsItemSeparator)" IconField="@(nameof(MenuItem.Icon))" Class="telMenu"> </TelerikMenu> @code {
public List <MenuItem> MenuItems { get; set; }

public class MenuItem
{
public int Id { get; set; }
public int? SectionId { get; set; }
public string Section { get; set; }
public string Page { get; set; }
public bool IsDisabled { get; set; }
public bool IsItemSeparator { get; set; }
public string Icon { get; set; }
public bool IsVisible { get; set; }
public string CssClass {get; set;}
public string IconClass { get; set; }
}

protected override void OnInitialized()
{
MenuItems=new List <MenuItem> ()
{
new MenuItem()
{
Id=0,
Section="Finalize",
Page="/",
Icon="buttonFinalize"
},
...

## Answer

**Dimo** answered on 28 Apr 2023

Hello Doug, The Menu provides an ItemTemplate, but it makes sense to use it only if all Menu items will have consistent structure and content. Otherwise you need conditionals inside the template and things become cumbersome. So, if you will have checkboxes in every Menu item, it's OK. Otherwise, with more varied item content it's better to go for the ToolBar. You can achieve hierarchy with SplitButtons or any other suitable component, depending on the exact scenario. The Menu is also not optimal if users will be clicking checkboxes and the goal for a child Menu is to remain open. In this case you need workarounds to prevent Menu closing. Regards, Dimo Progress Telerik

### Response

**Doug** commented on 28 Apr 2023

Dimo - Thanks for the advice. The SplitButton does, indeed, provide hierarchy, but I am struggling to get a single toolbar item which has an icon, shows the list upon clicking anywhere on it, fits wherever I put it on the toolbar (right now, it is above, but there may be a solution to that), and allows for lists within lists. It seems I can include 'Class="addFromIcon"' to get the icon, or I can include genImpAddFromSplitButton to remove the non-dropdown part of the button, but they won't both work together. I also tried putting a SplitButtonItems tag within a SplitButtonItem, but it failed. Any other advice would be welcome. <style>.buttonAddFrom {
@*sprite code*@}
.genImpAddFromSplitButton . k-button:first-child { display: none;
} </style> <TelerikSplitButton Title="Add From" Icon="@addFromIcon"> @* Class="addFromIcon genImpAddFromSplitButton"*@<SplitButtonContent> Add From </SplitButtonContent> <SplitButtonItems> <SplitButtonItem> Image Files
@* <SplitButtonItems> <SplitButtonItem> A </SplitButtonItem> <SplitButtonItem> B </SplitButtonItem> </SplitButtonItems> *@</SplitButtonItem> <SplitButtonItem> Open Encumbrances </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton> @code
string addFromIcon { get; set; }="buttonAddFrom";

### Response

**Dimo** commented on 28 Apr 2023

<TelerikSplitButton Title="Add From" Icon="@FontIcon.Calendar"> <SplitButtonItems> <SplitButtonItem> Image Files </SplitButtonItem> <SplitButtonItem> Open Encumbrances </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton>
