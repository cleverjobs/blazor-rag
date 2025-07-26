# External filters

## Question

**qwqw** asked on 30 Jul 2019

Hi all, I have case where grid must have external filters and filtering occurs by manual button click. I am trying to use snippet from documentation ([https://docs.telerik.com/blazor-ui/components/grid/manual-operations).](https://docs.telerik.com/blazor-ui/components/grid/manual-operations).) 01. <TelerikTextBox @bind-Value="FilterName" /> 02. <TelerikTextBox @bind-Value="FilterEmail" /> 03. 04. <TelerikButton OnClick="Filter">Filter</TelerikButton> 05. 06. <TelerikGrid Data=@GridData TotalCount=@Total Sortable=true Pageable=true> 07. <TelerikGridColumns> 08. <TelerikGridColumn Field="@nameof(Model.Name)" /> 09. <TelerikGridColumn Field="@nameof(Model.Email)" /> 10. </TelerikGridColumns> 11. 12. <TelerikGridEvents> 13. <EventsManager OnRead=ReadData /> 14. </TelerikGridEvents> 15. </TelerikGrid> 16. 17. @code{ 18. public IQueryable<Model> SourceData { get; set; } 19. public IEnumerable<Model> GridData { get; set; } 20. public int Total { get; set; } 21. 22. public string FilterName { get; set; } 23. public string FilterEmail { get; set; } 24. 25. protected async Task ReadData(GridReadEventArgs args) 26. { 27. // Adding external filter values to grid data source request 28. args.Request.Filters.Clear(); 29. args.Request.Filters.Add( new FilterDescriptor(nameof(Model.Name), FilterOperator.Contains, FilterName)); 30. args.Request.Filters.Add( new FilterDescriptor(nameof(Model.Email), FilterOperator.Contains, FilterEmail)); 31. 32. var datasourceResult=await SourceData.ToDataSourceResultAsync(args.Request); 33. GridData=(datasourceResult.Data as IEnumerable<Model>).ToList(); 34. Total=datasourceResult.Total; 35. 36. StateHasChanged(); 37. } 38. 39. protected void Filter() 40. { 41. // How to say to grid data source that he must read the data? 42. } 43. 44. public class Model 45. { 46. public string Name { get; set; } 47. public string Email { get; set; } 48. } 49. } I have some queations: 1. First of all, how to manually trigger Read event? Like in Kendo UI, Datasource have method read() ([https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/methods/read)](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/methods/read)) In other words, in Filter() handler how to say to grid data source that he must read the data? 2. What is right way to apply external filters and manually filtering?

## Answer

**Marin Bratanov** answered on 31 Jul 2019

Hello, At the moment, there is no facility for this, and I suggest you use the built-in filters. I see in this example that the data is already fetched on the page, so the built-in filters should suffice without the OnRead event. We improved them a lot in the 1.4.0 release and we also have a new filtering mode - the filter menu in addition to the filter row. We are considering adding a method on the grid instance like .Refresh() that will cause it to re-read its data source, and we will see how/if that makes it in. We need to consider a lot of scenario and implications, and before that we need to add some more features to the grid. Perhaps we would also add things like .Filter(field, value) and .Sort(field, direction), but these also need to be considered first. Regards, Marin Bratanov

### Response

**qw** answered on 01 Aug 2019

Hi Marin, Unfortunately, I can't use the built-in filters. I have a requirement that filters must be custom and external. Actually SourceData not fetched on the page, it Entity Framework DbSet that supplied from data access layer and execute query to db on each data read. Currently I found workaround. 01. <TelerikTextBox @bind-Value="FilterName" /> 02. <TelerikTextBox @bind-Value="FilterEmail" /> 03. 04. <TelerikButton OnClick="Filter">Filter</TelerikButton> 05. 06. <TelerikGrid Data=@GridData TotalCount=@Total Sortable=true Pageable=true> 07. <TelerikGridColumns> 08. <TelerikGridColumn Field="@nameof(Model.Name)" /> 09. <TelerikGridColumn Field="@nameof(Model.Email)" /> 10. </TelerikGridColumns> 11. 12. <TelerikGridEvents> 13. <EventsManager OnRead=ReadData /> 14. </TelerikGridEvents> 15. </TelerikGrid> 16. 17. @code{ 18. private DataSourceRequest _dataSourceRequest; 19. 20. public IQueryable<Model> SourceData { get; set; } 21. public IEnumerable<Model> GridData { get; set; } 22. public int Total { get; set; } 23. 24. public string FilterName { get; set; } 25. public string FilterEmail { get; set; } 26. 27. protected Task ReadData(GridReadEventArgs args) 28. { 29. if (_dataSourceRequest==null ) 30. _dataSourceRequest=args.Request; 31. 32. return ReadData(); 33. } 34. 35. private async Task ReadData(IEnumerable<IFilterDescriptor> filters=null ) 36. { 37. if (_dataSourceRequest==null ) return; 38. 39. if (filters !=null ) 40. { 41. _dataSourceRequest.Filters.Clear(); 42. _dataSourceRequest.Filters.AddRange(filters); 43. } 44. 45. var datasourceResult=await SourceData.ToDataSourceResultAsync(_dataSourceRequest); 46. GridData=(datasourceResult.Data as IEnumerable<Model>).ToList(); 47. Total=datasourceResult.Total; 48. 49. StateHasChanged(); 50. } 51. 52. protected Task Filter() 53. { 54. var filters=new List<IFilterDescriptor>(); 55. if (! string.IsNullOrWhiteSpace(FilterName)) 56. filters.Add( new FilterDescriptor(nameof(Model.Name), FilterOperator.Contains, FilterName)); 57. 58. if (! string.IsNullOrWhiteSpace(FilterEmail)) 59. filters.Add( new FilterDescriptor(nameof(Model.Email), FilterOperator.Contains, FilterEmail)); 60. 61. return ReadData(filters); 62. } 63. 64. public class Model 65. { 66. public string Name { get; set; } 67. public string Email { get; set; } 68. } 69. }

### Response

**Marin Bratanov** answered on 01 Aug 2019

That looks like it may work. I would also suggest you Follow this item, as we will probably add a method like .Refresh() so you can read your data anew when needed (which should be exactly what you need right now, and would let you do everything in OnRead). We will also handle the CollectionChanged event from the INotifyCollectionChanged Interface in case you use such a collection (which, I don't think will be your case). Regards, Marin Bratanov

### Response

**Phillip** commented on 23 Nov 2022

Has this Refresh() method been added to the Grid? I am looking for a similar function to be able to trigger the OnRead event from outside the grid.

### Response

**Svetoslav Dimitrov** commented on 25 Nov 2022

Hello Phillip, I am happy to report that this method is indeed available, but its name is Rebind(). If you have declared the OnRead event in your application, calling the Rebind method will execute the logic in the OnRead event handler.

### Response

**Flavio** answered on 17 Jul 2025

You can do it by using 2 telerik grid methods: 1. Grid Set State method var gridState=this.GridRef.GetState();
gridState.FilterDescriptors.Add( new Telerik.DataSource.FilterDescriptor
{
Member=nameof (TrackMeasurement.CreatedDate),
Operator=Telerik.DataSource.FilterOperator.IsLessThanOrEqualTo,
Value=this.searchForm.CreatedDateTo,
}); await this.GridRef.SetStateAsync(gridState); # This will trigger ReadItems 2. Grid ReadItems In here, read the the filters from GridReadEventArgs and build your custom server request logic. Example: protected async Task ReadItems ( GridReadEventArgs args ) { foreach ( var item in args.Request.Filters)
{ if (item is CompositeFilterDescriptor)
{
CompositeFilterDescriptor currFilter=item as CompositeFilterDescriptor; foreach (FilterDescriptor nestedFilter in currFilter.FilterDescriptors)
{
AddFilter(request, nestedFilter);
}
} else if (item is FilterDescriptor)

{
FilterDescriptor currFilter=item as FilterDescriptor;
AddFilter(request, currFilter);
}
} foreach (SortDescriptor item in args.Request.Sorts)
{
request.SortExpressions.Add( new SortExpression
{
PropertyName=item.Member,
SortDirection=item.SortDirection==ListSortDirection.Ascending ?
VantageFramework.Enum.DirectionType.ASC
: VantageFramework.Enum.DirectionType.DESC,
});
}
}
