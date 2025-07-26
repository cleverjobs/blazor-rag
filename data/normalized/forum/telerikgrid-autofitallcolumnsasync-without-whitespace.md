# TelerikGrid.AutoFitAllColumnsAsync without whitespace?

## Question

**Luk** asked on 21 Jul 2023

Hi, I am following the AutoFit Columns Guide that you have on your website. I have opted for the `OnGridRead` functionality as it doesn't require the extra JavaScript. I have noticed that in your approach the grid you have doesn't fill the whitespace on the right until after you click on the `AutoFit All Columns Manually` button and that when`OnAfterRenderAsync` occurs the grid will left align all of the contents. In my implementation this happens to me all of the time. I have added a button to manually call on the function as you have but it has no effect and leaves everything left aligned. The summary for the function states that it "Sets the minimum possible widths to all columns, so that there is no text wrappings" which holds up to what I am seeing, however is there other functions that can be applied (that I am unable to find) which will allow the columns to fill all the remain whitespace on the right or perhaps and overloaded version of `AutoFitAllColumnsAsync` that does this automatically?

### Response

**Kristian** commented on 04 Feb 2025

I know this is an old post, but on the off chance this helps someone, I came up with another solution that uses only CSS to ensure there is no whitespace when autofitting columns. I created a sample here.

## Answer

**Georgi** answered on 25 Jul 2023

Hi, Luke, By design, if the total width of the columns is less than the Grid width, white space will appear. One of the limitations of AutoFit Columns feature is that autofitting the columns on the initial load of the Grid is not supported. Take a look at the Grid column resizing article for more information. There is a viable workaround for this issue, but it requires a small amount of JavaScript. It is possible to leverage the grid's OnStateChanged event and adjust the width of the last column after a column resize. A JavaScript function can be used to calculate the width of the columns and conditionally adjust the width of the last one so it fills the whitespace. I have made a sample by modifying the OnGridRead example so you can see it in action. Let me know if there is anything else I could be of help with. Regards, Georgi Progress Telerik

### Response

**Luke** commented on 08 Aug 2023

Hi Georgi, Thanks for getting back to me and for the samples. I had seen them before but was hoping to avoid the extra JS requirement. The end result does create one column at the end that fills in the remaining white space which would help me out but is still a little off putting when looking at the overall spacing. I adapted your example below which seems to work well and I am posting for reference in the event anyone else comes across it and would like to use the approach. It essentially creates an even distribution of the available white space to all visible columns. It's not perfect and relies on the state.ColumnState[x].Width property to continue to use pixel(px) strings but for now it works well. Kind Regards, Luke @using Telerik.DataSource
@using Telerik.DataSource.Extensions
@inject IJSRuntime js
<TelerikButton OnClick="@AutoFit">AutoFit All Columns Manually</TelerikButton>

<TelerikGrid @ref="@Grid" OnRead="@OnGridRead" TItem="@Product" Pageable="true" Sortable="true" Resizable="true" FilterMode="GridFilterMode.FilterRow" OnStateChanged="@((GridStateEventArgs<Product> args)=> OnStateChangedHandler(args))">
<GridColumns>
<GridColumn Field="@nameof(Product.Name)" Title="Product Name" />
<GridColumn Field="@nameof(Product.Price)" />
<GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" />
<GridColumn Field="@nameof(Product.Active)" />
</GridColumns>
</TelerikGrid>

@code { private TelerikGrid<Product> Grid { get; set; } private List<Product> GridData { get; set; } private bool AutoFitFlag { get; set; } private bool FirstGridBindFlag { get; set; }=true; async void OnStateChangedHandler ( GridStateEventArgs<Product> args ) { bool hasWhiteSpace=await js.InvokeAsync<bool>( "hasWhiteSpace" ); if (hasWhiteSpace)
{ double whiteSpaceSize=await js.InvokeAsync<double>( "getWhiteSpace" ); var state=Grid.GetState(); int numberOfPopulatedColumns=state.ColumnStates.Where(colState=> ! string.IsNullOrWhiteSpace(colState.Width)).Count();
whiteSpaceSize=whiteSpaceSize / numberOfPopulatedColumns; foreach (GridColumnState colState in state.ColumnStates)
{ if (! string.IsNullOrWhiteSpace(colState.Width))
{
colState.Width=colState.Width.Replace( "px", "" );
colState.Width=$" {whiteSpaceSize + double.Parse(colState.Width)} px";
}
}
state.TableWidth=null; await Grid.SetStateAsync(state);
}
} private async Task AutoFit () {
Grid.AutoFitAllColumns();
} private async Task OnGridRead ( GridReadEventArgs args ) {
DataSourceResult result=GridData.ToDataSourceResult(args.Request);

args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults; if (FirstGridBindFlag)
{ // it is also possible to auto fit Grid columns on every rebind FirstGridBindFlag=false;
AutoFitFlag=true;
}
} protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (AutoFitFlag)
{
AutoFitFlag=false; await Task.Delay( 200 );
Grid.AutoFitAllColumns();
} await base.OnAfterRenderAsync(firstRender);
} protected override void OnInitialized () {
GridData=new List<Product>(); var rnd=new Random(); for ( int i=1; i <=70; i++)
{
GridData.Add( new Product()
{
Id=i,
Name="Product " + i.ToString(),
Price=( decimal )rnd.Next( 1, 100 ),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next( 60, 1000 )),
Active=i % 3==0 });
}
} public class Product { public int Id { get; set; } public string Name { get; set; } public decimal Price { get; set; } public DateTime ReleaseDate { get; set; } public bool Active { get; set; }
}
}
<script suppress-error="BL9992"> function hasWhiteSpace () { const grid=document.querySelector( ".k-grid" ); const gridTable=document.querySelector( ".k-grid-table" ); return grid.offsetWidth> gridTable.offsetWidth;
} function getWhiteSpace () { const grid=document.querySelector( ".k-grid" ); const gridTable=document.querySelector( ".k-grid-table" ); return grid.offsetWidth - gridTable.offsetWidth;
}
</script>
