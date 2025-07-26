# Grid shows up with columns but no row data!

## Question

**Dea** asked on 23 Jan 2023

Heres what I get on the page: See it has the column info from the DB and it should be showing 4 rows of data. When I debug I see it returning 4 rows! I have it hooked up as such: <TelerikGrid @ref="@GridMarginInfoResults" Data="@GDMarginInfoResults" AutoGenerateColumns="true" Pageable="true" Sortable="true" Class="custom-row-colors"> </TelerikGrid> private List<MarginInfo> GDMarginInfoResults { get; set; } public TelerikGrid<MarginInfo> GridMarginInfoResults { get; set; } What am I missing?

### Response

**Deasun** commented on 23 Jan 2023

Note! When I add a btn to page and on its click event I call the procedure that fills that grid it then appears with the rows! I also tried the call from the page after render event and that did not help either, same blank grid.

### Response

**Deasun** commented on 24 Jan 2023

this is starting to be an issue. Holding me back from going production. Looks like a bug to me!

### Response

**Nadezhda Tacheva** commented on 26 Jan 2023

Hi Deasun, I am sorry you are facing difficulties with the implementation. Let's try to find out what is causing the issue on your end. I've prepared a working runnable sample with the Grid declaration that you shared: [https://blazorrepl.telerik.com/mdEFcUbl37MMtM8U33.](https://blazorrepl.telerik.com/mdEFcUbl37MMtM8U33.) Can you please modify that to replicate your exact configuration and reproduce the issue, so I can further revise it? You may use some dummy data generation as per the sample I shared. I'd like to see how and when you are providing data to the Grid in order to find what causes the issue on your end. Thank you in advance!
