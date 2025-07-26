# Persist multiselect after data is refreshed and component re-rendered

## Question

**n/an/a** asked on 05 May 2022

Hello, In grid component, how do you keep the selected rows after you have performed an action on them and data needs to be refreshed and component re-rendered i.e I am sending the selected items in the server and performing operation on them in the data base, hence the component needs refreshed. Basically, when the component re-renders, I want the same rows upon which the action has been performed to be automatically selected . Thank you. Kind regards

## Answer

**Timothy J** answered on 05 May 2022

We do this by caching the primary key of the selected rows before the refresh of the data and then selecting (programmatically) the rows after the refresh. var response=await this.GetResponseAsync(dsr);
arg.Data=response.Items;
arg.Total=response.Count;

var tempSelected=new List <TModel> (this.SelectedItems);

foreach (TModel item in arg.Data)
{
if (tempSelected.SingleOrDefault(_=> Equals(_.Id, item.Id)) is { } alreadySelected)
{
tempSelected.Remove(alreadySelected);
tempSelected.Add(item);
}
}



this.SelectedItems=tempSelected;

### Response

**n/a** commented on 06 May 2022

thanks Timothy! At the end did it slightly different, but your answer is definitely something to keep in mind for future reference.
