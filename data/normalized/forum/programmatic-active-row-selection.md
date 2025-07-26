# Programmatic active row selection

## Question

**SLSL** asked on 16 Jan 2020

Is there a way to programmatically select an active row in the Grid? And if the active row is not visible allow scrolling the active row into view? Thanks.

## Answer

**Marin Bratanov** answered on 16 Jan 2020

Hello Joel, You can select a row programmatically by using two-way binding on the SelectedItems collection: single selection: [https://docs.telerik.com/blazor-ui/components/grid/selection/single#two-way-binding-of-selecteditems](https://docs.telerik.com/blazor-ui/components/grid/selection/single#two-way-binding-of-selecteditems) multiple selection: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems) You may also find useful this sample: [https://github.com/telerik/blazor-ui/tree/master/grid/persist-selection](https://github.com/telerik/blazor-ui/tree/master/grid/persist-selection) With the keyboard support that we introduced in our latest release, the user can also use the up/down arrows to move around the rows, and that will also scroll the grid. There is no built-in feature for scrolling to a specific selected row, however. If you are using single selection you could use JS interop to find the row the has the selected state and call its .scrollIntoView() method. For multiple row selection that would become a heuristic task, however. Regards, Marin Bratanov

### Response

**SL** answered on 16 Jan 2020

You guys are great, very fast response. Thank you very much.

### Response

**Michael** answered on 24 Mar 2020

"There is no built-in feature for scrolling to a specific selected row, however. If you are using single selection you could use JS interop to find the row the has the selected state and call its .scrollIntoView() method." Can you elaborate about how to do this? After an update I want to be able to select a row and make sure is viewable in the grid. I know virtually nothing about JS (hence my enthusiasm for Blazor) so an actual example would be great. Mike V.

### Response

**Marin Bratanov** answered on 24 Mar 2020

Hello Michael, Here's a sample JS function that expects a CSS selector to find the correct grid, then finds the first selected row and calls its .scrollIntoView() method: function scrollToSelectedRow ( gridSelector ) { var gridWrapper=document.querySelector(gridSelector); if (gridWrapper) { var selectedRow=gridWrapper.querySelector( "tr.k-state-selected" ); if (selectedRow) {
selectedRow.scrollIntoView();
}
}
} and here is a sample way of calling it (see the SelectItem method from the button click): @inject IJSRuntime JsInterop

<TelerikButton OnClick="@SelectItem">Select item</TelerikButton>

<TelerikGrid Data=@GridData
SelectionMode="GridSelectionMode.Single" @bind-SelectedItems="SelectedItems" Pageable="true" PageSize="30" Height="300px" Class="@theGridClass">
<GridColumns>
<GridColumn Field=@nameof (Employee.Name) />
<GridColumn Field=@nameof (Employee.Team) Title="Team" />
</GridColumns>
</TelerikGrid>

@code { string theGridClass { get; set; }="theSpecialGrid"; async Task SelectItem ( ) { // select item 11 which would be hidden initially SelectedItems=GridData.Where(item=> item.EmployeeId==11 ).ToList(); await Task.Delay( 20 ); //rougly one rendering frame so this has the chance to render in the browser await JsInterop.InvokeVoidAsync( "scrollToSelectedRow", "." + theGridClass);
} public List<Employee> GridData { get; set; } public IEnumerable<Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); protected override void OnInitialized ( ) {
GridData=new List<Employee>(); for ( int i=0; i <55; i++)
{
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3 });
}
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; }
}
} Regards, Marin Bratanov

### Response

**Michael** answered on 25 Mar 2020

Marin: Thanks for the prompt reply and sample code. This solves half of my problem; in addition to being able to select the row and scroll it into view I need to select the correct page that the row appears on. Imagine a grid with 100 rows with 10 rows per page. The user edits row 5 and as a consequence of the changes it will now be the 25th row of the grid-- so it's now on page 3. I need to both select page 3, select the row and make sure it's visible. I thought I could set a reference to the grid component and select the page in code, but that only changes the page selector at the bottom of the grid, it doesn't advance the contents of the grid so that it's showing the rows on that page. (at least when I do it). Can you please provide an example of how to move to a different page of the grid? Thanks

### Response

**Marin Bratanov** answered on 25 Mar 2020

Hello Michael, You can set the Page parameter of the grid to make it go to a different page: <TelerikNumericTextBox @bind-Value="@DesiredPage" Min="1" Max="34"></TelerikNumericTextBox>

<TelerikGrid Data="@MyData" Pageable="true" PageSize="15" Page="@DesiredPage" Height="500px">
<GridColumns>
<GridColumn Field="ID"></GridColumn>
<GridColumn Field="TheName" Title="Employee Name"></GridColumn>
</GridColumns>
</TelerikGrid>

@code { int DesiredPage { get; set; }=1; public IEnumerable<object> MyData=Enumerable.Range( 1, 500 ).Select(x=> new { ID=x, TheName="name " + x });
} Regards, Marin Bratanov

### Response

**Michael** answered on 25 Mar 2020

Thanks. That works great.

### Response

**Michael** answered on 19 Oct 2020

Great, thx for the quick reply that helps

### Response

**Roger Graham** answered on 21 Dec 2020

Hello, How to get the page number of selected item? So that we can set PageNumber dynamically to navigate to that grid view.

### Response

**Marin Bratanov** answered on 21 Dec 2020

Hello Roger, You could start with the approach described here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-index-of-grid-row.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-index-of-grid-row.) The example shows how to get the index of a particular item, in a similar fashion you could get that index according to all the data you have, not just the current page (that logic is entirely up to the app, the grid cannot influence the way you obtain data, and especially how to do this in a performant manner). Then, since you know the PageSize, you can perform the calculation to know which Page this item is on. Regards, Marin Bratanov

### Response

**John** commented on 11 Aug 2021

fyi, scrolling into view with a virtual grid worked fine in 2.22.0 but broke in 2.24. Not sure how or why this broke, but now you can scroll to the item, but the list will render as empty, just with the scrollbar visible. If you manually scroll a bit, the grid will update and items will rerender. Trying to figure out how to make the grid rerender after this now. I would go back to 2.22.0 but its no longer in the nuget package source.

### Response

**Dimo** commented on 13 Aug 2021

Hey John, Scrolling to a Grid row in virtual mode should rely on the Skip property of the Grid state. Are you using this approach? What exactly isn't working with new versions? Can you share your implementation? @using Telerik.DataSource.Extensions

<p>
<label>
Type a Row ID between 1 and @Data.Count :
<TelerikNumericTextBox Min="1" Max="@Data.Count" @bind -Value="@RowID" />
</label>
<TelerikButton OnClick="@ScrollToRow">Scroll to this ID</TelerikButton>
</p>

<TelerikGrid @ref="@MyGrid" Data="@CurrentData" TotalCount="@CurrentTotal" ScrollMode="GridScrollMode.Virtual" PageSize="100" Height="480px" RowHeight="48" OnRead="@OnGridRead">
<GridColumns>
<GridColumn Field="ID" Width="200px"></GridColumn>
<GridColumn Field="Name"></GridColumn>
</GridColumns>
</TelerikGrid> @code { private List<GridItem> Data { get; set; } private IEnumerable<GridItem> CurrentData { get; set; } private int CurrentTotal=0; private int RowID=1; private TelerikGrid<GridItem> MyGrid { get; set; } private async Task ScrollToRow()
{ var state=MyGrid.GetState(); // the line below assumes no sorting or filtering. // in more complex scenarios, calculate the desired row position // based on the whole Grid data set and the current sorting/filtering state state.Skip=Math.Min(RowID - 1, Data.Count - 9 ); await MyGrid.SetState(state);
} private async Task OnGridRead(GridReadEventArgs args)
{ var result=Data.ToDataSourceResult(args.Request);
CurrentData=(result.Data as IEnumerable<GridItem>).ToList(); ;
CurrentTotal=result.Total;
} protected override async Task OnInitializedAsync()
{
Data=new List<GridItem>(); for (int i=1; i <=1000; i++)
{
Data.Add( new GridItem()
{
ID=i,
Name="Name " + i
});
}
} public class GridItem
{ public int ID { get; set; } public string Name { get; set; }
}
}

### Response

**Rob** commented on 11 Nov 2024

I know this is old and hoping there is a better approach in later Blazor versions. Is the ONLY way to programmatically selected a row in a TelerikGrid is to use JS? Isn't that self-defeating? The entire reason we went with Blazor-Server was to avoid the need for JS? I would have thought one could add models to the .SelectedItems list to achieve that ... no? Rob.

### Response

**Dimo** commented on 12 Nov 2024

@Rob - just to clarify for anyone else who ends up here - programmatic row selection is possible without JavaScript by changing the Grid SelectedItems parameter value. Programmatic scrolling to a specific row on the current page requires JavaScript, but we have: A feature request about this. I voted on your behalf, but the demand is still low. A KB article - Scroll to selected Telerik Blazor Grid row.

### Response

**Rob** commented on 12 Nov 2024

@Dimo - Yes the SelectedItems does work but there are some gotcha's I ran into: 1. If adding to the SelectedItems list in a page's OnAfterRenderAsync(bool firstRender) any bound UI elements to SelectedItems will trigger an exception (null ref) when a StateHasChanged() is executed ... this is done on initial page load so that a "row" (selected item) will be highlighted by default. My work around (until and if I can find a better approach) is to create a bunch of local variables that will get assigned values from the model via the OnRowClickHandler() event and they are bound to the UI controls (i.e. TelerikTextBox). This is the only way I've been able to avoid the null exception. 2. When SelectionMode="GridSelectionMode.Single", and using OnRowClickHandler to clear the SelectedItems list and then Add the current row (args.Item) to the SelectedItems. This works, but it doesn't feel right. My expectation was that when I click on another row and in Single mode, then I would be able to bind to a "SelectedItem" (not plural) and that would automatically be updated (I don't have to use an event like OnRowClick) as the user selects a row. As it stands now, the code flow isn't following the intention of "binding" and feels more like a work-around. As far as scrolling to row not on the current page for the grid, we don't currently have a need for that as we use the built-in filters to narrow grid results. Multi-select across pages is not a good UI approach, been there done that, users hated it as they can't see everything they've selected.

### Response

**Dimo** commented on 13 Nov 2024

@Rob - 1. (Selecting in OnAfterRenderAsync ) The described algorithm works on my side: [https://blazorrepl.telerik.com/QSvlbRuL15oX5Abu11](https://blazorrepl.telerik.com/QSvlbRuL15oX5Abu11) 2. (Using OnRowClick for row selection) Single selection is a special case of multiple selection. That's why the Grid has only one parameter for its selected rows. Imagine a scenario in which you need to toggle between single and multiple selection in the same Grid instance. The need to use two separate parameters to track the selected items will be cumbersome. And yes, you don't need OnRowClick to select items. I assume the problem is a missing two-way binding for SelectedItems. The above example includes this scenario too.

### Response

**Rob** commented on 14 Nov 2024

@Dimo 1. Not working on my side ... OnRowClick never gets triggered from within OnAfterRenderAsync. .NET 7 Blazor-Server. We do inject a ProcessingService to handle display of an animated progress wheel during OnAfterRenderAsync. Maybe I'm missing something to ensure, not to worry. 2. All good and understand. Rob
