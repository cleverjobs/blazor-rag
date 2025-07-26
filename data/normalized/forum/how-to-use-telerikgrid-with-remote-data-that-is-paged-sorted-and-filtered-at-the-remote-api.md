# How to use TelerikGrid with Remote data that is paged, sorted and filtered at the remote API

## Question

**dca** asked on 11 Feb 2020

We are building a new server-side Blazor web site that gets its data from our existing ASP.NET Core 3.1 web API hosted in Azure. The API accepts PageSize, PageNumber and a dictionary of field names and values to be used for filtering and sorting, and returns the specified page of records that are filtered, and sorted against the full database table data. We would prefer to use a commercial Blazor grid component that displays FilterRow UI elements and use the user input values and FilterRow element assigned field names to pass the field names and filter values to our API for filtering. We also want to capture the Sort (column header click actions) to pass the sort filed name and direction to the API and finally, we want to capture the component's pager values for current PageNumber and PageSize to pass to our API. That way, our API can filter, sort and page the full data in the database and just return the result set to be displayed. We have a working version of the TelerikGrid v2.5.1 athat handles the paging the way we want, since you supply the GridReadEventArgs in the OnRead event that include the PageNumber and PageSize, but the sort and filter elements appear to be bound to the current data and so far, we have not been able to find a way to pull the filter and sort expression out to pass on to our API in a way that actually works. Is what we want to do at all possible with your 2.5.1 build of TelerikGrid for Blazor?

## Answer

**Marin Bratanov** answered on 12 Feb 2020

Hi, To begin with the simplest scenario - if your endpoint is oData compatible, you can have this with very little code: [https://github.com/telerik/blazor-ui/tree/master/grid/odata](https://github.com/telerik/blazor-ui/tree/master/grid/odata) We are also working on making the DataSourceRequest serializable so you can use our ToDataSourceResult extension method on a server - so you wouldn't have to extract the grid state yourself, but instead just send it over the wire in a fashion similar to the way our MVC grid works (see here for an example - something similar is the end goal). If you cannot use OData, you will have to use the DataSourceRequest object ( API ref ) and extract the required information - for example, by looping the Filters or Sorts collections. I added an example of this in the docs: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#extract-information-from-the-datasourcerequest-object-to-use-in-your-own-api](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#extract-information-from-the-datasourcerequest-object-to-use-in-your-own-api) Regards, Marin Bratanov

### Response

**dcadler** answered on 13 Feb 2020

Thanks for the quick reply Marin. I should be able to use the ToODataString extension method. Is there a way to turn off the OnRead until I click a Go button so it isn't sending data requests on each keystrokes?

### Response

**Marin Bratanov** answered on 14 Feb 2020

Hi, You can determine what to do in the OnRead handler according to your application logic - the even will fire, but you don't have to fetch data in it. Here's an example that offers some more details: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#cache-data-request.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#cache-data-request.) You may also find interesting this KB on reducing the number of requests: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-kb-throttle-operations](https://docs.telerik.com/blazor-ui/knowledge-base/grid-kb-throttle-operations) Regards, Marin Bratanov

### Response

**Alexander** answered on 04 Apr 2020

Hi, I continue waiting for the DataSourceRequest serialization solution for Blazor, which to me is the obvious implementation to have when we want to use the Blazor grid filters. Or at least, could we be provided with some extension method like: public DataSourceRequest ToDataSourceRequest(this string oDataString) Do you guys have an estimate on when will that be available?

### Response

**Marin Bratanov** answered on 06 Apr 2020

Hi Alexander, We are working on this task at the moment and you can Follow its progress here: [https://feedback.telerik.com/blazor/1456603-filter-server-side-serialize-datasourcerequest-from-a-wasm-app-to-remote-endpoint.](https://feedback.telerik.com/blazor/1456603-filter-server-side-serialize-datasourcerequest-from-a-wasm-app-to-remote-endpoint.) Regards, Marin Bratanov

### Response

**Ryan** answered on 23 Sep 2020

Hey Marin-- Are there settings on the 'Telerik Blazor Grid' to allow it to use OData v3 instead of v4? I have an older API--with OData v3 services--and the $count in the 'args' query is causing issues. Thanks for your help!

### Response

**Marin Bratanov** answered on 23 Sep 2020

Hi Ryan, We have a method that generates an oData v4 query. If you need older versions, you could either modify the v4 string we provide, or build your own by looping over the data in the DataSourceRequest object (see how to do that in the Get Information From the DataSourceRequest section of the docs). Regards, Marin Bratanov
