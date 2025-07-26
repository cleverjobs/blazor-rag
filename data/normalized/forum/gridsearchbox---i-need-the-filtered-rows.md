# GridSearchBox - I need the filtered rows

## Question

**Gra** asked on 14 Oct 2020

When using the GridSearchBox to filter the grid, is it possible to obtain the filtered row items? I want to know what rows are currently displayed.

## Answer

**Marin Bratanov** answered on 14 Oct 2020

Hi Graham, It is possible and rather straightforward through the OnRead event. I made the following Knowledge Base article that explains the situation: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data.) Regards, Marin Bratanov

### Response

**Graham** answered on 15 Oct 2020

Thanks. I got it working but had to change my collection to ObservableCollection to get the grid to refresh when I changed the data externally - I am using a drop-down control to apply a filter to the data. (I think Telerik advise using ObservableCollection as the default?). Question - is there a way of accessing the GridSearchBox text or knowing if the GridSearchBox triggered the OnRead event? thanks

### Response

**Graham** answered on 15 Oct 2020

Regarding my last question - I found this which allows me to see the current filters... [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#get-information-from-the-datasourcerequest](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#get-information-from-the-datasourcerequest) thanks

### Response

**Marin Bratanov** answered on 15 Oct 2020

Hello Graham, Indeed, an observable collection is needed when you will be changing the data from an external place via the .Add(), .Remove() and .Clear() methods of the collection, you can read more on this here. We can't recommend that as the default, because whether you need that depends on your scenario and it is up to you to decide. The grid merely needs an IEnumerable - list, array, observable collection. On getting data from OnRead - that's the way - you can loop over the information in the .Request object to get what you need out of it. Regards, Marin Bratanov
