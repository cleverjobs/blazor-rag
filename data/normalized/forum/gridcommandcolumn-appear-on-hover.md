# GridCommandColumn Appear on Hover

## Question

**Sco** asked on 02 Nov 2020

Is there a good way to achieve this with the GridCommandColumn? I have tried a combination of visibility and floats without much luck. 19. Do not bloat your table with too many status icons or buttons Minimize the use of visual signs that may bloat your UI with indigestible content. Use mouse hovering to highlight one row at a time along with the relevant action buttons.

## Answer

**Marin Bratanov** answered on 03 Nov 2020

Hi Scott, You can cascade through the :hover pseudoclass on the grid rows to show buttons that normally have display: none. You can then use the grid state to put the grid in edit mode, if needed. Here's a basic example of the concept: <style>
.generally-hidden {
display: none; /* apply other styling as needed */ }

.hover-only-buttons .k-grid-content tr:hover .generally-hidden {
display: inline;
}
</style> <TelerikGrid Data="@MyData" Height="400px" Class="hover-only-buttons" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date">
<Template>
@{
SampleData item=context as SampleData;
<text>@item.HireDate.ToShortDateString()</text>
<button class="generally-hidden" @onclick="@( async ()=> await DoWork(item) )">Do Work</button>
}
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { async Task DoWork ( SampleData currRow ) {
Console.WriteLine(currRow.Id);
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Scott** answered on 03 Nov 2020

Thanks, I'll give that a shot.

### Response

**Scott** answered on 03 Nov 2020

So this works pretty well with standard buttons in a standard column. A small tweak gets them working as overlay buttons as well. .generally-hidden { display: none; position: absolute; left: 10px; top: 10px; /* apply other styling as needed */ } But what I was trying to achieve is doing this with the buttons in the GridCommandColumn. So the starting markup would look something like this: <TelerikGrid Data="@MyData" Height="400px" Class="hover-only-buttons" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridCommandColumn Width="0px"> <GatewayGridCommandButton Command="Edit" Icon="@IconName.Edit" Name="Edit" /> <GatewayGridCommandButton Command="Save" Icon="@IconName.Save" Name="Save" ShowInEdit="true" /> <GatewayGridCommandButton Command="Cancel" Icon="@IconName.Cancel" Name="Cancel" ShowInEdit="true" /> </GridCommandColumn> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> <Template> @{ SampleData item=context as SampleData; <text>@item.HireDate.ToShortDateString()</text> <button class="generally-hidden" @onclick="@( async ()=> await DoWork(item) )">Do Work</button> } </Template> </GridColumn> </GridColumns> </TelerikGrid>

### Response

**Marin Bratanov** answered on 04 Nov 2020

Hi Scott, This command column has a width set to 0px so it will not show up. A table is not designed to have content from one cell overlay the others by default so that's why you won't see the absolutely posiotioned buttons either. That's why I recommended using a "regular" column and adding buttons to it. In the template you could then add more HTML such as a div with position:relative to better control offsets with positioning. Now you have to review the grid rendering and hack through it. That said, I made another example for you that alters the grid settings to get that behavior so you can use it as base for further development: <style>.generally-hidden { display: none; position: absolute; /*changed these to keep the button in the row*/ left: 10px; top: 0px;
}.hover-only-buttons.k-grid-content tr:hover.generally-hidden { display: inline;
}.k-grid td.no-padding { /*reduce height*/ padding: 0; /*positioning per the button class*/ position: relative; /*overflow content over other cells*/ overflow: visible;
}.k-grid td.no-padding> span { /*see the grid rendering, needed for positioning*/ position: relative; display: block; height: 2em;
}
</style>

<TelerikGrid Data=" @MyData " Height="400px" Class="hover-only-buttons" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true">
<GridColumns>
<GridCommandColumn Width="0px" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" no-padding " )">
<GridCommandButton Command="Edit" Icon="@IconName.Edit" Class="generally-hidden" />
<GridCommandButton Command="Save" Icon="@IconName.Save" Class="generally-hidden" ShowInEdit="true" />
<GridCommandButton Command="Cancel" Icon="@IconName.Cancel" Class="generally-hidden" ShowInEdit="true" />
</GridCommandColumn>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code { async Task DoWork ( SampleData currRow )
{
Console.WriteLine(currRow.Id);
} public IEnumerable <SampleData> MyData=Enumerable.Range (1, 30).Select ( x=> new SampleData {
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData {
public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Scott** answered on 04 Nov 2020

Thank you, that is what we were looking for.
