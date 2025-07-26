# ref null if grid is inside a window

## Question

**Gia** asked on 22 Apr 2020

Hi I've put the grid inside a modal window All works but I cannot get the ref to the grid: I get null. Is it correct ? I need to put a filter by code when I show the window modal with grid tnx

## Answer

**Giampaolo** answered on 22 Apr 2020

Hi I've solved (I think) I moved the grid in another component, and inside the modal window I've put this component. Th ref is not null in OnAfterRenderAsync Any other solution ? Tnx anyway

### Response

**Svetoslav Dimitrov** answered on 23 Apr 2020

Hello Giampaolo, What you said in your second post about the OnAfterRenderAsync is correct and is one way to solve this. That is because the variable you are storing the reference to the Grid will be only populated after the component is rendered and its output includes the Grid. Until that point, there's nothing to reference. To manipulate components references after the component has finished rendering, use the OnAfterRenderAsync or OnAfterRender methods. More information on the lifecycle methods can be found in the Microsoft documentation here: [https://docs.microsoft.com/en-us/aspnet/core/blazor/lifecycle?view=aspnetcore-3.1#after-component-render](https://docs.microsoft.com/en-us/aspnet/core/blazor/lifecycle?view=aspnetcore-3.1#after-component-render) Having said that, below is a small example where the Grid is located directly inside a Telerik Modal Window. I have set a Task.Delay so that the component has time to render and populate the reference. @using Telerik.DataSource

<TelerikButton OnClick="@ShowWindow">Open Modal</TelerikButton>

<TelerikWindow Modal="true" Visible="@isVisible">
<WindowTitle>
<strong>My Grid in Modal Window</strong>
</WindowTitle>
<WindowContent>
<TelerikGrid Data="@MyData" @ref="GridReference" FilterMode="@GridFilterMode.FilterRow" Pageable="true" PageSize="10" Height="300px">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.ID))">
</GridColumn>
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name">
</GridColumn>
</GridColumns>
</TelerikGrid>
</WindowContent>
<WindowActions>
<WindowAction Name="Minimize" />
<WindowAction Name="Maximize" />
<WindowAction Name="Close" />
</WindowActions>
</TelerikWindow>

@code { public TelerikGrid<SampleData> GridReference { get; set; } public bool isVisible { get; set; } async Task ShowWindow ( ) {
isVisible=true; await Task.Delay( 20 ); //Gives time to the component to render and populate the reference await SetGridFilter();
} async Task SetGridFilter ( ) {
GridState<SampleData> desiredState=new GridState<SampleData>()
{
FilterDescriptors=new List<FilterDescriptorBase>()
{ new FilterDescriptor() { Member="ID", Operator=FilterOperator.IsGreaterThan, Value=10, MemberType=typeof ( int ) },
}
}; await GridReference?.SetState(desiredState);
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
ID=x,
Name="name " + x
}); //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; }
}
} Regards, Svetoslav Dimitrov
