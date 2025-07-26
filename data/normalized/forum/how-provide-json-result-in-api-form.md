# How provide json result in api form?

## Question

**Pet** asked on 14 Apr 2022

Hi, I have in a serverside Blazor page a grid, which can paging, filtering and sorting. In Kendo UI with Javascript the grid component provide a put request with filter, sort, page capabilities, i.e. { "sort": "Column1-desc", "page": "1", "pageSize": "10", "group": "", "filter": "Column2~eq~1~and~Column3~gt~10", } which return the data in json format. Instead of showing the page with the grid I want create an url which returns the json data. Possible as GET Request with Parameter: /api?sort=Column1-desc&page=1&pageSize=10&filter=Column2~eq~1~and~Column3~gt~10 But a PUT request with the paramter of Kendo UI is also possible. Do you have an idea or example, how I can extend my Blazor web app? Best regards, Peter

## Answer

**Dimo** answered on 14 Apr 2022

Hi Peter, You can bind the Grid via OnRead. This will allow you to get the DataSourceRequest object, serialize it, and send it to the server. Also check " Serialize the DataSoureRequest to the server " in the Examples section on the same page. Regards, Dimo Progress Telerik

### Response

**Peter** answered on 26 Apr 2022

Thank you, the project SampleWebApi from WebApiFromServerApp is the solution. Now I can get some data from Postman with POST [https://localhost:44326/WeatherForecast/actionresultsample](https://localhost:44326/WeatherForecast/actionresultsample) with Body as JSON i.e. {"Skip":0,"Page":1,"PageSize":10,"Sorts":[],"Filters":[{"LogicalOperator":0,"FilterDescriptors":[{"Member":"Date","Operator":5,"Value":"2022-04-05T00:00:00"}]}],"Groups":[],"Aggregates":[],"GroupPaging":false} This json is generated in the WebApiFromServerApp, WeatherForecastController.cs: content=JsonSerializer.Serialize(dsRequest) I can also omit the not needed properties from DataSourceRequest and keep only the filters: {"Filters":[{"LogicalOperator":0,"FilterDescriptors":[{"Member":"Date","Operator":5,"Value":"2022-04-05T00:00:00"}]}]} And insert a null check in WeatherForecastController.cs: if (request.Groups?.Count> 0) The integer values from the enums in Telerik.Datasource.dll are used, starting with 0: public enum FilterCompositionLogicalOperator
{
And,
Or
} public enum FilterOperator
{
IsLessThan,
IsLessThanOrEqualTo,
IsEqualTo,
IsNotEqualTo,
IsGreaterThanOrEqualTo,
IsGreaterThan,
StartsWith,
EndsWith,
Contains,
IsContainedIn,
DoesNotContain,
IsNull,
IsNotNull,
IsEmpty,
IsNotEmpty,
IsNullOrEmpty,
IsNotNullOrEmpty
} Regards, Peter

### Response

**Dimo** commented on 27 Apr 2022

Thanks for the follow-up and confirmation, Peter.
