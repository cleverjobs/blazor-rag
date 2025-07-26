# How to re-order TelerikGrid columns programmatically

## Question

**Mar** asked on 17 May 2024

Hello, I have the following requirement, I need to be able to re-order telerik grid columns programmatically. I have come up with a simple sample project to demonstrate the need, but I've noticed that although it re-orders the columns the first time I press a button (see sample), it does not re-order the columns after that....something which I find very peculiar. Notice, I tried two approaches in re-ordering columns, one using simple rearrangement of <GridColumn>s and another is to muck around with Grid state object (_grid.GetState()). Any help is greatly appreciated. <div style="width: 100%; height: 100%"> <TelerikGrid TItem="@Model" FilterMode="@GridFilterMode.FilterRow" SelectionMode="GridSelectionMode.Single" EnableLoaderContainer="true" Pageable="false" Sortable="true" Height="100%" OnStateChanged="OnStateChanged" Data="Data" @ref=@_grid> <GridColumns> @{
foreach (var col in ColumnOrder)
{
if (col==1)
{ <GridColumn Field="@(nameof(Model.One))" FieldType="@(typeof(string))" Title="One Values"> </GridColumn> }
else if (col==2)
{ <GridColumn Field="@(nameof(Model.Two))" FieldType="@(typeof(string))" Title="Two Values"> </GridColumn> }
else if (col==3)
{ <GridColumn Field="@(nameof(Model.Three))" FieldType="@(typeof(string))" Title="Three Values"> </GridColumn> }
}
} </GridColumns> </TelerikGrid> <Button @onclick="ButtonClick1"> Order Columns: 3,2,1 </Button> <Button @onclick="ButtonClick2"> Order Columns: 2,3,1 </Button> <Button @onclick="ButtonClick3"> Order Columns: 1,2,3 </Button> </div> @code {
private List <Model> Data=new();
private int[] ColumnOrder=new[] { 1,2,3 };
private TelerikGrid <Model> _grid;

protected override void OnInitialized()
{
BuildData();
}

private void BuildData()
{
for (int i=0; i <10; i++)
{
Data.Add(new Model
{
One=$"One {i}",
Two=$"Two {i}",
Three=$"Three {i}",
});
}
}

private void ButtonClick1()
{
ColumnOrder=new[] { 3,2,1 };
_grid.Rebind();
StateHasChanged();
}

private void ButtonClick2()
{
ColumnOrder=new[] { 2, 3, 1 };
_grid.Rebind();
StateHasChanged();
}

private void ButtonClick3()
{
var state=_grid.GetState();
var i=0;
foreach (var col in state.ColumnStates)
{
if (col.Field=="One") col.Index=0;
if (col.Field=="Two") col.Index=1;
if (col.Field=="Three") col.Index=2;
}
//ColumnOrder=new[] { 1,2,3 };
StateHasChanged();
}

private void OnStateChanged(GridStateEventArgs <Model> obj)
{
Console.WriteLine("StateChanged");
}

public class Model
{
public string One { get; set; }
public string Two { get; set; }
public string Three { get; set; }
}
}

## Answer

**Marcin** answered on 17 May 2024

Well, I seem to have found a solution using the grid's SetStateAsync method. Here are the changes: <div style="width: 100%; height: 100%"> <TelerikGrid TItem="@Model" FilterMode="@GridFilterMode.FilterRow" SelectionMode="GridSelectionMode.Single" EnableLoaderContainer="true" Reorderable="true" Pageable="false" Sortable="true" Height="100%" OnStateChanged="OnStateChanged" Data="Data" @ref=@_grid> <GridColumns> @{
foreach (var col in ColumnOrder)
{
if (col==1)
{ <GridColumn Field="@(nameof(Model.One))" FieldType="@(typeof(string))" Title="One Values"> </GridColumn> }
else if (col==2)
{ <GridColumn Field="@(nameof(Model.Two))" FieldType="@(typeof(string))" Title="Two Values"> </GridColumn> }
else if (col==3)
{ <GridColumn Field="@(nameof(Model.Three))" FieldType="@(typeof(string))" Title="Three Values"> </GridColumn> }
}
} </GridColumns> </TelerikGrid> <Button @onclick="ButtonClick1"> Order Columns: 3,2,1 </Button> <Button @onclick="ButtonClick2"> Order Columns: 2,3,1 </Button> <Button @onclick="ButtonClick3"> Order Columns: 1,2,3 </Button> </div> @code {
private List <Model> Data=new();
private int[] ColumnOrder=new[] { 1,2,3 };
private TelerikGrid <Model> _grid;

protected override void OnInitialized()
{
BuildData();
}

private void BuildData()
{
for (int i=0; i <10; i++)
{
Data.Add(new Model
{
One=$"One {i}",
Two=$"Two {i}",
Three=$"Three {i}",
});
}
}

private async Task ButtonClick1()
{
var state=_grid.GetState();
var i=0;
foreach (var col in state.ColumnStates)
{
if (col.Field=="One") col.Index=2;
if (col.Field=="Two") col.Index=1;
if (col.Field=="Three") col.Index=0;
}
await _grid.SetStateAsync(state);
StateHasChanged();
}

private async Task ButtonClick2()
{
var state=_grid.GetState();
var i=0;
foreach (var col in state.ColumnStates)
{
if (col.Field=="One") col.Index=2;
if (col.Field=="Two") col.Index=0;
if (col.Field=="Three") col.Index=1;
}
await _grid.SetStateAsync(state);
StateHasChanged();
}

private async Task ButtonClick3()
{
var state=_grid.GetState();
var i=0;
foreach (var col in state.ColumnStates)
{
if (col.Field=="One") col.Index=0;
if (col.Field=="Two") col.Index=1;
if (col.Field=="Three") col.Index=2;
}
//ColumnOrder=new[] { 1, 2, 3 };
await _grid.SetStateAsync(state);
_grid.Rebind();

StateHasChanged();
}

private void OnStateChanged(GridStateEventArgs <Model> obj)
{
Console.WriteLine("StateChanged");
}

public class Model
{
public string One { get; set; }
public string Two { get; set; }
public string Three { get; set; }
}
}

### Response

**Hristian Stefanov** commented on 22 May 2024

Hi Marcin, I'm glad to see that you have quickly found the recommended approach for your scenario. Thank you for sharing your case here, publicly, so other developers with the same question can benefit from it. Kind Regards, Hristian
