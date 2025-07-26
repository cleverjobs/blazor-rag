# Adding Button to Grid Column Template

## Question

**DanDan** asked on 26 Feb 2020

I can add the button, but I need to be able to identify the row that the button was on in the @onclick event so that I can pop-up a form with information specific to that row.

## Answer

**Marin Bratanov** answered on 26 Feb 2020

Hello Dan, A custom command button gives you the item in its event arguments: [https://docs.telerik.com/blazor-ui/components/grid/columns/command.](https://docs.telerik.com/blazor-ui/components/grid/columns/command.) While this requires a dedicated command column, you may already have it for the CRUD operations. If you want to use a Template in a data column, you need to use a lambda expression in the OnClick handler so you can pass extra data from the context, something like this: <TelerikGrid Data="@MyData" Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px">
<Template>
@{
SampleData currItem=context as SampleData;
<TelerikButton OnClick="@( _=> HandleClick(currItem.Id) ) ">click me</TelerikButton>
<button @onclick="@( _=> HandleClick(currItem.Id) )">I do the same</button>
}
</Template>
</GridColumn>
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" />
</GridColumns>
</TelerikGrid>

@code { void HandleClick ( int theId ) {
Console.WriteLine(theId);
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x
}); public class SampleData { public int Id { get; set; } public string Name { get; set; }
}
} Regards, Marin Bratanov

### Response

**Dan** answered on 26 Feb 2020

That is exactly what I needed. Thank you.
