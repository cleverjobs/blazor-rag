# Grid Filter Input Reset on refresh

## Question

**Joh** asked on 05 Oct 2022

I am using a async task which reloads the grid every few seconds. After fetching the rows, the whole page is refreshed via InvokeAsync(StateHasChanged). The issue I have is if the user is trying to set a column filter in the grid, the refresh resets any changes the user has made (but not applied). Is there a way to either not refresh the filter control or be notified when the filter is opened and closed (so the refresh task can not refresh the page)? Attached short video describing the issue. The updated label at top left shows when page is refreshed. When typing the filter value after refresh, inputting the next digit seems to wipe out previous digits. Changing filter operation also seems to lose the change.

## Answer

**Nadezhda Tacheva** answered on 10 Oct 2022

Hi John, As the whole page is refreshed, it is expected that the FilterMenu is also re-rendered and the user input is lost since it is not saved. In this scenario, it will not be possible to save and load Grid State from browser LocalStorage as filters are not yet applied and there are no filter descriptors added to the Grid state. I'd say the key point here is why you actually need to refresh the whole page. A possible use case is that you are fetching live data and the Grid needs to be updated every few seconds to display relevant data. If this is the case, I would recommend refreshing just the data collection that the Grid uses instead of re-rendering the page. There are several options you can use to achieve that - you may find details in the Grid - Refresh Data article. Thus, the Grid data will be updated as needed but the filter input will not be omitted. I hope you will find this information useful to move forward with your application. Please let us know if any further questions are raised. Regards, Nadezhda Tacheva Progress Telerik
