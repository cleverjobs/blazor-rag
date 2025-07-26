# Drag & Drop between grids doesn't work when one Grid Starts out Empty

## Question

**BobBob** asked on 11 Oct 2021

I am not able to drag and drop between grids when one of the grids starts out with an empty list of data. I have used your code from the example and altered it to make one grid empty to start out with. When I try to drag a new item into that grid I just get the "not allowed" tooltip and nothing will drop. @page "/DragDropTest"
@layout AuthorizedMainLayout

@* Drag a row from one Grid and Drop it in the other *@<TelerikGrid Data="@MyData" Height="400px" Pageable="true" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true" @ref="@FirstGrid" RowDraggable="true" OnRowDrop="@((GridRowDropEventArgs<SampleData> args)=> OnRowDropHandler(args))"> <GridSettings> <GridRowDraggableSettings DragClueField="@nameof(SampleData.Name)"> </GridRowDraggableSettings> </GridSettings> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> <TelerikGrid Data="@MySecondGridData" Height="400px" Pageable="true" Resizable="true" Reorderable="true" RowDraggable="true" OnRowDrop="@((GridRowDropEventArgs<SampleData> args)=> OnSecondGridRowDropHandler(args))"> <GridSettings> <GridRowDraggableSettings DragClueField="@nameof(SampleData.Name)"> </GridRowDraggableSettings> </GridSettings> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> @code {
TelerikGrid <SampleData> FirstGrid { get; set; }

private void OnRowDropHandler(GridRowDropEventArgs <SampleData> args)
{
//The data manipulations in this example are to showcase a basic scenario.
//In your application you should implement them as per the needs of the project.

MyData.Remove(args.Item);
InsertItem(args);
}

private void OnSecondGridRowDropHandler(GridRowDropEventArgs <SampleData> args)
{
//The data manipulations in this example are to showcase a basic scenario.
//In your application you should implement them as per the needs of the project.

MySecondGridData.Remove(args.Item);
InsertItem(args);
}

private void InsertItem(GridRowDropEventArgs <SampleData> args)
{
var destinationData=args.DestinationGrid==FirstGrid ? MyData : MySecondGridData;

var destinationIndex=0;

if (args.DestinationItem !=null)
{
destinationIndex=destinationData.IndexOf(args.DestinationItem);
if (args.DropPosition==GridRowDropPosition.After)
{
destinationIndex +=1;
}
}

destinationData.InsertRange(destinationIndex, args.Items);
}

public List <SampleData> MySecondGridData=Enumerable.Range(1, 30).Select(x=> new SampleData
{
Id=x + 2,
Name="name " + x + 2,
Team="team " + x % 3,
HireDate=DateTime.Now.AddDays(-x * 2).Date
}).ToList();

public List <SampleData> MyData=new(); // Enumerable.Range(1, 30).Select(x=> new SampleData
//{
// Id=x,
// Name="name " + x,
// Team="team " + x % 5,
// HireDate=DateTime.Now.AddDays(-x).Date
//}).ToList();

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public DateTime HireDate { get; set; }
}
}

### Response

**Matthias** commented on 13 Oct 2021

Have you already found a solution? I needed this in my application as well. But had no problems with it. Try to place the element at the top. (If not, I'll check tomorrow!) Regards Matthias

### Response

**Bob** commented on 13 Oct 2021

I am not sure what you mean by "Try to place the element at the top" When I drag the element to the empty grid no matter where I try to place it is get the circle with the line through it and I can not drop it.

## Answer

**Matthias** answered on 14 Oct 2021

Hello Bob, attached is a small video showing the process. The source code shows only the necessary functions. Checks and errorhandling are not implemented. This should allow you to insert an item in an empty list without any problems. Best regards Matthias <TelerikGrid @ref="@DragGridLeft" Data="@LeftCustomers" Pageable="false" ScrollMode="GridScrollMode.Scrollable" PageSize="20" Sortable="true" Groupable="false" Resizable="true" ShowColumnMenu="true" Class="posViewDrag-Grid" Height="500px" FilterMode="@GridFilterMode.None" RowDraggable="true" OnRowDrop="@((GridRowDropEventArgs<Adress> args)=> OnDropOneLeft(args))"> <GridSettings> <GridRowDraggableSettings DragClueField="@nameof(Adress.AdressName)" /> <GridColumns> <GridColumn Field="@nameof(Adress.AdressName)" Title="Customer" Width="60px" ShowColumnMenu="false" /> </GridColumns> </GridSettings> </TelerikGrid> <TelerikGrid @ref="@DragGridRight" Data="@RightCustomers" Pageable="false" ScrollMode="GridScrollMode.Scrollable" PageSize="20" Sortable="true" Groupable="false" Resizable="true" ShowColumnMenu="true" Class="posViewDrag-Grid" Height="500px" FilterMode="@GridFilterMode.None" RowDraggable="true" OnRowDrop="@((GridRowDropEventArgs<Adress> args)=> OnDropOneRight(args))"> <GridSettings> <GridRowDraggableSettings DragClueField="@nameof(Adress.AdressName)" /> <GridColumns> <GridColumn Field="@nameof(Adress.AdressName)" Title="Customer" ShowColumnMenu="false" /> </GridColumns> </GridSettings> </TelerikGrid> code: @code { public TelerikGrid<Adress> DragGridLeft { get; set; } public TelerikGrid<Adress> DragGridRight { get; set; } public ObservableCollection <Adress> LeftCustomers { get; set; }=new ObservableCollection<Adress>(); public ObservableCollection <Adress> RightCustomers { get; set; }=new ObservableCollection<Adress>(); protected override void OnInitialized ( ) {
LeftCustomers.Add( new Adress() {ID=1, AdressName="Tom Miller" });
LeftCustomers.Add( new Adress() {ID=2, AdressName="Mira Schneider" });
LeftCustomers.Add( new Adress() {ID=3, AdressName="Helgard Schmitz" });
LeftCustomers.Add( new Adress() {ID=4, AdressName="Marius Klein" });
LeftCustomers.Add( new Adress() {ID=5, AdressName="Sara Brown" });
} public class Adress { public int ID { get; set; } public string AdressName { get; set; }
} private void OnDropOneLeft ( GridRowDropEventArgs<Adress> args ) {
InsertItem(args);
} private void OnDropOneRight ( GridRowDropEventArgs<Adress> args ) {
InsertItem(args);
} void InsertItem ( GridRowDropEventArgs<Adress> args ) { var adress=args.Items.FirstOrDefault(); if (args.DestinationGrid==DragGridLeft)
{
LeftCustomers.Add(adress);
RightCustomers.Remove(adress);
} else {
RightCustomers.Add(adress);
LeftCustomers.Remove(adress);
}

}

}

### Response

**Bob** commented on 14 Oct 2021

Okay, I found the problem. The ONLY place you can drop a new item is exactly over the "No Data" line. I had css that put my No Data line in the center of the grid. Thus, I had to drag my new item directly over the center of the grid in order to drop it. Since this would not be obvious to our users, I had to put the No Data Line (in my case a templated image) at the top of the the grid so that they can drop it.

### Response

**Dimo** commented on 14 Oct 2021

Hi Bob, Row drag & drop relies on a DestinationItem in the destination table, that's why it expects the user to drop over/above/below a specific row. In your case, you can do one of the following: remove the destination Grid height use a NoDataTemplate that is high enough to fill the empty Grid data area . posViewDrag-Grid.k-grid-norecords { height: 250px;
} I will update the documentation to clarify the situation. I am sorry if you have invested time in this issue.
