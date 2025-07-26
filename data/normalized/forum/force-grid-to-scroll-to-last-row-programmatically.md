# Force grid to scroll to last row programmatically?

## Question

**RobRob** asked on 14 Jan 2025

Background: Grid bound to a List provided by EF from SQL data source. Pageable=true. EditMode=Incell. Process: 1. User clicks Add button 2. In the Add event handler for the button, a new object instance is created and added to the List that is Data bound to the grid (last item in the List not an Insert ... this is a user requirement and must be added to end of List) 3. StateHasChange(), Grid?.Rebind 4. Force the grid to scroll to the last item. I researched and found this Telerik documentation Scroll to Selected Grid Row and it suggests I have to use JavaScript "scrollIntoView()"?? I absolutely do NOT want to go this route for what should be a very simple process. Please tell me there is a better way? I was "hoping" I could use SelectionMode=Single and bind SelectedItemsInPage and then programmatically set the SelectedItem to the last item in the List (Data=) and Telerik Grid would do the control update to appropriate page and make the last row visible in the grid. Unfortunately this is not the case. Do you folks have a more Blazor-Server like approach for .NET 9 and 7.1.0 suite? Rob.

## Answer

**Dimo** answered on 15 Jan 2025

Hi Rob, Programmatic scrolling in the Grid is an existing feature request. When NOT using row virtualizatio, it requires JavaScript, but the implementation in your case can be a lot simpler, because there is no dependency to a specific row. If there is only one Grid instance on the page, you don't need the custom CSS class either. The only consideration is that if the user is not on the last Grid page, then the app needs to navigate to it first. @inject IJSRuntime JsInterop @*Move to external .js file *@<script suppress-error="BL9992"> function scrollToLastGridRow ( gridClass ) { var lastRow=document.querySelector( `. ${gridClass}.k-grid-content tr:last-child` ); if (lastRow) {
lastRow.scrollIntoView({ behavior: "smooth" });
}
} </script> <TelerikButton OnClick="@ScrollToLastGridRow">Scroll To Last Grid Row</TelerikButton> <TelerikGrid Data="@GridData" Height="300px" Class="js-scrollable-grid"> <GridColumns> <GridColumn Field="@nameof(Employee.Name)" /> </GridColumns> </TelerikGrid> @code {
private List<Employee> GridData { get; set; }=new ();

private async Task ScrollToLastGridRow ( ) { await JsInterop.InvokeVoidAsync( "scrollToLastGridRow", "js-scrollable-grid" );
}

protected override void OnInitialized ( ) { for (int i=1; i <=20; i++)
{
GridData.Add( new Employee ( ) {
EmployeeId=i,
Name=$ "Employee {i}" });
}
}

public class Employee {
public int EmployeeId { get; set; }
public string Name { get; set; }=string.Empty;
}
} Regards, Dimo Progress Telerik

### Response

**Rob** commented on 15 Jan 2025

Thanks for quick response Dimo. Is the feature request in your development queue? For now, the users will just be told to goto the last row on the last page as adding JS is not an option, just way too many issues with JS and browser versions on various platforms. Appreciate your code sample response. Rob.

### Response

**Dimo** commented on 15 Jan 2025

The Unplanned status means that the feature request is confirmed to be valid, but not scheduled for implementation yet. Usually, the request should gain more popularity to justify the time to develop, test, document, etc.
