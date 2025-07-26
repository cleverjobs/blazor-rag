# Expand/Collaps Details on RowClick instead of clicking the expand/collapse button?

## Question

**imw** asked on 11 Jan 2022

Instead of having the user click on the expand/collapse button on the row, we want them to be able to click the entire row to expand/collapse the details template. We have implemented it like and that seems to be working, but it seems like there should be a better way to do this, perhaps even built in? async Task OnRowClickHandler(GridRowClickEventArgs args)
{

args.ShouldRender=true;

int currentIndexOfItem=CorporateCustomerList.IndexOf(args.Item);
if (currentIndexOfItem> -1)
{
var state=Grid.GetState();

if(state.ExpandedRows.Contains(currentIndexOfItem))
state.ExpandedRows.Remove(currentIndexOfItem);
else
state.ExpandedRows.Add(currentIndexOfItem);

await Grid.SetState(state);


}
}

### Response

**imwise** commented on 11 Jan 2022

We've noticed one problem with this though, which I am not sure if it is a bug in the grid or something we are doing wrong. If we have a grid with lets say 5 items/rows, and click lets say the third one, everything will work fine. If we then do some kind of filtering and only one row is displayed, the int currentIndexOfItem=CorporateCustomerList.IndexOf(args.Item); will still return the index that row had before the filtering (in this case 3), despite the grid now only containing one row. We will then try to expand/collaps the third row, which will of course not work as only one row is displayed. Is this a bug as we are getting an index of a row that is not being displayed? Or are they still considered to be there even though they are not displayed? If the latter, how are we supposed to handle this (which probably has noting to do with expand/collapse in particular)?

### Response

**imwise** commented on 11 Jan 2022

Actually, you can simplify this to that int currentIndexOfItem=CorporateCustomerList.IndexOf(args.Item); Always gives you the wrong currentIndexOfItem if you are using filters, which might be correct regarding the actual data but not regarding what is displayed on the screen. How can we solve this?

## Answer

**Nadezhda Tacheva** answered on 14 Jan 2022

Hi Patrik, Generally speaking, expanding/collapsing the details template on row click would be considered a custom scenario rather than a supported out of the box functionality as it would interfere with the built-in behavior of the Grid selection which is normally done on row click. Furthermore, one could want to perform various actions when the user clicks on a Grid row, so this is why we have exposed the OnRowClick event to allow such customizations based on the desired result. That said, you have chosen the correct approach for the use case - handle the OnRowClick event and set the expanded rows through the Grid state. Now, as the ExpandedRows collection contains the indexes of the corresponding expanded items, when some additional operation that could possibly change the items indexes is performed with the Grid (such as sorting, filtering), that could lead to undesired behavior and should be taken into consideration in the business logic. Even though the current approach allows programmatic control of the expanded items, working with only their indexes could be tricky in some scenarios and requires some additional setup. Therefore, for our upcoming 3.0.0 release we will introduce an enhancement in this regard - the state will expose a collection of the actual expanded items, instead of just their indexes which will make such scenarios be achieved a lot easier. You can check the public request here - Expanded Items in the Grid State. Version 3.0.0 of Telerik UI for Blazor is expected to be live around January 19th, so you can try it yourself afterwards. I hope you will find the above information useful. If any further questions appear, please let us know. Regards, Nadezhda Tacheva
