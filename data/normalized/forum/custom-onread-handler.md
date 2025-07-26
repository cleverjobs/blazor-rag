# Custom OnRead Handler

## Question

**Adr** asked on 06 Jul 2021

I have a Telerik Blazor Grid where I am doing a custom OnRead event to get the data. I am trying to detect within that event handler when the grid filters have changed as I need to request extra data if someone changes the grid filters in anyway. I have tried comparing the previous filters with the new request filters but it says they are always different even when just requesting a new page in the grid. My code looks like this: protected override async Task OnReadHandler ( GridReadEventArgs e ) { if (!ReHydrateGridFromPersistedState)
{ //no grid state exists so call the database for data var filtersHaveChanged=GridRequest !=null && !GridRequest.Filters.Equals(e.Request.Filters);

GridRequest=e.Request; if (filtersHaveChanged)
{
ExtraData=await GetExtraDataAsync();
} await base.OnReadHandler(e);
} else {
GridRequest=e.Request;
}
} var filtersHaveChanged=GridRequest !=null && !GridRequest.Filters.Equals(e.Request.Filters); /* filtersHaveChanged is ALWAYS true */

## Answer

**Marin Bratanov** answered on 06 Jul 2021

Hi Adrian, Generally speaking, you should request the new data every time OnRead fires, that is an indication that the user changed something in the grid that demands new data. Thus, fetching data only for some cases will result in your users seeing invalid information. That said, I can suggest you consider the StateChanged event which tells which aspect of the grid was last modified through its event arguments (say, filter descriptors). You can read more about it in the Grid State article (see the "Get and Override User Action That Changes The Grid" section for a particular example about getting that info). The third option would be to write a comparer for the filter descriptors that compares the actual values rather than references (references is how the framework compares objects by default). Regards, Marin Bratanov Progress Telerik

### Response

**Adrian** commented on 07 Jul 2021

Thanks for the help. Do you have a list of all the possible string values that can be in GridStateEventArgs<TItem>.PropertyName ? Currently I only know of "Page" and "FilterDescriptors"

### Response

**Marin Bratanov** commented on 07 Jul 2021

I made a pull request with that info for the docs, it will be live when it gets merged and in the meantime you can see the list in the PR.
