# Sorted/filtered items

## Question

**Rob** asked on 28 Aug 2023

If sorting and/or filtering is applied to the grid, how do I access the resulting subset of items, i.e. the items currently displayed in the grid?

## Answer

**Georgi** answered on 30 Aug 2023

Hi, Robert, The OnStateChanged event of the grid is triggered when a data operation takes place - e.g. when filtering or sorting. Its arguments can be used to obtain the subset of filtered and sorted items. You can create DataSourceRequest - this is a class that describes the request for data (what page index, page size, filters, and sorts, groups, and aggregates are required by the client). Pass the request to the ToDataSourceMethod to get a DataSource that holds all the items and their total number. private async Task OnStateChangedHandler ( GridStateEventArgs<SampleData> args ) { await Task.Delay( 500 ); //simulate network delay from a real async call DataSourceRequest request=new DataSourceRequest
{
Page=1,
Filters=args.GridState.FilterDescriptors.ToList(),
Sorts=args.GridState.SortDescriptors.ToList()
}; var datasourceRestult=GridData.ToDataSourceResult(request);
RowsNumber=datasourceRestult.Total;
SubSet=(List<SampleData>)datasourceRestult.Data;
} I have prepared a REPL example you can take a look at. Let me know if additional questions arise. Regards, Georgi Progress Telerik
