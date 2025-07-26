# Remove Row From Grid and NOT refresh all the data

## Question

**Tim** asked on 23 May 2021

I have a grid bound to a List<> of data. I have a button in the row to remove the row. I am not using "OnRead". If I would like to delete the row (and send the change to the backend), how do I remove the row from the grid without having to refresh all the data? I have tried removing it from the List<> and then calling StateHasChanged, but it has no effect on the grid. The record is removed in the backend. Please advise.

## Answer

**Marin Bratanov** answered on 24 May 2021

Hi Timothy, You can use observable collections for that. You can see how they work and how you can generally refresh the grid data in the following articles: generally on observable data, which Telerik components use it and how: [https://docs.telerik.com/blazor-ui/common-features/observable-data](https://docs.telerik.com/blazor-ui/common-features/observable-data) specific to the grid, with concrete examples scenarios and cases: [https://docs.telerik.com/blazor-ui/components/grid/refresh-data](https://docs.telerik.com/blazor-ui/components/grid/refresh-data) Regards, Marin Bratanov
