# Grid: Combine GridFilterMode.FilterRow with ShowColumnMenu

## Question

**Hen** asked on 19 Dec 2022

I would like to use the ColumnMenu and the FilterRow at the same time. It seems to me that is not possible although it is so obvious !? I do no need any more filters in the ColumnMenu just the "Columns" Menu-Items to hide/show or lock/unlock columns.

### Response

**Yanislav** commented on 21 Dec 2022

Hello Hendrik, At this stage, FilterRow is not compatible with ColumnMenu. You may check the details on the matter in our Feedback Portal: [https://feedback.telerik.com/blazor/1530096-allow-using-filter-row-with-column-menu](https://feedback.telerik.com/blazor/1530096-allow-using-filter-row-with-column-menu) The item is currently scheduled for 4.1.0 of UI for Blazor. I've added your vote to keep proper track of the requests for this feature. You may additionally follow it to get notified of changes in its status. Since both functionalities ( ColumnMenu & FilterRow ) currently cannot be used in one Grid, what I can recommend you is to review and consider using the suggested workaround in the discussion from the

## Answer

**Leland** answered on 08 Apr 2024

It is now possible to use ColumnMenu and the FilterRow at the same time. Just do the following: ShowColumnMenu="true"
FilterMode="GridFilterMode.FilterMenu"
