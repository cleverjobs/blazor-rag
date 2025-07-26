# Filter Template - Detecting the Clear Filter Button

## Question

**Jen** asked on 29 Jul 2021

I've just started to look into building custom filter templates and using the example here to help me. I've noticed that when I click the 'Clear' button, it will clear the checkbox items but if I select a new item, on hitting 'Filter' it will re-add previous selections to the filter and they will show on the checkbox menu again. Can someone show me how I'd modify the example to rectify this please, and get it to filter correctly after clearing the intial selection? This is the code from the example I've used, unmodified: @using Telerik.DataSource

This custom filter menu lets you choose more than one option to match against the data source <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" Height="400px" Width="600px" Pageable="true"> <GridColumns> <GridColumn Field="Id" Filterable="false" Width="80px" /> <GridColumn Field="Size"> <FilterMenuTemplate> @{
// we store a reference to the filter context to use in the business logic to show we can
// we could, alternatively pass it as an argument to the event handler in the lambda expression
// which can be useful if you want to use the same filter for several columns
// you could then pass more arguments to the business logic such as field name and so on
theFilterContext=context;
}

@foreach (var size in Sizes)
{ <div> <TelerikCheckBox Value="@(IsCheckboxInCurrentFilter(context.FilterDescriptor, size))" TValue="bool" ValueChanged="@((value)=> UpdateCheckedSizes(value, size))" Id="@($" size_ { size }")"> </TelerikCheckBox> <label for="@($" size_ { size }")"> @if (size==null) // part of handling nulls - show meaningful text for the end user
{ <text> Empty </text> }
else
{
@size
} </label> </div> } </FilterMenuTemplate> </GridColumn> <GridColumn Field="ProductName" Title="Product" Filterable="false" /> </GridColumns> </TelerikGrid> @code {
FilterMenuTemplateContext theFilterContext { get; set; }
public List <string> CheckedSizes { get; set; }=new List <string> ();

public bool IsCheckboxInCurrentFilter(CompositeFilterDescriptor filterDescriptor, string size)
{
// get all current filter descriptors and evaluate whether to select the current checkbox
// the default value for string filter descriptors is null so it would select the null checkbox always
// so we will add a check to ensure it matches the desired operator - IsNull (see the UpdateCheckedSizes method below)
if (size==null)
{
foreach (FilterDescriptor item in filterDescriptor.FilterDescriptors)
{
if(item.Operator==FilterOperator.IsNull)
{
return true;
}
}
return false;
}
return filterDescriptor.FilterDescriptors.Select(f=> (f as FilterDescriptor).Value?.ToString()).ToList().Contains(size);
}

public void UpdateCheckedSizes(bool value, string itemValue)
{
// update the list of items we want to filter by
var isSizeChecked=CheckedSizes.Contains(itemValue);
if (value && !isSizeChecked)
{
CheckedSizes.Add(itemValue);
}

if (!value && isSizeChecked)
{
CheckedSizes.Remove(itemValue);
}

// prepare filter descriptor
var filterDescriptor=theFilterContext.FilterDescriptor;

filterDescriptor.FilterDescriptors.Clear();
// use the OR logical operator so we include all possible values
filterDescriptor.LogicalOperator=FilterCompositionLogicalOperator.Or;
CheckedSizes.ForEach(s=> {
// instantiate a filter descriptor for the desired field, and with the desired operator and value
FilterDescriptor fd=new FilterDescriptor("Size", FilterOperator.IsEqualTo, s);
// set its type to the field type you filter (the Size field in this example)
fd.MemberType=typeof(string);
// handle null values - use a specific filter operator that the user cannot select on their own
// in this custom filter template (the grid has it in a dropdown by default)
if(s==null)
{
fd.Operator=FilterOperator.IsNull;
}

filterDescriptor.FilterDescriptors.Add(fd);
});

//ensure there is at least one blank filter to avoid null reference exceptions
if (!filterDescriptor.FilterDescriptors.Any())
{
filterDescriptor.FilterDescriptors.Add(new FilterDescriptor());
}
}

// sample grid data

public List <SampleData> GridData { get; set; }

protected override void OnInitialized()
{
GridData=Enumerable.Range(1, 70).Select(x=> new SampleData
{
Id=x,
Size=Sizes[x % Sizes.Length],
ProductName=$"Product {x}"
}).ToList();
base.OnInitialized();
}

public class SampleData
{
public int Id { get; set; }
public string Size { get; set; }
public string ProductName { get; set; }
}

public string[] Sizes=new string[] { "XS", "S", "M", "L", "XL", null };
}

### Response

**Marin Bratanov** commented on 29 Jul 2021

The Clear button will clear the FilterDescriptors the grid has, but those checkboxes are not tied to them but to a custom collection in the view-model. You may want to use the grid state (see the StateChanged example to capture the filtering change in the "Get and Override User Action That Changes The Grid" section) to also clean that collection accordingly. That said, I can't reproduce a problem with the sample from the docs, so I recommend comparing the problematic code you have against it to see what's the difference causing unexpected behavior on your end.

### Response

**Jenna** commented on 30 Jul 2021

Thank you Marin - the code I'm using with the issue is the exact code in the sample with no amendments! but obviously if you're unable to replicate there must be something else affecting it at my end. Thanks for your help, I'll look into Grid State.

### Response

**Jon** commented on 23 Aug 2021

I am having the same issue. To replicate: Add a few filters (s/m/l). Filter. Clear Filters. Add filter xl. filter. The filter will now contain s/m/l/xl.

### Response

**Nadezhda Tacheva** commented on 26 Aug 2021

Hi Jon, Have you tried Marin's suggestion from the previous comment? If yes, but you are still experiencing some issues, you can send us a runnable reproduction, so we can investigate further and provide some insights. Regards, Nadezhda Tacheva

### Response

**Jon** commented on 26 Aug 2021

Yes. Best I can tell the args will show a "filter" event, but can't tell if it is clear or not. Adding another attribute to the event with button name or changing type to indicate a clear. Or perhaps make the template have an option for bool AllowClear, event handler OnClearFilter.. So many choices.

### Response

**Nadezhda Tacheva** commented on 31 Aug 2021

Hi Jon, Indeed, it will be useful to know when the Clear button was clicked. We have an opened feature request for ability to control both Clear and Filter actions that you may find interesting in this regard - Allow control over Filter and Clear actions in the FilterMenu. I have added your vote to increase its popularity as we are prioritizing the feature requests implementation based on the community interest and demand. You can also subscribe to receive email notifications when its status changes. This is the best way to keep in track with the progress of the feature as once we know which release will contain its implementation , we will update its status in the
