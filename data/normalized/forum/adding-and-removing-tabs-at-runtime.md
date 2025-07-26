# Adding and Removing Tabs at runtime

## Question

**Dou** asked on 11 Jun 2020

I would like to add and remove tabs at runtime and the contents of each tab will be a child component. I've seen the example on how to bind the tabstrip to a collection but it is not displaying the child component. I also need a close button on the tab itself. The use case is as follows: The first tab is a grid of data (let's say cars for this example). When you click on a row, a new tab will be spawned with the car details (child component) shown and the title of the tab with be the car name. As you click on more cars, more tabs will open until the user closes the tabs. Can this tabstrip control handle this use case? Thanks, Doug

## Answer

**Marin Bratanov** answered on 12 Jun 2020

Hi Doug, When this gets implemented, you will be able to put buttons in the tab headers to remove them: [https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.](https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.) Combined with a loop over a tab descriptor collection (like the last sample here ), you can add/remove or show/hide elements from the list, and render components in them (also pass parameters to them). For the time being, you'd have to put a close button in the tab content. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 12 Jun 2020

Since you mentioned clicks on grid rows, you may want to Follow that feature too: [https://feedback.telerik.com/blazor/1417387-row-click-and-double-click-events.](https://feedback.telerik.com/blazor/1417387-row-click-and-double-click-events.) In the meantime, you can use the selection feature. Here's a sample of that and of looping to create tabs that I made for you: <TelerikTabStrip>
<TabStripTab Title="Main View">
<TelerikGrid Data=@GridData
SelectionMode="@GridSelectionMode.Multiple" SelectedItems="@SelectedItems" SelectedItemsChanged="@((IEnumerable<Employee> employeeList)=> OnSelect(employeeList))" Pageable="true" Height="400px">
<GridColumns>
<GridCheckboxColumn />
<GridColumn Field=@nameof (Employee.Name) />
<GridColumn Field=@nameof (Employee.Team) Title="Team" />
</GridColumns>
</TelerikGrid>
</TabStripTab>
@{ foreach (MyTabModel item in tabs.Where(t=> t.Visible==true ))
{

<TabStripTab Title="@item.Title" Disabled="@item.Disabled">
@* in the future, the button would go in the title template
For the time being you can look into special styling such as absolute or relative positioning*@<TelerikButton Icon="@IconName.Close" OnClick="@( ()=> item.Visible=false )"></TelerikButton>

<TabContent Name="@item.Title" />
</TabStripTab>
}
}
</TelerikTabStrip>

@code {
List<MyTabModel> tabs { get; set; }=new List<MyTabModel>(); public List<Employee> GridData { get; set; } public IEnumerable<Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); protected void OnSelect ( IEnumerable<Employee> employees ) {
SelectedItems=employees;
PopulateTabs();
} void PopulateTabs ( ) { foreach (Employee item in SelectedItems)
{
MyTabModel currItemModel=tabs.Where(t=> t.Title==item.Name).FirstOrDefault(); if (currItemModel !=null )
{ //this can toggle the tab back on for items that have already been selected, but the user "closed" their tabs //decide whether to use it according to your business logic //currItemModel.Visible=true; } else {
tabs.Add( new MyTabModel { Title=item.Name, Visible=true });
}
}
} protected override void OnInitialized ( ) {
GridData=new List<Employee>(); for ( int i=0; i <15; i++)
{
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3 });
} // select Employee with ID 4 SelectedItems=GridData.Where(item=> item.EmployeeId==4 ).ToList();
PopulateTabs();
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; }
} public class MyTabModel { public string Title { get; set; } public bool Disabled { get; set; } public bool Visible { get; set; }
}
} and for this example, here's a simple <TabContent> component that just generates some data to show per each tab and according to the parent value (of course, feel free to edit the parameters, descriptors and data retrieval and content): <TelerikGrid Data=@GridData
Pageable="true" Height="400px">
<GridColumns>
<GridCheckboxColumn />
<GridColumn Field=@nameof (SampleData.EmployeeName) />
<GridColumn Field=@nameof (SampleData.SomeExtraInfo) Title="Metadata" />
</GridColumns>
</TelerikGrid>

@code {
[ Parameter ] public string Name { get; set; } public List<SampleData> GridData { get; set; } protected override async Task OnParametersSetAsync ( ) { //here we just generate some data, in a real case - fetch it from actual data service GridData=new List<SampleData>(); for ( int i=0; i <15; i++)
{
GridData.Add( new SampleData()
{
EmployeeName=Name,
SomeExtraInfo="more data " + i
});
}
} public class SampleData { public string EmployeeName { get; set; } public string SomeExtraInfo { get; set; }
}
} Regards, Marin Bratanov

### Response

**Doug** answered on 12 Jun 2020

Thanks Marin. I've got the selected event working and used the loop process to add tabs but the child component is not rendering from within the new tabs. I added a content property to the public class MyTabModel { public string Title { get; set; } public object Content { get; set; } }

### Response

**Doug** answered on 12 Jun 2020

Thanks Marin. I've got the selected event working and used the loop process to add tabs but the child component is not rendering from within the new tabs. I added a content property to the tab model object but this does not seem to be the proper way to get a child control to render. public class MyTabModel { public string Title { get; set; } public object Content { get; set; } } foreach (MyTabModel item in tabs) { <TabStripTab Title="@item.Title" Disabled="@item.Disabled">@item.Content</TabStripTab> }

### Response

**Doug** answered on 12 Jun 2020

To clarify, each tab could have a different child component.

### Response

**Marin Bratanov** answered on 12 Jun 2020

Hi Doug, The Content of a tab is a RenderFragment. Creating a component instance programmatically into one is messy, at best, and hard to maintain. It is one way to render different things. Once you can render components of yours programmatically like that in a simple RenderFragment, you would be able to use this in the tabs too. Another, more blazor-y way, is to choose one of the following options: use an if-block sequence to choose what component to render in the markup render the same component in the tab strip, pass all needed information as parameters to it, and let it decide what to render in its own markup based on the parameter data Regards, Marin Bratanov

### Response

**Doug** answered on 12 Jun 2020

Here's an example of how the TabStrip could look after spawning a few tabs (minus the parameter). <TelerikTabStrip> <TabStripTab Title="Data"><PrjInvGrid /></TabStripTab> <TabStripTab Title="SKU 1"><InventoryItem /></TabStripTab> <TabStripTab Title="SKU 2"><InventoryItem /></TabStripTab> <TabStripTab Title="Sales Order 1"><SO /></TabStripTab> <TabStripTab Title="Purchase Order 1"><PO /></TabStripTab> </TelerikTabStrip>

### Response

**Marin Bratanov** answered on 12 Jun 2020

If you have several types of components you can also make several tab descriptor collections and several loops to create tabs. Regards, Marin Bratanov

### Response

**Doug** answered on 12 Jun 2020

Thanks for the followup. I like your second option of creating a single Tab component that will handle showing the different UI's depending on what the tab is.

### Response

**Marin Bratanov** answered on 15 Oct 2020

To anyone looking for similar examples, we just made one: [https://github.com/telerik/blazor-ui/tree/master/tabstrip/DynamicTabs](https://github.com/telerik/blazor-ui/tree/master/tabstrip/DynamicTabs) Regards, Marin Bratanov

### Response

**Jeff** answered on 09 Feb 2021

I've followed that example and messed with the demo but even using the @key attribute I am not getting a refresh of the same component in different tabs. If I switch to a tab that does not use the component, then back to one that does, it will refresh the tab and unfortunately, the data call as well. I was really hoping to have "pre-rendered" tabs that could be switch between without calling actually reloading the tab contents, including calling the API. Is this just not a likely possibility with Blazor, let alone the tabstrip?

### Response

**Marin Bratanov** answered on 10 Feb 2021

Hello Jeff, The truly Blazor way is to do what we do right now - remove all old content when a tab deactivates and replace it with the new one. This causes the behavior you see - components going away and initializing from scratch, and if you use the same components you must use @key to ensure they re-render properly - the framework tries to minimize renders. That said, we do see some value in the ability to have all the content and to toggle it with CSS, and you can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) I've added your Vote on your behalf to raise its priority. In the meantime, I can also suggest you consider keeping data and component state in the parent component (where the tab strip is declared) or in an application state (such as a service) so that you can avoid making data requests every time a tab activates, but instead use a form of cache. That would also be the Blazor way to do this, while keeping the render tree small. You could even implement a memory cache in the data service so that even if it is called, it could pull the previous data from memory unless a certain amount of time has elapsed since the last time the cache was updated. Regards, Marin Bratanov

### Response

**Jeff** answered on 11 Feb 2021

Marin, thanks for directing me to the new feature and adding my vote. Shortly after posting that comment I managed to realize that the @key attribute needs to be added to MY COMPONENT, not the TabStripTab. This solved my problem of having each tab function independently and I thought it might be a useful observation for anyone else that might be struggling with this advanced setup. BTW, love the toolset, in general.

### Response

**Marin Bratanov** answered on 12 Feb 2021

Hello Jeff, It is good to see you make progress, and I am happy that you like our tools, I do hope they bring you a boost in productivity :) Regards, Marin Bratanov
