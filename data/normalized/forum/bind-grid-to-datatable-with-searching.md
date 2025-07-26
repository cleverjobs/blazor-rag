# Bind Grid to Datatable with searching

## Question

**Eri** asked on 18 Apr 2023

I have followed the example here to bind the grid to a data table: Bind to DataTable (telerik.com) Everything seems to work fine, but the searching functionality. Is there something special I have to make that work? <TelerikGrid Data=@GridData.AsEnumerable() TItem="DataRow" Pageable="true" Sortable="true" Resizable="true" FilterMode="@GridFilterMode.None" @bind-PageSize="@PageSize">
<GridSettings>
<GridPagerSettings InputType="PagerInputType.Input" PageSizes="@AppSettings.PageSizes" ButtonCount="5" Adaptive="true">
</GridPagerSettings>
</GridSettings>
<GridExport>
<GridExcelExport AllPages="@true" />
</GridExport>
<GridToolBarTemplate>
<GridCommandButton Command="custom" Icon="@FontIcon.MaxWidth" Size="sm" OnClick="@AutoFitAllColumns">Auto-fit</GridCommandButton>
<span class="k-toolbar-spacer"></span>
<GridCommandButton Command="ExcelExport" Icon="@FontIcon.FileExcel" Size="sm">To Excel</GridCommandButton>
<span title="Searches the items in the below grid." class="tooltip">
<GridSearchBox DebounceDelay="200" Placeholder="Search" Size="sm"></GridSearchBox>
</span>
</GridToolBarTemplate>
<GridColumns>
@foreach (DataColumn col in GridData.Columns)
{
<GridColumn Field="@col.ColumnName" Title="@col.ColumnName">
<Template>
@((context as DataRow).ItemArray[col.Ordinal].ToString())
</Template>
</GridColumn>
}
<GridColumn Field="@nameof(RawDataVm.SearchString)" Title="" Width="1%" ShowFilterCellButtons="false" OnCellRender="@((e)=> e.Class=" merge-border ")">
<Template>
@( "" )
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid> Also, the private TelerikGrid<DataRow> Grid { get; set; }=null!; declaration seems to be null, should it be a different object type?

### Response

**Yanislav** commented on 21 Apr 2023

Hello Eric, Search functionality Generally speaking, the search function in the Grid works similarly to the filter function. You shared a feedback item from the public portal, which mentions that the code snippet throws errors when performing data operations like filtering. However, that code snippet was a temporary proposal for binding the Grid to a DataTable. Instead, we recommend following the approach shown in our official demo ` Grid - Data Table `. You can see the implementation by checking the "View Source" tab. To demonstrate how the search functionality works when the Grid is properly bound to a DataTable, I've prepared a REPL example. I hope this is helpful to you. TelerikGrid reference To obtain a reference to a TelerikGrid, you need to indicate which property is associated with the component. To do this you have to use the @ref directive. <TelerikGrid @ref="Grid"...

TelerikGrid<T> Grid { get; set;}

### Response

**George** commented on 14 Aug 2023

In the example, there is an extention method on the data table, DataTable.ToDataSourceResult(args.Request); what namespace or library is used to bring that into the class file?

### Response

**Yanislav** commented on 16 Aug 2023

Hello George, The ToDataSourceResult method is part of the Telerik.DataSource.Extensions namespace. In general, the namespace comes from a package called Telerik.DataSource. However, the package is a dependency of Telerik.UI.for.Blazor. That being said, if the Telerik UI for Blazor package is installed in the project, you can access the ToDataSourceResult method by including the following ' using ' statement: using Telerik.DataSource.Extensions; I hope this helps.
