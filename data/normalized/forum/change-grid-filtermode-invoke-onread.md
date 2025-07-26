# Change grid FilterMode invoke OnRead

## Question

**Cla** asked on 21 Mar 2025

Hi, i have a TelerikGrid who manage paging and read data using the OnRead property. On top of my grid i have a button to open/hide the inline grid filter (binding a property with the FilterMode grid property). Now the problem is: when i open o close the filter (changing the FilterMode property) the OnRead method is invoked. I don't want to do a server request to read data if not necessary, and simply open or close the filter does not affect the data loaded in the current page of the grid. how to avoid this? This is a sample code to reply the issue: [https://blazorrepl.telerik.com/cfOnmPFz42OsM8ki11](https://blazorrepl.telerik.com/cfOnmPFz42OsM8ki11) Thanks

## Answer

**Anislav** answered on 21 Mar 2025

I checked the TelerikGrid code, and it appears that changing the FilterMode property automatically triggers the OnRead event. There isn't a built-in way to prevent this behavior. However, you can implement a workaround by using CSS to hide or show the filter row instead of modifying the FilterMode property. This way, the grid won't trigger a new data fetch when toggling the filter visibility. Here’s an example of how you can achieve this: @if (!IsFilterRowDisplayed)
{ <style> tr.k-filter-row { display: none;
} </style> } Here is the link to the complete sample code: [https://blazorrepl.telerik.com/mzuxQFPA19lknC0g32](https://blazorrepl.telerik.com/mzuxQFPA19lknC0g32) Regards, Anislav Atanasov

### Response

**Anislav** commented on 24 Mar 2025

Claudio, did my suggestion helpt you?

### Response

**Claudio** commented on 24 Mar 2025

Thanks Anislav, the workaround solve the issue but i have to change the behaviour of all grids used in my application. I think who call OnRead on FilterMode property change is a bug, it should be called only when the filter is updated. Can you evaluate to solve the issue avoiding to call OnChange for FilterMode property change on next version of the library? Thanks

### Response

**Anislav** commented on 24 Mar 2025

I’m not part of Progress, so I’m unable to assist with the further evaluation of this feature. I assume there was a specific reason for implementing it this way, as changing the FilterMode may trigger other actions as well. Unfortunately, I don’t have the time to investigate this further at the moment. Regards, Anislav Atanasov

### Response

**Dimo** answered on 26 Mar 2025

Hi Claudio, The Grid fires OnRead in OnParametersSetAsync(). The behavior is by design. We believe it's safer to make the Grid more reactive, rather than less reactive to runtime changes. If you wish to avoid the database call without using custom CSS, you can cache the received data from the previous OnRead event. Here is a KB article with a similar example: Cache and reuse data in the Grid OnRead event Regards, Dimo
