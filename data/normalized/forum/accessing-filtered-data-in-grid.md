# Accessing Filtered Data in Grid

## Question

**Cam** asked on 17 Jul 2020

Is there currently a way to access filtered data from the grid? I want users to be able to filter data in the grid and then display it in a chart. The only way I can see to do it is by rolling my own filtering code with the OnRead event.

## Answer

**Marin Bratanov** answered on 17 Jul 2020

Hi Cameron, Indeed, that's the most straightforward way. An alternative is to get the current grid state (see the GridRef.GetState() method), and create a new DataSourceRequest object with the current filters, then use the .ToDataSourceResult() extension method of ours with that request - this would let you perform the same operation on the data as the grid does internally so you can fetch the same data. Ultimately, it's almost the same as using the OnRead event. If you already have all the data in the view model, the .ToDataSourceResult() method can let you do that filtering for the grid too, pretty easily. Regards, Marin Bratanov

### Response

**laboratorysystemdevelopment** answered on 07 Aug 2020

[quote] Marin Bratanov said: Hi Cameron, Indeed, that's the most straightforward way. An alternative is to get the current grid state (see the GridRef.GetState() method), and create a new DataSourceRequest object with the current filters, then use the .ToDataSourceResult() extension method of ours with that request - this would let you perform the same operation on the data as the grid does internally so you can fetch the same data. Ultimately, it's almost the same as using the OnRead event. If you already have all the data in the view model, the .ToDataSourceResult() method can let you do that filtering for the grid too, pretty easily. Regards, Marin Bratanov

### Response

**Cameron** answered on 07 Aug 2020

Following Marin's suggestions I was able accomplish my goal. Thanks Marin btw! Here is a snipped of my code: public List<ExpandoObject> GetFilteredData() { if (Data==null || !Data.Any()) { // Return empty list if no data is available return new List<ExpandoObject>(); } // Apply filters from grid var req=new DataSourceRequest(); var gridData=Grid.GetState(); var FilteredData=new List<ExpandoObject>(); req.Filters=new List<IFilterDescriptor>(); req.Filters.AddRange(gridData.FilterDescriptors); FilteredData.AddRange((IEnumerable<ExpandoObject>)Data.ToDataSourceResult(req).Data); return FilteredData; }

### Response

**Marin Bratanov** answered on 08 Aug 2020

Thank you for sharing, Cameron! Regards, Marin Bratanov

### Response

**laboratorysystemdevelopment** answered on 10 Aug 2020

[quote] Cameron said: Following Marin's suggestions I was able accomplish my goal. Thanks Marin btw! Here is a snipped of my code: public List<ExpandoObject> GetFilteredData() { if (Data==null || !Data.Any()) { // Return empty list if no data is available return new List<ExpandoObject>(); } // Apply filters from grid var req=new DataSourceRequest(); var gridData=Grid.GetState(); var FilteredData=new List<ExpandoObject>(); req.Filters=new List<IFilterDescriptor>(); req.Filters.AddRange(gridData.FilterDescriptors); FilteredData.AddRange((IEnumerable<ExpandoObject>)Data.ToDataSourceResult(req).Data); return FilteredData; } [/quote] Thanks! It worked!

### Response

**Greg** answered on 11 May 2022

I simplified this code and turned it into a generic extension method because its something I need often. ie: for selecting all rows matching the current filters. Works very easily this way. public static List <T> FilteredData <T>( this TelerikGrid<T> grid ) { var req=new DataSourceRequest { Filters=new List<IFilterDescriptor>(grid.GetState().FilterDescriptors) }; var filteredData=new List<T>((IEnumerable<T>)grid.Data.ToDataSourceResult(req).Data); return filteredData;
}

### Response

**Jonathan** answered on 11 Nov 2024

Here is my implementation in Blazor Server: private void OnGridStateChanged(GridStateEventArgs <OMSGrossMargin> args)
{
if (args.PropertyName=="FilterDescriptors")
{
var req=new DataSourceRequest
{
Filters=GridRef.GetState().FilterDescriptors.ToList()
};

GrossMarginTotal=((IEnumerable <OMSGrossMargin> )OMSGrossMarginList
.ToDataSourceResult(req).Data)
.Sum(x=> x.GMPPRO);

StateHasChanged();
}
}
