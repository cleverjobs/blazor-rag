# Reference to data displayed in filtered grid?

## Question

**Dou** asked on 26 Mar 2021

I have a use case where I need to write an SSRS report that is based off of the data displayed in a TelerikGrid. I obviously have a reference to the source data the the grid is displaying but if the user filters the grid and then wants to run the report I can't figure out how to get a reference to the filtered data the grid is displaying. Thinking I should be able to respond to the OnStateChanged event but I can't see how to get a reference to the IEnumerable from the GridStateEventArgs object which I would need to package up and send to my SSRS report. If I respond to OnRead I can get the data using the ToDataSourceResult extension method but then the default filtering doesn't work. I don't need to implement custom filtering so is there an easy way to get the data I need?

## Answer

**Marin Bratanov** answered on 29 Mar 2021

Hi Doug, The following article shows how you can use the filtered data in the grid: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data.) You need to use the OnRead event so that's the data you have in the grid. The key thing about using this event is that once you add a handler to it, you must implement all the data source operations in that event handler, including filtering. Our .ToDataSourceResult() extension method is a convenient way to do that. Regards, Marin Bratanov Progress Telerik

### Response

**Doug** answered on 29 Mar 2021

Thanks Marin, that helps but I'm still having a problem when the user filters the grid and then does something outside the grid which causes the source data to change. OnRead isn't going to fire in that case and I can't blindly set the grid data to a copy of the new source data because then the grid displays the source data without honoring the filter. Any thoughts on how best to manage that scenario?

### Response

**Marin Bratanov** answered on 30 Mar 2021

Hi Doug, If there is something outside the grid that changes the data displayed in the grid, you will have to change the Data collection of the grid. This means that you already have that collection in either case, especially when you are using the OnRead event. To see how to make the grid change its display when you alter its source data, see this article: [https://docs.telerik.com/blazor-ui/components/grid/refresh-data.](https://docs.telerik.com/blazor-ui/components/grid/refresh-data.) Through OnRead you can cache the last data source request so you can apply it to new data if firing its logic again is not suitable for you. Regards, Marin Bratanov
