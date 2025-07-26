# Using OnRead to Open Autocomplete on Init

## Question

**Phi** asked on 12 Mar 2023

Hi Im using the OnRead event to display data in the autocomplete which works fine as expected for remote data. What I want to do is display the drop down when the application starts to show some local search results without typing in any text. The OnRead event does fire as it should when the component init runs and ive confirmed the data collection has data in it but the dropdown doesnt open up to show any data unless some text is entered. Is what im wanting to do possible please? Phil

### Response

**Dimo** commented on 14 Mar 2023

Phil - are you using the Open method? If you call it in OnAfterRenderAsync, the AutoComplete dropdown show display.
