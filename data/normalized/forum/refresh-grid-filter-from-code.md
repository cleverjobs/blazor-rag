# Refresh grid filter from code

## Question

**Cla** asked on 28 Jan 2025

I have a paged TelerikGrid loaded using OnRead event with 2 filter modes: Inline and programmately. With inline filter i manage a FilterCellTemplate and call FilterCellTemplateContext.FilterAsync() to refresh the grid after setting the filter value. If i set a filter programmately, to update the grid i call Grid.Rebind(), but i need to set the grid to page 1, so i need to set the Page property binding to 1 before calling Grid.Rebind. There is a better way to refresh the grid for filtering programmately? the best would be a method to call (as done with FilterCellTemplateContext.FilterAsync() ) who manage the page reset. Thanks

## Answer

**Tsvetomir** answered on 31 Jan 2025

Hi Claudio, To achieve programmatic filtering and reset the Grid to the first page efficiently, the approach you are currently using is indeed one of the best available options. However, you can use the following to achieve your goal: Set Filter Descriptors - Programmatically update the filter descriptors as needed. Reset the Page - Before rebinding, configure the Grid state by setting its page to 1. Rebind the Grid - Use the Grid.Rebind() method to refresh the grid data. Here's how you can implement this: @code {
TelerikGrid<MyDataType> gridRef;
GridState<MyDataType> gridState=new GridState<MyDataType>(); private void ApplyProgrammaticFilter ( ) { // Set your filter descriptors here gridState.FilterDescriptors=new List<FilterDescriptorBase>
{ new FilterDescriptor( "MyColumn", FilterOperator.Contains, "FilterValue" )
}; // Reset to the first page gridState.Page=1; // Apply the state and rebind the grid gridRef.SetState(gridState);
gridRef.Rebind();
}
} This method manages the grid state directly, including filters and pagination. By setting the Page property to " 1 ", you ensure that the grid starts from the first page after applying the filters. In addition, you can refer to our Grid - Refresh Data article to explore the other available options for refreshing the Grid. I hope the provided information serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik

### Response

**Claudio** answered on 31 Jan 2025

Thanks Tsvetomit, i made an extension method: public static async Task RebindAsync <T> (this Telerik.Blazor.Components.TelerikGrid <T> grid, bool resetToFirstPage=false)
{
if (!resetToFirstPage)
{
grid.Rebind();
return;
}

var gridState=grid.GetState();
gridState.Page=1;

await grid.SetStateAsync(gridState);
}
