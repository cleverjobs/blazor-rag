# Grid column sorting always uses Ascending

## Question

**Adr** asked on 07 May 2021

I have a Blazor grid and when I click the column heading it sorts the data Ascending. If I click the same column heading again, I'm expecting it to toggle to Descending, but the DataSourceRequest object always has Ascending regardless. I see that the Telerik Demos work and I don't think I've done much different that those. I notice in the demos there is an arrow indicating which way the sort is going, in my grid no arrow icon is visible.

### Response

**Marin Bratanov** commented on 07 May 2021

I have a couple of guesses what could be going wrong: - an error somewhere on the backend does not return correct data - a StateHasChanged handler overrides the user action, or the reference to the DataSourceRequest object is changed by other application code - if you are using OnRead to fetch data, there isn't a StateHasChanged() call after updating the grid
