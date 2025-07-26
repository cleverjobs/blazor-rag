# Programmatically set/reset columns to original definitions?

## Question

**Joh** asked on 13 Oct 2021

Hi, I'm implementing "Reset to Default" functionality that needs to reset any moved/resized columns to the original blazor code. I create my columns/grid using <TelerikGrid @ref="TelerikGridInstance" Data="@GridItems" TotalCount="@GridItems.Count" @bind-SelectedItems="@SelectedItems" Reorderable="@Resetting" PageSize="30" Height="@Height" RowHeight="28" Resizable="true" OnStateChanged="OnStateChangedHandler" SelectionMode="GridSelectionMode.Multiple" OnRowDoubleClick="OnRowDoubleClick" OnRowClick="OnRowClick" ScrollMode="@(VirtualMode ? GridScrollMode.Virtual : GridScrollMode.Scrollable)" OnRowContextMenu="OnRowContextMenu"> <GridColumns> @foreach (var c in Columns)
{
if(ColumnVisible(c)==false){
continue;
} <GridColumn Width="@width" Title="@c.Label"> <HeaderTemplate>.... </HeaderTemplate> </GridColumn> <Template>.... </Template> } </GridColumns> </TelerikGrid> I tried temporarily settings columns to nothing and then rerendering, but they get restored in the previous state. I could go down the path of destroying the component completely and then having to recreate everything but thats a pretty expensive task and my hope is there is a better way to do this. Or a way to set the column order/widths in code? Since I do know the original order/widths TIA

## Answer

**Hristian Stefanov** answered on 15 Oct 2021

Hi John, You can achieve the desired functionality by creating a new empty state in the ResetDefault method and set it to the Grid. I have prepared for you an example of the approach with basic configuration: <TelerikButton OnClick="@ResetDefault" Primary="true"> Reset Default! </TelerikButton> <br /> <br /> <TelerikGrid @ref="@GridRef" Pageable="true" Data="@MyData" Sortable="true" FilterMode="@GridFilterMode.FilterRow" AutoGenerateColumns="true"> </TelerikGrid> @code { TelerikGrid <SampleData> GridRef;

public void ResetDefault()
{
var state=new GridState <SampleData> (); //Creating a new empty state GridRef.SetState(state); //Setting the state to the Grid }

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData
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
} } You can extend the above example in the actual project to cover your application needs. Regards, Hristian Stefanov
