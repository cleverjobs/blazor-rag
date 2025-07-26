# Mix server and client filtering in the grid

## Question

**Mar** asked on 12 Dec 2023

I have just for the first time tried server side paging and filtering using the ToDataSourceResultAsync extension. This works REALLY well. The only problem I have, is that I can't filter and sort on computed values in my view model as I can when all data manipulation is on the wasm client. Can I somehow mix server and client sorting? I would like to filter the current page on a field's not in the database. So not another roundtrip only the data on the client. UPDATE I am adding filters on the client. It works but the resulting sql uses AND, should be OR On the client: private async Task OnReadHandler ( GridReadEventArgs arg ) {
Query.GridRequest=arg.Request; var request=Query.GridRequest; var searchBoxFilter=request.Filters.SelectMemberDescriptors().Where(x=> x.Member=="ProductName" ).ToList(); if (searchBoxFilter.Any())
{ var clientFilter=new FilterDescriptor{Member="ClientName", Operator=FilterOperator.Contains, Value=searchBoxFilter.First().Value.ToString()};
request.Filters.Add(clientFilter); var initialsFilter=new FilterDescriptor{Member="UserInitials", Operator=FilterOperator.Contains, Value=searchBoxFilter.First().Value.ToString()};
request.Filters.Add(initialsFilter);
} var envelope=await TradeOverviewService.GetCertificateTradeRequestsForTradeOverView(Query);
arg.Data=envelope.CurrentPageData.ToList();
arg.Total=envelope.TotalItemCount;
} Part of the sql FROM "IBEX"."V_CERTIFICATE_TRADE_REQUEST" "v" WHERE (("v"."FLOW_TYPE" NOT IN ( 8, 10 )) AND (((( LOWER ("v"."PRODUCT_NAME_INTERNAL") LIKE '%sydbank%' ) AND ( LOWER ("v"."CLIENT_NAME") LIKE '%sydbank%' )) AND ( LOWER ("v"."USER_INITIALS") LIKE '%sydbank%' )))) ORDER BY "v"."TRADE_DATE" DESC OFFSET:p_0 ROWS FETCH NEXT :p_1 ROWS ONLY So can I create the filters so the resulting sql will be. FROM "IBEX"."V_CERTIFICATE_TRADE_REQUEST" "v" WHERE (("v"."FLOW_TYPE" NOT IN ( 8, 10 )) AND (((( LOWER ("v"."PRODUCT_NAME_INTERNAL") LIKE '%sydbank%' ) OR ( LOWER ("v"."CLIENT_NAME") LIKE '%sydbank%' )) OR ( LOWER ("v"."USER_INITIALS") LIKE '%sydbank%' )))) ORDER BY "v"."TRADE_DATE" DESC OFFSET:p_0 ROWS FETCH NEXT :p_1 ROWS ONLY

## Answer

**Dimo** answered on 15 Dec 2023

Hi Martin, By design, all filter descriptors at root level ( GridReadEventArgs.Request.Filters.Add(...) ) are combined with an AND logical operator. To configure OR filtering, you need to nest several descriptors in a single CompositeFilterDescriptor with an OR. In your case, the filter descriptor structure should look like this: CompositeFilterDescriptor LogicalOperator: OR FilterDescriptors: CompositeFilterDescriptor LogicalOperator: AND FilterDescriptors: FilterDescriptor FLOW_TYPE FilterDescriptor PRODUCT_NAME_INTERNAL FilterDescriptor CLIENT_NAME FIlterDescriptor USER_INITIALS Note that complex filter structures are usually not compatible with the Grid UI logic and the component is not able to display them to the user. This should not be a problem when you are changing the filters in OnRead, because this is a temporary change that the Grid is not aware of. However, if you need to make the filter structure visible to the user, you need our Filter component. @using Telerik.DataSource
@using Telerik.DataSource.Extensions

<p>Showing products that a company wants to get rid of. They are:</p> <ul> <li> ( No longer in production AND in stock ) OR </li> <li> Returned OR </li> <li> Damaged </li> </ul> <TelerikGrid OnRead="@OnGridRead" TItem="@Product" Pageable="true" Sortable="true"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.Stock)" /> <GridColumn Field="@nameof(Product.InProduction)" /> <GridColumn Field="@nameof(Product.Damaged)" /> <GridColumn Field="@nameof(Product.Returned)" /> </GridColumns> </TelerikGrid> @code {
private List<Product> GridData { get; set; }=new ();

private async Task OnGridRead ( GridReadEventArgs args ) { await Task.Delay( 1 );

args.Request.Filters.Add( new CompositeFilterDescriptor ( ) {
LogicalOperator=FilterCompositionLogicalOperator.Or,
FilterDescriptors=new FilterDescriptorCollection ( ) { new CompositeFilterDescriptor ( ) {
LogicalOperator=FilterCompositionLogicalOperator.And,
FilterDescriptors=new FilterDescriptorCollection ( ) { new FilterDescriptor ( ) {
Member=nameof(Product.InProduction),
MemberType=typeof (bool),
Operator=FilterOperator.IsEqualTo,
Value=false }, new FilterDescriptor ( ) {
Member=nameof(Product.Stock),
MemberType=typeof (int),
Operator=FilterOperator.IsGreaterThan,
Value=0 }
}
}, new FilterDescriptor ( ) {
Member=nameof(Product.Returned),
MemberType=typeof (bool),
Operator=FilterOperator.IsEqualTo,
Value=true }, new FilterDescriptor ( ) {
Member=nameof(Product.Damaged),
MemberType=typeof (bool),
Operator=FilterOperator.IsEqualTo,
Value=true }
}
});

DataSourceResult result=GridData.ToDataSourceResult(args.Request);

args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults;
}

protected override void OnInitialized ( ) { var rnd=new Random(); for (int i=1; i <=100; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name=$ "Product {i}",
Price=(decimal)rnd.Next( 1, 100 ),
Stock=rnd.Next( 0, 5 ),
InProduction=i % 11!=0,
Damaged=i % 13==0,
Returned=i % 17==0 });
}
}

public class Product {
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
public decimal Price { get; set; }
public int Stock { get; set; }
public bool Damaged { get; set; }
public bool Returned { get; set; }
public bool InProduction { get; set; }
}
} Regards, Dimo Progress Telerik

### Response

**Martin Herløv** answered on 15 Dec 2023

Thanks, super example to have as a reference. Yesterday I got it to work with the following code. Still wants to know if it's possible to mix server and client filtering. private void AddTelerikFiltering ( CertificateTradeOverviewQuery query ) { var searchBoxFilter=query.GridRequest.Filters
.SelectMemberDescriptors()
.Where(x=> x.Member=="ProductName" )
.ToList(); if (searchBoxFilter.Any())
{
CompositeFilterDescriptor toRemove=null; foreach ( var filterDescriptor1 in query.GridRequest.Filters)
{ var compositeFilter=(CompositeFilterDescriptor)filterDescriptor1; foreach ( var filterDescriptor2 in compositeFilter.FilterDescriptors)
{ var filterDescriptor=(FilterDescriptor)filterDescriptor2; if (filterDescriptor.Member=="ProductName" )
{
toRemove=compositeFilter; break;
}
}
} if (toRemove !=null )
query.GridRequest.Filters.Remove(toRemove); var cfd=new CompositeFilterDescriptor { LogicalOperator=FilterCompositionLogicalOperator.Or }; var clientFilter=new FilterDescriptor
{
Member="ClientName", Operator=FilterOperator.Contains,
Value=searchBoxFilter.First().Value.ToString()
}; var initialsFilter=new FilterDescriptor
{
Member="UserInitials", Operator=FilterOperator.Contains,
Value=searchBoxFilter.First().Value.ToString()
}; var productFilter=new FilterDescriptor
{
Member="ProductName", Operator=FilterOperator.Contains,
Value=searchBoxFilter.First().Value.ToString()
};
cfd.FilterDescriptors.AddRange( new [] { clientFilter, initialsFilter, productFilter });
query.GridRequest.Filters.Add(cfd);
}
}

### Response

**Dimo** commented on 15 Dec 2023

Well, yes, you can apply additional filtering to the data in the DataSource Result object. You can either use LINQ Where() or execute ToDataSourceResult () again with your own DataSource Request argument. However, you will be limited to the collection that you receive from the server, which is usually a single page. Moreover, the logical operator of the additional "client" filters will be always AND with regard to all "server" filters.

### Response

**Martin Herløv** commented on 15 Dec 2023

Let me understand you right. You are saying that if I use the filter component I can build filters on values not in the grid. And Use the filter values to build the grid result from many data sources. I also have filtering like this if (query.ViewDarwinTrades)
{
iQuery=iQuery.Where(x=> x.ProductInvestmentFund==darwinInvestmentFund);
} if (flowTypes.Any())
{
iQuery=iQuery.Where(x=> flowTypes.Contains(x.FlowType));
}

### Response

**Dimo** commented on 15 Dec 2023

The Filter component can produce filter descriptors, which you can use to filter a collection and feed the result to the Grid. The Grid itself has no part in this process, as you can see in the linked online demo. So, if you have a datasource that can handle the LINQ expression, which will be generated from the Filter component Value, then the answer to your question is "yes".
