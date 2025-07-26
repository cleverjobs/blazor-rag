# Treeview and navigation problem

## Question

**Syl** asked on 14 May 2020

Hello, I'm working on a hosted webassembly project with .net core 3.2 RC1 and Visual Studio 16.6.0 Preview 6 I would like to use the treeview to present a search result hierarchically and navigate to an other page when the user clicks on a child item. I use the templates and <a> tag. The problem is that if i use <a href="customerPage">test url</a> for example, it throw an exception when i click on the link and the page "customerPage" is not rendered. The issue is the same with a <NavLink> tag. If i use the <a> tag with the onclick event associated to the NavigationManager in a code behind function, it seems to work, but i can see an exception in the the browser's console. To reproduce the problem, I have created a new Hosted Client Side project. I added a treeview in the index.razor file and use the code of your "Flat Data" demo to populate the treeview and update the counter page to pass a CounterValue parameter. I took some screenshot after clicking on the different links. Here is the code : Index.razor @page "/"<h1>Hello, world!</h1>
Welcome to your new app.
<SurveyPrompt Title="How is Blazor working for you?" /><TelerikTreeView Data="@FlatData"> <TreeViewBindings> <TreeViewBinding ParentIdField="Parent" ExpandedField="IsExpanded"> <ItemTemplate> @{ var item=(context as TreeItem);
<span>(a href) <a href="counter/@item.Id">id:@item.Id</a>&nbsp; | &nbsp;</span> <span> (navlink)<NavLink href="counter">no id</NavLink>&nbsp; | &nbsp;</span> <span> (a onclick) <a href="javascript:void(0)" @onclick="@( _=> Navigate(item))">id:@item.Id</a></span> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings></TelerikTreeView> Index.razor.cs using System; using System.Collections.Generic; using System.Linq; using System.Threading.Tasks; using Microsoft.AspNetCore.Components;
namespace BlazorApp2.Client.Pages
{
public partial class Index {
public IEnumerable<TreeItem> FlatData { get; set; }
[Inject] private NavigationManager NavigationManager { get; set; }
public class TreeItem //most fields use the default names and will bind automatically in this example {
public int Id { get; set; }
public string Text { get; set; }
public int? Parent { get; set; } //this is a non-default field name public bool HasChildren { get; set; }
public bool IsExpanded { get; set; } //this is a non-default field name }
protected override void OnInitialized()
{
FlatData=LoadFlat();
}
private void Navigate(TreeItem item)
{
var uri=$"counter/{item?.Id.ToString() ?? ""}";
NavigationManager.NavigateTo(uri);
}
private List<TreeItem> LoadFlat()
{
List<TreeItem> items=new List<TreeItem>();
items.Add(new TreeItem()
{
Id=1,
Text="Parent 1",
Parent=null, // indicates a root (zero-level) item HasChildren=true, // informs the treeview there are children so it renders the expand option IsExpanded=true // an item can be expanded by default });
items.Add(new TreeItem()
{
Id=2,
Text="Parent 2",
Parent=null, // indicates a root item HasChildren=true,
IsExpanded=false });
items.Add(new TreeItem()
{
Id=3,
Text="Parent 3",
Parent=null, // indicates a root item HasChildren=false, //there will be no children in this item IsExpanded=true // will not have an effect if there are no children });
items.Add(new TreeItem()
{
Id=4,
Text="Child 1 of Parent 1",
Parent=1, // the parent will be the first item HasChildren=false,
IsExpanded=false });
items.Add(new TreeItem()
{
Id=5,
Text="Child 2 of Parent 1",
Parent=1, // the parent will be the first item HasChildren=true,
IsExpanded=true });
items.Add(new TreeItem()
{
Id=6,
Text="Child 1 of Child 2",
Parent=5, // the parent will be the first child of the first root item HasChildren=false,
IsExpanded=false });
items.Add(new TreeItem()
{
Id=7,
Text="Child 1 of Parent 2",
Parent=2, // the parent will be the second root item HasChildren=false,
IsExpanded=false });
return items;
}
}
} Counter.razor @page "/counter"@page "/counter/{counterValue:int}"<h1>Counter</h1><p>Current count: @CounterValue</p><button class="btn btn-primary" @onclick="IncrementCount">Click me</button> Counter.razor.cs using Microsoft.AspNetCore.Components;
namespace BlazorApp2.Client.Pages
{
public partial class Counter {
[Parameter] public int CounterValue { get; set; }
private void IncrementCount()
{
CounterValue++;
}
}
}

## Answer

**Marin Bratanov** answered on 14 May 2020

Hi Sylvain, The treeview can generate links for you - you only need to provide the UrlField: [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview) That said, simple <a> or <NavLink> elements in the template should not cause errors and if they do - my best guess is that something is wrong with the app itself - maybe a wrong base URL. Judging from the first screenshot - there seems to be a JS error thrown by some scripts on the page, and that can break the entire app. Could you try resolving that to see if it helps? I'm attaching here an app that seems to work fine for me so you can compare against it and see what's the difference causing the navigation issues in the problematic app. If this does not get you closer to a solution, please modify my sample to showcase the Telerik problem you are facing so I can have a look. Regards, Marin Bratanov

### Response

**Sylvain** answered on 14 May 2020

Hi Marin, Thank you for your reply, I hadn't paid attention that the treeview can manage url directly, but I still have my problem. Your project works but it is not the same use case because you put the treeview in the NavMenu.razor component, so the treeview is not disposed when you navigate. In my project I use the treeview in a similar case and it works correctly but in the "search result" case, my treeview is not in the menu but in a component like in the index.razor or counter.razor of the test project. I tested your solution by copying the treeview code contained in the NavMenu to the Index.razor. When I click on the "Some Component" item of the treeview which is in the NavMenu.razor component, it works correctly but if I click on the same item of the treeview which is in the index.razor page, I have the exception. I did some other tests, it appears the problem exists in Chrome (81.0.4044.138) and Edge Chromium (81.0.416.72) (what seems to be normal) with all extensions disabled in normal or InPrivate mode. The only thing is the first exception (after loading) disapears after having disabled the extensions (I only use Adblock Plus 3.8.4, Ghostery 8.5.0 and Redux DevTools 2.17.0). In Firefox (76.0.1) there is no problem... I took some screenshot because I can't upload a zip file with the updated solution. Thank you Sylvain

### Response

**Marin Bratanov** answered on 14 May 2020

Thank you for the clarification. I had assumed that a navigation component would be outside of the @Body. I logged this issue for research and fixing, and you can Follow its progress here: [https://feedback.telerik.com/blazor/1466134-navigating-and-disposing-a-menu-throws-errors-in-a-webassembly-app](https://feedback.telerik.com/blazor/1466134-navigating-and-disposing-a-menu-throws-errors-in-a-webassembly-app) On a side note, if you open a private support ticket, you will be able to attach archives, this forum thread only allows images. Regards, Marin Bratanov

### Response

**Sylvain** answered on 14 May 2020

Ok Thank you Have a nice day Regards

### Response

**Marin Bratanov** answered on 14 May 2020

I just thought of this - depending on what kind of navigation and UI/UX you seek, maybe using the Menu with Vertical orientation can serve your needs? Regards, Marin Bratanov
