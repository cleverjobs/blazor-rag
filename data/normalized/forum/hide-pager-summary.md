# Hide Pager Summary

## Question

**Mat** asked on 29 Oct 2020

Is there a way to hide the counter on the pager? I don't need to see 1-3 of 75 items especially in mobile view. Takes up more space than necessary.

## Answer

**Svetoslav Dimitrov** answered on 29 Oct 2020

Hello Matt, You could use CSS to apply a display: none rule to the span that contains the information. Below, you could see an example of how I achieved it. A short summary of what I did was to add a custom CSS class to the Grid using its Class parameter to apply the CSS rules only to that instance of the Grid. After that, I created a suitable selector and applied the necessary rule. <style>.myGridClass.k-pager-info.k-label { display: none;
}
</style> <TelerikGrid Data=" @MyData " Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true" Class="myGridClass">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code { public IEnumerable <SampleData> MyData=Enumerable.Range (1, 30).Select ( x=> new SampleData {
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData {
public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Svetoslav Dimitrov

### Response

**Matt** answered on 30 Oct 2020

Perfect!!! Thank you Svetoslav.
