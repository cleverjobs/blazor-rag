# Programmatically create Grid / Columns?

## Question

**Jon** asked on 28 Mar 2020

Hi I want to bind a grid to a source source. But the data source varies each time. 1. Can you automatically generate the columns when binding? 2. Can you programatically create a grid ? thx in advance

## Answer

**Marin Bratanov** answered on 28 Mar 2020

Hello Jonathan, The feature that would let the grid generate columns based on the data source is this one, so you can click the Follow button to get status updates for it: [https://feedback.telerik.com/blazor/1418456-bind-to-datatable.](https://feedback.telerik.com/blazor/1418456-bind-to-datatable.) I have added your Vote for it to raise its priority. For the time being, I'd suggest you implement a column chooser or at least the loop over the column descriptor from this feature request: [https://feedback.telerik.com/blazor/1450105-column-chooser.](https://feedback.telerik.com/blazor/1450105-column-chooser.) Perhaps you could create descriptors and populate their collection based off your data, maybe through reflection. On programmatic creation - the component model in Blazor is not designed for this. The way to add components conditionally is to use razor syntax in your views - if-blocks, foreach loops and so on to declare the grid instances as needed so they render based on your conditions and data. This applies to our grid and to any other components. There are ways to hack through that by creating a RenderFragment yourself, but I personally find that extremely cumbersome and unmaintainable. Regards, Marin Bratanov

### Response

**Jonathan** answered on 29 Mar 2020

thx..! I was also able to use an ExpandoObject - populate with that from whatever is returned from a query <TelerikGrid Data="@expandoList" Pageable="true" Resizable="true" Reorderable="true" Groupable="false"> <GridColumns> @foreach (ExpandoObject exo in expandoList) { @foreach (var property in (IDictionary<String, Object>)exo) { Console.WriteLine(property.Key + ": " + property.Value); <GridColumn Field="@property.Value.ToString()" Title="@property.Key"> <Template> @{ string toRender=""; toRender=property.Value.ToString(); @toRender } </Template> </GridColumn> } } </GridColumns>

### Response

**Marin Bratanov** answered on 30 Mar 2020

Hi Jonathan, You may also want to Follow this enhancement (I added your Vote on your behalf): [https://feedback.telerik.com/blazor/1429858-please-add-support-for-binding-grids-to-dynamic-expandoobject.](https://feedback.telerik.com/blazor/1429858-please-add-support-for-binding-grids-to-dynamic-expandoobject.) Regards, Marin Bratanov

### Response

**Jitendra** answered on 08 Jul 2022

Hello I am trying to generate Dynamic columns for Telerik Grid it is generating multiple times columns set I want to avoid this please check bellow screen short. Here is the my code. <TelerikGrid Data="@SearchConfigs" Resizable="true" Reorderable="true" Groupable="false"> <GridColumns> @foreach (SearchConfig row in SearchConfigs)
{
@foreach (var property in (IDictionary<string, string>)row.SearchFields)
{ <GridColumn Title="@property.Key"> <Template> @property.Value </Template> </GridColumn> }
} </GridColumns> </TelerikGrid> public List <SearchConfig> SearchConfigs { get; set; }=new List<SearchConfig>();

IDictionary<string, string> keyValuePairs=new Dictionary<string, string>
{
{ "Col1", "Value1" },
{ "Col2", "Value2" },
{ "Col3", "Value3" },
{ "Col4", "Value4" },
{ "Col5", "Value5" },
{ "Col6", "Value6" },
{ "Col7", "Value7" },
{ "Col8", "Value8" },
};

SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs });
SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs });
SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs }); Could you please help me figure out what is going wrong here? Thank you
