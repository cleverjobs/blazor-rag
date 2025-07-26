# Custom FilterMenuTemplate - await for async data to load.

## Question

**Adr** asked on 11 Jun 2021

I have a Telerik Blazor Grid where I have implemented a custom FilterMenuTemplate which is used on 12 of the columns in the grid. The custom FilterMenuTemplate displays a checkbox for all the distinct values in the database for that column field. It takes approximately 2-3 seconds for the data to be returned from the database, and this is for each column. When I first implemented the custom FilterMenuTemplate I only added it to a single column and it worked fine. Since adding it to all 12 columns I have experienced a null reference exception. The exception happens when the data hasn't finished being returned from the database and the collection Data property in the custom FilterMenuTemplate is null. I added a null check like so to stop the null reference exception from being thrown, instead displaying a message to the user that the data is loading...: <div class="filter-values-container"> @if (Data==null)
{ <p> Loading filter values... </p> }
else
{
foreach (var item in Data)
{ <div> <TelerikCheckBox Value="@(CurrentDistinctValueFilters.Contains(item.Key.ToString()))" ValueChanged="@((bool value)=> CheckBoxValueChanged(value, item.Key.ToString()))" Id="@($" { Field } _ { item.Key }")" Enabled="@EnableDistinctValues" /> <label for="@($" { Field } _ { item.Key }")" class="k-label k-form-label"> @item.Value </label> </div> }
} </div> What I was hoping would happen is that once the user clicks on the column filter, that the filter popup would temporarily show the loading message and then dynamically update and remove the loading message instead show the checkboxes once the Data property had data from the database. This doesn't appear to happen, instead the filter popup remains open and the loading message stays on screen. In order to get the filter popup to update with the checkboxes the user has to cancel the filter popup and re-active it to show the data. Is there away of updating the filter popup dynamically once it is open and the data is available to render the checkboxes? As a temporary crud workaround what I have none for now is disabled all the columns with these particular custom filters by binding the Filterable property on those columns to a boolean property which gets set to true when ALL the data for ALL 12 of those columns have been retrieved from the database. e.g. Filterable="@DataLoadedForGridFilters" The downside to this is that none of those 12 column filters are enabled to be used for about 25+ seconds after the grid and then the associated column filter data have been retrieved from the database.

## Answer

**Dimo** answered on 14 Jun 2021

Hello Adrian, Your observations are correct - the data for the filter template needs to be available before the filtering popup is opened for the first time. I am afraid that dynamic updates are not supported at this time, because the popup is rendered in the page <body> and is not affected by StateHasChanged calls. We have some ideas for the future, but for the time being, this is an existing limitation. Perhaps you could enable filtering for each column separately, as soon as its own data is loaded? Bound columns have a Filterable property as well. Other than that, the cumulative data load seems so resource-intensive, that I would also consider some form of caching it. Even if the popups refreshed on the fly, users may still have to wait longer than they expect with an open filter menu. Regards, Dimo Progress Telerik
