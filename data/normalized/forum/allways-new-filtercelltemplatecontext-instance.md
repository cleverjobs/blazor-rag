# Allways new FilterCellTemplateContext instance

## Question

**Vad** asked on 31 Aug 2022

I have created custom row filtering. TelerikDateRangePicker is used inside FilterCellTemplate. Based on the examples from the article -> [https://demos.telerik.com/blazor-ui/grid/custom-filter-row](https://demos.telerik.com/blazor-ui/grid/custom-filter-row) <- select start, end dates and clear button handlers was implemented. But I found that for each handler (select start or end date) new instance of FilterCellTemplateContext has been used. And when I try to get selected values in OnRead method from GridReadEventArgs -> Request.Filters, filters do not contain selected date range. Could someone please explain why there are a lot of instances of FilterCellTemplateContext (more that one on each method call)? How can I get selected date range values in OnRead methods from GridReadEventArgs? Thanks!

## Answer

**Svetoslav Dimitrov** answered on 05 Sep 2022

Hello Vadzim, I have prepared a short sample code snippet where I investigated the issue you have reported to us. See it from this REPL link. When I filtered the "Salary" column the OnRead event gets the filter descriptors as expected. Can you modify the snippet so that the issue is reproducible so that we can further investigate? Regards, Svetoslav Dimitrov Progress Telerik
