# How can we use a Flux approach with new Grid system (new OnRead, server side Pagination etc.)

## Question

**Eco** asked on 09 Mar 2022

Hello everyone, I hope you are good. In our application we use the Flux approach, with Fluxor library. Before the 3.0.0 version release, we had no issue to use the Grid component with server side pagination while using Flux. To simplify, let's imagine that we use only one Store, with one simple state : public record HouseState ( List<HouseSimple> Houses, int TotalCount ) In grids components, we used to: Bind "Data" parameter to the "Houses" field of the state Bind the "TotalCount" parameter to the "TotalCount" field of the state Bind this callback: protected void ReadItems ( GridReadEventArgs args ) { var page=args.Request.Page; var filters=args.Request.Filters; var sorts=args.Request.Sorts;

dispatcher.Dispatch( new LoadHouseAction(page, filters, sorts));
} As you can see, we get all required information (page, skip etc.), then we dispatch the action. The action will perform an API call, and will create another state with new received data. <TelerikGrid Data="@State.Houses" TotalCount="@State.TotalCount" OnRead="@ReadItems"> After migration of Telerik 3.0.0 We cannot use the "TotalCount" parameter anymore. So we need to use the OnRead event, in order to set the TotalCount in it. In the documentations, all examples are like : protected async Task ReadItems ( GridReadEventArgs args ) {
DataEnvelope DataResult=await FetchPagedData(args.Request.Page, args.Request.PageSize);

args.Data=DataResult.CurrentPageData;
args.Total=DataResult.TotalItemCount;
} This approach is made to be used with a classic approach to "ask and wait the data". It could work perfectly but in the approach that we use (flux pattern) it is more like "ask and save in state the data, and views use state ". To be able to keep the same functionality of server side pagination, we had to subscribe in our view to the event "the data in the store has been refreshed" and then call the Rebind method of the grid. Something like that: private void UpdateGridData ( AgencesSetAgencesAction action ) { if (GridRef is null ) return;
GridRef.Rebind();
} protected void ReadItems ( GridReadEventArgs args ) { var total=this.HousesState.Value..TotaCountl; var data=this.HousesState.Value.Items;

args.Total=total;
args.Data=data ?? Enumerable.Empty<HouseItem>();
} It works perfectly, but it seems that we break the Flux approach. Is there any other way to perform that, while using flux approach or something like it? Thanks a lot, do not hesitate to ask for some precision. // Dylan

## Answer

**Marin Bratanov** answered on 10 Mar 2022

Hello, The following thread discusses a very similar scenario and I hope my answer there helps you as well: [https://www.telerik.com/forums/how-to-set-grid-data-total-count-and-other-paging-info-declaratively-or-programmatically-outside-of-onread](https://www.telerik.com/forums/how-to-set-grid-data-total-count-and-other-paging-info-declaratively-or-programmatically-outside-of-onread) Regards, Marin Bratanov Progress Telerik

### Response

**Ecofip** commented on 11 Mar 2022

Hello, Thanks for your answer, and I apologize for the "doublon", I haven't seen the post you linked. (It seems that there are some trouble with the search module on the Telerik Blazor forum, I tried many combinaison of key words and did not return me this post) I will answer and bring my contribution on the other post. Regards, Dylan
