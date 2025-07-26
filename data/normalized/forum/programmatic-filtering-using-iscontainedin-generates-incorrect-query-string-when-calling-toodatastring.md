# Programmatic Filtering using "IsContainedIn" generates incorrect query string when calling ToODataString

## Question

**Tyl** asked on 02 Apr 2020

I am setting filters programmatically using the "FilterRow" example from here. Everything worked perfectly until I needed to implement a filter using FilterOperator.IsContainedIn. I have confirmed that calling GridReadEventArgs.Request.ToODataString() is rendering the query string incorrectly by placing single quotes around the FilterDescriptor Member. The below is a working example I created using the OData Blazor demo found on the Telerik GitHub here. I did have to update Blazor-UI to v2.9 for this demo to work. If you uncomment the line in ReadItems that removes the extra single quotes, you'll see that the page functions as it should. I've also included a couple of screenshots which have the requestUrl rendered in the browser to better visualize what I mean. @page "/" @inject HttpClient Http @using Telerik.Blazor.ExtensionMethods @using WasmApp.Shared @using Telerik.DataSource <TelerikGrid Data=@GridData Height="460px" RowHeight="60" PageSize="10" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterRow" OnRead=@ReadItems TotalCount=@Total OnStateInit="@((GridStateEventArgs<ODataProduct> args)=> OnStateInit(args))"> <GridColumns> <GridColumn Field="ProductID" /> <GridColumn Field="ProductName" /> <GridColumn Field="Discontinued" /> </GridColumns> </TelerikGrid> <h4>@appStatus</h4> @code{ public List<ODataProduct> GridData { get; set; }=new List<ODataProduct>(); public int Total { get; set; }=0; public string appStatus { get; set; } protected void OnStateInit(GridStateEventArgs<ODataProduct> args) { GridState<ODataProduct> gridState=new GridState<ODataProduct>() { FilterDescriptors=new List<FilterDescriptorBase>() { new FilterDescriptor() {Member="ProductName", Operator=FilterOperator.IsContainedIn, Value="Chai,Chang", MemberType=typeof(string)} } }; args.GridState=gridState; } protected async Task ReadItems(GridReadEventArgs args) { var baseUrl=" [https://demos.telerik.com/kendo-ui/service-v4/odata/Products?](https://demos.telerik.com/kendo-ui/service-v4/odata/Products?) "; var requestUrl=$"{baseUrl}{args.Request.ToODataString()}"; //requestUrl=requestUrl.Replace("%27ProductName%27", "ProductName"); appStatus=requestUrl; Console.WriteLine(appStatus); ODataResponseOrders response=await Http.GetJsonAsync<ODataResponseOrders>(requestUrl); GridData=response.Products; Total=response.Total; } }

## Answer

**Marin Bratanov** answered on 06 Apr 2020

Hi Tyler, The OData specs ( link ) list the following string filters which has "contains" but does not have "is contained in": 5.1.1.5 String and Collection Functions
5.1.1.5.1 concat
5.1.1.5.2 contains
5.1.1.5.3 endswith
5.1.1.5.4 indexof
5.1.1.5.5 length
5.1.1.5.6 startswith
5.1.1.5.7 substring Thus, my advice is to use only filter operators that can work with OData, and switch to using Operator=FilterOperator. Contains The "IsContainedIn" operator that we have is kind of the reverse - and is highly specific to local string - The left operand must be contained in the right one - so this is not suitable for filtering fields, but strings. That said, I am attaching the output I get when I use the valid operator - the grid is filtered as expected. Regards, Marin Bratanov

### Response

**Tyler** answered on 06 Apr 2020

Hi Marin, Thanks for the reply. I am familiar with the OData specs for string and collections. However, I may not have made clear my dilemma and just posted what I assumed was a bug. I am trying to filter on a list of strings separated by commas. That's why I used the string below for the Value parameter. Value="Chai,Chang" In my project, we have a field called "JobType" that consists of a string of two characters. We have a couple of pages that need to filter on multiple values for this field. My goal was to use one FilterDescriptor instead of needing 5 separate ones to accomplish the same thing. I had seen elsewhere on the Telerik forums (for other Telerik Projects) that this was possible and IsContainedIn seemed like the closest thing I could find. Is there a way to accomplish this? Below is the line in my project that is obviously not working: new FilterDescriptor() {Member="JobType", Operator=FilterOperator.IsContainedIn, Value="SA,SC,SD,GC,GD", MemberType=typeof(string) }, I ended up implementing DoesNotContain and just adding a Filter Descriptor for each value to omit instead of the ones to match: new FilterDescriptor() {Member="JobType", Operator=FilterOperator.DoesNotContain, Value="GP", MemberType=typeof(string)}, new FilterDescriptor() {Member="JobType", Operator=FilterOperator.DoesNotContain, Value="GS", MemberType=typeof(string)}, new FilterDescriptor() {Member="JobType", Operator=FilterOperator.DoesNotContain, Value="SO", MemberType=typeof(string)}, new FilterDescriptor() {Member="JobType", Operator=FilterOperator.DoesNotContain, Value="SR", MemberType=typeof(string)}, new FilterDescriptor() {Member="JobType", Operator=FilterOperator.DoesNotContain, Value="SS", MemberType=typeof(string)} Thanks, Tyler

### Response

**Marin Bratanov** answered on 06 Apr 2020

Hi Tyler, Such a "contains" operation would match and item that has a text similar to "some padding SA,SC,SD,GC,GD some more padding", so it is expected that it won't provide the desired result. At this point, the grid does not have a multi-value filter yet, though, and it cannot generate such queries. You can try to alter the OData string yourself and include the desired operator: [https://groups.google.com/forum/#!topic/odata-discussion/jKqXU4i6248.](https://groups.google.com/forum/#!topic/odata-discussion/jKqXU4i6248.) You could do it with a multiselect component from outside of the grid. You may also find useful the filter templates - once they become available you could put the external component inside the grid. I've added your vote for both features to raise their priority. Regards, Marin Bratanov

### Response

**Jstemper** commented on 08 Jun 2021

Has there been any changes in the answer to this question? I too have a need to use a containedin type of query. It did work in the previous grid library that was using (none telerik)

### Response

**Svetoslav Dimitrov** commented on 11 Jun 2021

Hello John, From what I can see in the OData documentation the containedIn filter query is no longer supported - [https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html#_Toc31360955.](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html#_Toc31360955.) We do support the latest version of the OData and hence the reason this operator is not there.
