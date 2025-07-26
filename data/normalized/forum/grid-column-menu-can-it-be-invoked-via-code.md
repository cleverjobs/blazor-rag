# Grid Column Menu...can it be invoked via code?

## Question

**Jef** asked on 30 Apr 2021

I'd like to have my own button invoke the GridColumnMenu... can this be done?

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hi Jeffrey, You could use JS Interop to click the appropriate element. Here's an example I made for you: @inject IJSRuntime _js

<TelerikButton OnClick="@ShowMenuForColumn2">show the menu for the second column</TelerikButton>

@* Move this script to its proper location in your project
It is here with the suppress-error hack to make the sample easy to copy*@<script suppress-error="BL9992"> function clickColumnMenu ( gridSelector, colIndex ) { let colMenuElems=document.querySelectorAll(gridSelector + " .k-grid-column-menu" ); let desiredElem=(colMenuElems !=null && colMenuElems.length>=colIndex) ? colMenuElems[colIndex] : null; debugger; if (desiredElem) {
desiredElem.click();
}
} </script> <TelerikGrid Data="@MyData" Class="target-grid" Pageable="true" PageSize="5" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="80px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> @code { async Task ShowMenuForColumn2()
{ await _js.InvokeVoidAsync( "clickColumnMenu", ".target-grid", 1 ); }

public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select( x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
});

public class SampleData {
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Jeffrey** commented on 30 Apr 2021

Thanks Marin.. is an actual API in the works?

### Response

**Marin Bratanov** commented on 30 Apr 2021

I don't think it will be considered anytime soon. Looking into that would weigh down the entire API of the component a lot, and is likely to make a lot of things cumbersome - if nothing else, the columns would have to start exposing references or other form of unique identification, and such a method would likely boil down to similar code to the js interop anyway. Using this js approach is perfectly valid.
