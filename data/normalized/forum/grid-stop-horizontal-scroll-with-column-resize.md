# Grid stop horizontal scroll with column resize

## Question

**Emm** asked on 12 Sep 2024

Hi, I'm using a pretty basic grid with the Resize and Reorder parameters set to true. I can see there are functions around a Min and Max size for individual columns and auto sizing. I have read through this a few times and looked at the various resize demos [https://docs.telerik.com/blazor-ui/components/grid/columns/width.](https://docs.telerik.com/blazor-ui/components/grid/columns/width.) But it doesn't quite suit what I'm after. Ideally I'm looking for this type of functionality: When only some column widths are set and the cumulative width of columns with set widths is less than the available Grid width, the widths of the columns with a set width are respected and the remaining width is distributed evenly between the other columns. But the inverse so that if the cumulative width of columns is greater than the available width, it shrinks the remaining columns so that no horizontal scroll bar shows. Does anyone have any suggestions to how I might accomplish that with the grids inbuilt features? My alternative would be to calculate the size of the columns in the grids state changed event and then set the widths manually but its so far proved to be problematic with continues loops of the grids state changed event. Thanks

## Answer

**Dimo** answered on 13 Sep 2024

Hello Emmett, Perhaps I am missing something, because what you described as the wanted behavior is the default behavior: When only some column widths are set and the cumulative width of the columns with set widths is greater than the available Grid width, a horizontal scrollbar appears and all set column widths are respected. Columns with no set width are invisible as their width is 0. In other words, the Grid always expands or shrinks the columns without a width, so that there is no horizontal scrollbar, if possible. If you are after some more enhanced column width behavior, you can: Subscribe to the Grid OnStateChanged event. Check if the user modified the column state via args.PropertyName. Then check if or which column width changed, and make additional adjustment. Regards, Dimo Progress Telerik

### Response

**Emmett** commented on 16 Sep 2024

Hi Dimo, Thanks for the reply. My aim is to stop the horizontal scroll bar from appearing when a column is resized larger than the grid. To add a limitation so that the columns cannot be resized in such a way that they can expand beyond the width of the parent grid. The shrinking works as I need it to, its the restricting the width to the grid size im after. A few attempts at forcing the widths using the OnStateChanged has been less than perfect with continuous updates. Setting the column manually once displayed seems to trigger the state changed event again. Thanks Emmett

### Response

**Dimo** commented on 16 Sep 2024

Hello Emmett, I must confirm that it's not possible to prevent the user from triggering a horizontal Grid scrollbar when they expand a column during resizing. Sorry about that. In such scenarios, why not leave the user adjust the Grid UI the way they want?

### Response

**Emmett** commented on 16 Sep 2024

Hi, Unfortunately thats not an option given our requirements. The grid control is within a printable form in which the grid must then be confined within the printed page. So horizontal scrolls are not acceptable. We have alternative options with warnings and the like but that is far from ideal. Thanks Emmett

### Response

**Dimo** commented on 16 Sep 2024

In this case, I have two suggestions: Configure the Grid with optimal preset column widths, which correspond to the typical amount of data in each column. Then, disable column resizing altogether. Implement print-only CSS styles that shrink the columns to fit without a horizontal scrollbar. <p> Resize the Grid columns and then print. </p> <TelerikGrid Data="@GridData" Class="printable-grid" Groupable="true" Resizable="true"> <GridColumns> <GridCheckboxColumn Width="3.2em" /> <GridColumn Field="@nameof(SampleModel.Name)" /> <GridColumn Field="@nameof(SampleModel.GroupName)" /> <GridColumn Field="@nameof(SampleModel.Price)" /> <GridColumn Field="@nameof(SampleModel.Quantity)" /> <GridColumn Field="@nameof(SampleModel.StartDate)" /> <GridColumn Field="@nameof(SampleModel.IsActive)" /> </GridColumns> <DetailTemplate> Detail Template </DetailTemplate> </TelerikGrid> <style> @@media print {.printable-grid table { width: 100%!important;
}.printable-grid col:not (.k-hierarchy-col ):not (.k-group-col ):not (.k-drag-col ):not ( [style*="3.2em" ] ) { width: auto!important;
}
} </style> @code {
private List <SampleModel> GridData { get; set; }=new();

protected override void OnInitialized()
{
for (int i=1; i <=3; i++)
{
GridData.Add(new SampleModel()
{
Id=i,
Name=$"Name {i}",
GroupName=$"Group {i % 3 + 1}",
Price=Random.Shared.Next(1, 100) * 1.23m,
Quantity=Random.Shared.Next(0, 1000),
StartDate=DateTime.Now.AddDays(-Random.Shared.Next(60, 1000)),
IsActive=i % 4> 0
});
}
}

public class SampleModel
{
public int Id { get; set; }
public int? ParentId { get; set; }
public string Name { get; set; }=string.Empty;
public string GroupName { get; set; }=string.Empty;
public decimal Price { get; set; }
public int Quantity { get; set; }
public object Icon { get; set; }=SvgIcon.File;
public DateTime StartDate { get; set; }
public DateTime EndDate { get; set; }
public bool IsActive { get; set; }
}
}

### Response

**Emmett** commented on 17 Sep 2024

Hi Dimo, Thanks for the detailed alternatives, these might be good in some cases but still aren't fully acceptable for the requirement. Our printable form is configurable by the client, so the column width calculations need to be dynamic based on each clients individual needs beyond the scope of the main product. Each client data and view requirements will be completely different to the next and are centered around WIZIWIG so a dynamic approach is needed where they can specify their own columns sizes within their printable form. On top of that they are legal documents so the screen needs to match the print out. Its a complex juggling act with what our requirements are. However these solutions might be useful to others that come across the question. Your second option may be an acceptable alternative so ill mark the answer as complete however it still not the ideal scenario.
