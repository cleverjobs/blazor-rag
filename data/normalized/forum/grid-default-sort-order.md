# Grid Default Sort Order

## Question

**Pet** asked on 06 Sep 2024

Hello Telerik, I want to confirm this is the recommended way to create the Default Sort Order for a Grid. Thank you. TelerikGrid Data="@MyData" Sortable="true" AutoGenerateColumns="true"
OnStateInit="@((GridStateEventArgs <SampleData> args)=> OnStateInitHandler(args))"> </TelerikGrid> @code {
async Task OnStateInitHandler(GridStateEventArgs <SampleData> args)
{
var state=new GridState <SampleData> {
SortDescriptors=new List <Telerik.DataSource.SortDescriptor> {
new Telerik.DataSource.SortDescriptor{ Member="LastModified", SortDirection=Telerik.DataSource.ListSortDirection.Descending }
}
};

args.GridState=state;
}

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 5).Select(x=> new SampleData
{
Id=x,
LastModified=new DateTime(2022, x, 28)
});

public class SampleData
{
public int Id { get; set; }

public DateTime LastModified { get; set; }
}
}

## Answer

**Marco** answered on 09 Sep 2024

Hy Peter, In the OnStateInit method I set the default sorts in this way,: I follow the OnStateInit event documentation on Blazor Grid - State - Telerik UI for Blazor. Regards
