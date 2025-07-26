# Default sort direction for a grid column

## Question

**Cra** asked on 17 May 2022

Hi, I was looking for a way to specify that a grid column should toggle thru the ListSortDirection in a different order. By default it appears a sortable column toggles through its sort directions in this order: 1st click to sort - Ascending 2nd click - Descending 3rd click - no sort That works for a majority of our grids and their columns (primarily strings and numbers) but we have some columns like 'Last Modified' dates that I'd like it to: 1st click to sort - Descending 2nd click - Ascending 3rd click - no sort This would also be more intuitive with our grids that we set their initial sort column to a date column in Descending order on page load. The 'first sort' a user expects is Descending on those columns. I assume there's a way to use OnStateChanged to do this but it'd involve tracking state changes ourselves and other custom code to try to indicate a certain column should toggle sort directions through different orders. Way too much work for us to introduce into our product at this time. Other tech stacks provide a way to specify the toggle order via column properties, and was hoping such a feature either existed or could be added. Thanks!

## Answer

**Hristian Stefanov** answered on 20 May 2022

Hi Craig, I fully agree with you that an option to set a default sort in the Grid column would be great for the component. We have an existing feature request opened on our public feedback portal regarding such functionality - Allow changing the Sorting Direction order via an attribute. I voted there on your behalf and raised the priority. In the meantime, upon interest, here is an example of how to set sorting order with the state: <TelerikGrid Data="@MyData" Sortable="true" AutoGenerateColumns="true" OnStateInit="@((GridStateEventArgs<SampleData> args)=> OnStateInitHandler(args))"> </TelerikGrid> @code {
async Task OnStateInitHandler(GridStateEventArgs <SampleData> args)
{
var state=new GridState <SampleData> {
SortDescriptors=new List <Telerik.DataSource.SortDescriptor> {
new Telerik.DataSource.SortDescriptor{ Member="LastModified", SortDirection=Telerik.DataSource.ListSortDirection.Descending }
}
};

args.GridState=state;
}

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 5).Select(x=> new SampleData
{
Id=x,
LastModified=new DateTime(2022, x, 28)
});

public class SampleData
{
public int Id { get; set; }

public DateTime LastModified { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Craig** commented on 26 May 2022

Thanks, Hristian. I apologize as I struggle finding existing requests in the Feedback portal. Probably just poor searching on my part. Good to know it's already requested and thanks for the example.

### Response

**Craig** commented on 26 May 2022

I should note your example code is for the initial sort only, which we have implemented for the very first sort. It does not change the sort cycle order, which is what the feature request is for.

### Response

**Hristian Stefanov** commented on 31 May 2022

Hi Craig, Thank you for noting, as I missed mentioning the above example is for the initial sort only, and the feature request is for the sort cycle order. Great observations.
