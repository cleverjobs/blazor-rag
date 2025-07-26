# Grid.SetState() doesn't work with observable collection

## Question

**Ber** asked on 15 May 2020

Hello, when I try to sort a grid, bound to an observable collection, it doesn't work. The function SetState does not exit Best Regards

## Answer

**Marin Bratanov** answered on 15 May 2020

Hi Bert, The following seems to work fine for me with the current latest 2.13.0. Am I missing something, or do you have a different scenario? @using Telerik.DataSource;
@using System.Collections.ObjectModel

<TelerikButton Primary="true" OnClick="@SetGridSort"> set sort from code</TelerikButton>

<TelerikGrid Data="@MyData" Height="400px" @ref="@Grid" Pageable="true" Sortable="true">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code { public TelerikGrid<SampleData> Grid { get; set; } async Task SetGridSort ( ) {
GridState<SampleData> desiredState=new GridState<SampleData>()
{
SortDescriptors=new List<SortDescriptor>()
{ new SortDescriptor { Member="Id", SortDirection=ListSortDirection.Descending }
}
}; await Grid.SetState(desiredState);
} public ObservableCollection<SampleData> MyData { get; set; }=new ObservableCollection<SampleData>(
Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
})
); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Bert** answered on 15 May 2020

I tried again and now it works. I don't know why it didn't work before. Thanks anyway and sorry for the the trouble

### Response

**Marin Bratanov** answered on 15 May 2020

No worries, Bert, it's best to check and if it's a bug that gives us the chance to improve the component. If it does come up again, let us know. Regards, Marin Bratanov
