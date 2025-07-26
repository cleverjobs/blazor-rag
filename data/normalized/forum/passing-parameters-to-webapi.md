# Passing Parameters to WebAPI

## Question

**Ale** asked on 31 Jul 2019

Hi there! My project is a fullstack Blazor application - server, client and shared projects. On my server project I have some custom logic for paging that I want to use in my Telerik Grid. My question is how am I supposed to use my server side paging instead of the built-in one in the TelerikGrid. The issue is that I want to send a request to the Server project(WebAPI) and pass some parameters to it(ex. page=2, limit=10). I get the parameters from the url(ex. "[http://localhost:5000/api/Forecasts?Page=2&Limit=10")](http://localhost:5000/api/Forecasts?Page=2&Limit=10")) so I can send different request for every single page(I have large data source). Is there a way I can integrate my server-side paging logic with your TelerikGrid for Blazor? Thank you in advance!

## Answer

**Marin Bratanov** answered on 31 Jul 2019

Hi Alek, You can do this by extracting the state of the grid in the OnRead event, so you can manage all operations yourself (including paging, filtering, sorting): [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) You can also see this in action in the following demo: [https://demos.telerik.com/blazor-ui/grid/manual-operations.](https://demos.telerik.com/blazor-ui/grid/manual-operations.) We have plans to make the DataSourceRequest object serializable so you could send it easily to the endpoint and use the code there to return the needed data only (or even to use the ToDataSourceResult() extension method from our DataSource package), and you can monitor the release notes to see when this becomes available, as it may make it easier for you to work with large data, especially if you use entities and LINQ on the backend. Regards, Marin Bratanov

### Response

**Alek** answered on 31 Jul 2019

Hi Marin, Thank you very much for your quick response! That is definitely going to work for my case. :)) Veli says hi to you! Have a great day! :))

### Response

**Marin Bratanov** answered on 31 Jul 2019

I'm glad to hear that, Alek. Good luck with implementing Blazor :) Say "Hi" back to Veli, I hope things are going well :) Regards, Marin Bratanov

### Response

**Alek** answered on 05 Aug 2019

Hello again Marin! I will be very happy to get some more assistance from you. So, I've started implementing that custom paging using Manual DataSource Operations. I'm having some issues with adding query params to the client side url(ex. [http://localhost:5000/test?page=2&pageSize=10).](http://localhost:5000/test?page=2&pageSize=10).) With the help of query params I want to go on a specific page like in the example - page 2 and limit the pageSize to 10 items per page. Do you think that such scenario is possible? I've tried implementing this logic, check the attached image below. I have a collection of 14 items, I do get items 11-20(which in my case are only 4 items), however the grid pager stays on page 1, and I cannot navigate through the other pages with it.

### Response

**Marin Bratanov** answered on 05 Aug 2019

Hi Alek, The grid will automatically populate the Request with the current page the user chose. You should use the value supplied by the grid when creating the URL parameters. The same applies for the page size - it is received as an argument based on the grid configuration. The UI of the grid controls the data requests, not the other way around. Regards, Marin Bratanov

### Response

**Alek** answered on 05 Aug 2019

[quote] Marin Bratanov said: Hi Alek, The grid will automatically populate the Request with the current page the user chose. You should use the value supplied by the grid when creating the URL parameters. The same applies for the page size - it is received as an argument based on the grid configuration. The UI of the grid controls the data requests, not the other way around. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 06 Aug 2019

Hi Alek, At the moment, this is possible only through the grid UI. Theoretically, you should also be able to bind the page index a bit like this, although it still requires UI interaction: @using Telerik.Blazor.Components.Grid @using Telerik.Blazor.Components.NumericTextBox <TelerikNumericTextBox @bind-Value="@startPage" Min="1"></TelerikNumericTextBox> <TelerikGrid Data="@MyData" Height="300px" Pageable="true" Sortable="true" Page="@startPage" FilterMode="Telerik.Blazor.FilterMode.FilterRow"> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(SampleData.Id))" /> <TelerikGridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" /> <TelerikGridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </TelerikGridColumns> </TelerikGrid> @code { int startPage { get; set; }=2; public IEnumerable<SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData { Id=x, Name="name " + x, HireDate=DateTime.Now.AddDays(-x) }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; } } } There seems, however, to be a problem with doing that while using the OnRead event and I am logging it for research. You can Follow it here (your vote's already in): [https://feedback.telerik.com/blazor/1424309-binding-the-page-index-does-not-work-when-using-onread.](https://feedback.telerik.com/blazor/1424309-binding-the-page-index-does-not-work-when-using-onread.) Regards, Marin Bratanov

### Response

**Alek** answered on 06 Aug 2019

Thank you for checking and reporting that Marin! I believe the URL should contain the page and pageSize parameters, so a URL for a specific page can be sent. Ex: I want to send you page 63/729 with the certain URL: [http://localhost:5000/test?page=63](http://localhost:5000/test?page=63) or [http://localhost:5000/test?page=63&pageSize=10.](http://localhost:5000/test?page=63&pageSize=10.)

### Response

**Marin Bratanov** answered on 06 Aug 2019

Hello Alek, The URL depends on the API and the service behind it. It will not control the grid, though, so its format depends entirely on its creators. Regards, Marin Bratanov

### Response

**Alek** answered on 07 Aug 2019

Ok, thanks again Marin! You've been very helpful I will keep following the Bug Report you logged.

### Response

**Dhruv** answered on 18 Sep 2019

If anyone still needs this since the DataSourceRequest is NOT serializable I have a solution for Filtering and Sorting. If you want to add grouping I left the code in the comments just needs to be implemented. I created a Helper class which contains all of the Kendo code to build a proper query string using System; using System.Collections; using System.Linq; using Telerik.Blazor.Common.Serialization; using Telerik.Blazor.Components.Grid; namespace Client.Helpers { public static class UrlHelpers { public static string JsonToQuery( this string jsonQuery) { string str="?"; str +=jsonQuery.Replace( ":", "=" ).Replace( "{", "" ). Replace( "}", "" ).Replace( ",", "&" ). Replace( "\"", "" ); return str; } public static string KendoToQueryString( this GridReadEventArgs args, IJavaScriptSerializer KendoJavaScriptSerializer) { /* * This Section of code should be deleted once Kendo supports serialization of the DataSourceRequest element. * [https://www.telerik.com/forums/passing-parameters-to-webapi](https://www.telerik.com/forums/passing-parameters-to-webapi) #NAaCW-6bXECTgpCR2YuScw * Link Above is an article mentioning it is in progress * Dhruvb@microsoft.com also has a support ticket open for this particular issue. This workaround should suffice for now */ string kendoFilters=null; for ( int i=0; i <args.Request.Filters.Count; i++) { var Member=args.Request.Filters[i].GetPropertyById( "Member" ); var Operator=args.Request.Filters[i].GetPropertyById( "Operator" ).ToLower(); var Value="'" + args.Request.Filters[i].GetPropertyById( "Value" ) + "'"; if (i==0) { kendoFilters +="(" + Member + "~" + Operator + "~" + Value; } if (i !=0) { kendoFilters +="~and~" + Member + "~" + Operator + "~" + Value; } if (i==args.Request.Filters.Count - 1) { kendoFilters +=")"; } } string kendoSorts=null; for ( int i=0; i <args.Request.Sorts.Count; i++) { var Member=args.Request.Sorts[i].GetPropertyById( "Member" ); var Direction=args.Request.Sorts[i].GetPropertyById( "SortDirection" ); var Operator=Direction.Equals( "Ascending" ) ? "asc": "desc"; if (i==0) { kendoSorts +=Member + "-" + Operator; } if (i !=0) { kendoSorts +="~" + Member + "-" + Operator; } } var customJson=new { Page=args.Request.Page, PageSize=args.Request.PageSize, Filter=string.IsNullOrEmpty(kendoFilters)==true? "": kendoFilters, Sort=string.IsNullOrEmpty(kendoSorts)==true? "": kendoSorts /* * If we ever need Grouping or Aggregates we will need to implement the code below */ //Groups=KendoJavaScriptSerializer.Serialize(args.Request.Groups), //Not Yet Implemented //Aggregates=KendoJavaScriptSerializer.Serialize(args.Request.Aggregates) //Not Yet Implemented }; var kendoDataSourceResultSerialized=KendoJavaScriptSerializer.Serialize(customJson); var kendoDataSourceResultToQueryString=kendoDataSourceResultSerialized.JsonToQuery(); return kendoDataSourceResultToQueryString; } } } Then you add this second class which I use for reflection throughout my application and in the code above. You could remove this but its really useful namespace Client.Helpers { public static class ReflectionHelper { public static string GetPropertyById<T>( this T item, string id) { return item.GetType().GetProperty(id).GetValue(item).ToString(); } } } Use this generic class to be used client side for DataSourceRequest return type namespace ViewModels.Kendo { public class DataSourceRequestViewModel<T> { public T[] Data { get; set; } public int Total { get; set; } public object Errors { get; set; } } } And Finally Implementation of the code public async Task ReadItems(GridReadEventArgs args) { var url=args.KendoToQueryString(KendoJavaScriptSerializer); gridData=_httpClient.GetJsonAsync<DataSourceRequestViewModel<MyGridDataReturnType>>(Url + args); StateHasChanged(); }

### Response

**Dhruv** answered on 18 Sep 2019

Just noticed I forgot dependency injection in the implementation class. You need the following code with "using Telerik.Blazor.Common.Serialization;" at the top of the file. [Inject] protected IJavaScriptSerializer KendoJavaScriptSerializer { get; set; }

### Response

**Marin Bratanov** answered on 19 Sep 2019

Thank you for sharing your solution with the community, Dhruv. As a small 'thank you', I updated your Telerik points. Regards, Marin Bratanov

### Response

**Niklas** answered on 10 Oct 2019

Hello! I want to push this thread again because i want build something similar, but i'm struggling to adapt the shown examples to my project. I'm currently building a generic grid which works with generic DTOs, consumed by Web APIs. Everything works currently, and now i want to achieve dynamic paging - my API now supports this. For each get request, i get a list of results, page size, page count, total row counts, ... I'm now struggling to wire the Blazor Grid to it. Right now, my grid loads the initial set of rows (page 1 with a default page size). I now need to give the grid the infos, how many pages exist and what the TotalCount is. If i set the ToalCount after the initial data load, i see (for a glimpse of a second) the pagination pages and total counts, but after that, the grid somehow "clears" this data, and only my first page (page 1, total count of those entries) is shown. My question: Do i need the OnRead function? Do i need the ToDataSourceResult extension? The example at [https://demos.telerik.com/blazor-ui/grid/manual-operations](https://demos.telerik.com/blazor-ui/grid/manual-operations) loads all items the first time - but, i want and support only specific page loads (if i navigate to page 2, the grid should trigger something where i can tell my API to get page 2) Greetings! Niklas

### Response

**Marin Bratanov** answered on 10 Oct 2019

Hello Niklas, You will need to use the OnRead event, extract the data from the .Request object and send it to the WebAPI endpoint you have. The total of the grid must be always the total number of records that the current data set will have (e.g., taking into account filtering), so the grid knows what to render in the pager. Then, the Data of the grid is the current page only. We have it on our radar to allow the DataSourceRequest object to be serializable, so you should, when that gets implemented, be able to send it with a simply PostJsonAsync() to the endpoint and extract all needed info there (or, use our DataSource package again, like in our MVC suites). You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1406084-expose-odata-string-from-the-grid-request-object.](https://feedback.telerik.com/blazor/1406084-expose-odata-string-from-the-grid-request-object.) Regards, Marin Bratanov

### Response

**Niklas** answered on 10 Oct 2019

Hey Marin! Perfect, works fine! :) Like always - thank you very much! Niklas

### Response

**Robert** answered on 23 Nov 2020

Will the DataSourceRequest object be properly serializable, so that you can send it as a parameter to the API? Alternatively, can you create a DataSourceRequest from the odata-string?

### Response

**Marin Bratanov** answered on 23 Nov 2020

Hello Robert, It is serializable, you can find a couple of examples here: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server) The grid in particular also has some extension methods to produce an OData string: [https://github.com/telerik/blazor-ui/tree/master/grid/odata.](https://github.com/telerik/blazor-ui/tree/master/grid/odata.) On the backend of things - if you sent an actual DataSourceRequest, your serializer of choice should be able to parse it. If not, read it as a string from the body of the query and deserialize it. As for OData - if the backend does not automatically produce a LINQ query or similar information for you based on the URL, you can parse the URL with your own code and fill in a new instance of a DataSourceRequest object. A basic example of creating one from scratch is available here: [https://docs.telerik.com/blazor-ui/common-features/telerik-datasource-package#examples](https://docs.telerik.com/blazor-ui/common-features/telerik-datasource-package#examples) Regards, Marin Bratanov
