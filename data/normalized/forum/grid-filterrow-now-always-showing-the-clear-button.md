# Grid FilterRow now always showing the clear button

## Question

**Dim** asked on 31 Jan 2022

After upgrading to version 3 we now always get the clear filter button in our filter row Before the upgrade this button would only show up after we typed something in the filter, now it is always there even when the filter is empty. Is there a way to return to the old behaviour? Kind Regards Dimitri

## Answer

**Hristian Stefanov** answered on 03 Feb 2022

Hi Dimitri, Currently, you can define one boolean that tracks when the data is filtered and conditionally hide the button with custom CSS style. The OnRead event will help you track whether the Grid is filtered. I have prepared an example for you: @using Telerik.DataSource
@using Telerik.DataSource.Extensions

@if (!ShowClearBtn)
{ <style>.k-filtercell-operator> button { display: none;
} </style> } <TelerikGrid TItem="@SampleData" OnRead="@OnReadHandler" Sortable="true" FilterMode="@GridFilterMode.FilterRow" Pageable="true" PageSize="15" Height="400px"> <GridColumns> <GridColumn Field="Id" /> <GridColumn Field="Name" /> <GridColumn Field="Team" /> <GridColumn Field="HireDate" /> </GridColumns> </TelerikGrid> @code {
public bool ShowClearBtn { get; set; }=false;

async Task OnReadHandler(GridReadEventArgs args)
{
if (args.Request.Filters.Count> 0)
{
ShowClearBtn=true;
}
else
{
ShowClearBtn=false;
}
var result=PristineData.ToDataSourceResult(args.Request);

args.Data=result.Data;
args.Total=result.Total;
}

public IEnumerable <SampleData> PristineData=Enumerable.Range(1, 300).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
});

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public DateTime HireDate { get; set; }
}
} Please run and test it to see the result. Additionally, we have a feature request scheduled for our next 3.1.0 release that will give you the option out of the box to hide filter buttons: Option to hide grid filter operators and set default filter operator Upon interest, you can take a look there as well. Regards, Hristian Stefanov Progress Telerik
