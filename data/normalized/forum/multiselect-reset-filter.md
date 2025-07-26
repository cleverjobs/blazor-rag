# Multiselect reset filter

## Question

**EdEd** asked on 24 Mar 2022

I have the following set up. <TelerikMultiSelect Data="@lstXfers" @ref="@Xrefs" @bind-Value="@lstSelectedXfers" TextField="FermentationName" ValueField="FermentationXferId" Width="250px" ClearButton="true" AutoClose="false" OnBlur="OnXferBlur" OnRead="OnXferRead" Filterable="true" FilterOperator="StringFilterOperator.Contains" /> I am doing custom filter to allow the user to enter a filter and, when the control loses focus, if the typed in filter is an exact match to one of the available items, then the typed in item will be added. Everything works great, with one exception. I can't seem to clear the Request.Filters Telerik.DataSource.FilterDescriptor collection. private FilterDescriptor filter; protected void OnXferRead(MultiSelectReadEventArgs args)
{
if (args.Request.Filters.Count()> 0)
{
filter=args.Request.Filters[0] as Telerik.DataSource.FilterDescriptor;

var q1=from a in db.Fermentations
where a.IsActive==true && a.SiteId==appData.SiteId
select new FermentationXferModel()
{
FermentationName=a.FermentationName,
FermentationXferId=a.FermentationId
};
q1=q1.OrderBy(a=> a.FermentationName).Distinct();

lstXfers=q1.ToList();
args.Data=lstXfers;
var lstSelectedItemsToExclude=(from a in lstXfers
where lstSelectedXfers.Contains(a.FermentationXferId)
select a).ToList();
var filterItems=(from a in lstXfers
where !a.FermentationName.ToLower().StartsWith(filter.Value.ToString().ToLower())
select a).Except(lstSelectedItemsToExclude).ToList();
args.Data=(from a in (List <FermentationXferModel> )args.Data select a).Except(filterItems);

}
else
args.Data=lstXfers;

}


public void OnXferBlur()
{
if (filter !=null)
{
FermentationXferModel filterEntry;
filterEntry=(from a in lstXfers
where a.FermentationName.ToLower()==filter.Value.ToString().ToLower()
select a).FirstOrDefault();
if (filterEntry !=null)
{

// mark it as selected
filterEntry.Selected=true;
// create a new list to force a refresh.
// this thing doesn't support observablecollections.
List <int> lst=new List <int> (lstSelectedXfers);
// add the matching entry
lst.Add(filterEntry.FermentationXferId);
//copy the list to the bound variable
lstSelectedXfers=new List <int> (lst);
// Clean up the typed in filter
Task.Run(async ()=> await jsRuntime.InvokeVoidAsync("clearMultiselectInput"));
}
else
{
var q1=from a in db.Fermentations
where a.IsActive==true && a.SiteId==appData.SiteId
select new FermentationXferModel()
{
FermentationName=a.FermentationName,
FermentationXferId=a.FermentationId
};
q1=q1.OrderBy(a=> a.FermentationName).Distinct();

lstXfers=q1.ToList();
Xrefs.Data=lstXfers;
}
}

} And teh js: function clearMultiselectInput() { var inputs=document.querySelectorAll(".k-multiselect .k-input-inner"); inputs.forEach(e=> e.value="") } Ideally, in the OnBlur handler if the private FilterDescriptor filter property is not null, then I want to clear it. How??? Thanks... Ed

## Answer

**Marin Bratanov** answered on 27 Mar 2022

Hi Ed, I do not see a line that says filter=null; so the view-model field will always stay populated. Anyway, I think the issue is the CSS seletor for the input, this one would be a correct one after 3.0.0 .k-multiselect .k-input-values input With that, I was able to clear the input on blur. Regards, Marin Bratanov Progress Telerik

### Response

**Ed** commented on 27 Mar 2022

Hi Marin, The question here is how do I get the filter in the OnBlur to be able to set it to null? Thanks ... Ed

### Response

**Marin Bratanov** commented on 28 Mar 2022

The component provides the DataSourceRequest (and thus the FilterDescriptor) only in the OnRead event. If you need the information later, caching it in the view model is the correct way to go. You can't clear the filter directly because it is something the component makes on the fly based on the parameters it has (such as the filter operator you've chosen), and the user input in its text box. Thus, if there is nothing in the textbox, there filter descriptor won't have a value.

### Response

**Ed** commented on 31 Mar 2022

Hi Marin, Ok, so as you suggested, I cached off the Filter descriptor to a private FilterDescriptor filter; Then in the OnBlur, the last thing I do is set filter=null; I click on the multiselect and so far so good. I see the list shown below: Next I type in 205314. I get the following: still good. I now tab off the control. still good. Next, I click back on the control: I expected to see the full unfiltered list as we set the filter to null in the onblur. Any ideas? Thanks ... Ed

### Response

**Nadezhda Tacheva** commented on 04 Apr 2022

Hi Ed, Using the correct selectors to access and clear the search input value and clearing the filter variable in addition should serve to deliver your desired result. Could you please send us a runnable version of your latest configuration, so we can debug on our end and find what might be missing? Thank you in advance! I'll be looking forward to hearing from you!
