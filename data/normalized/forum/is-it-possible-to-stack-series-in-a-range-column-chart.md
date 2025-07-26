# Is it possible to 'stack' series in a Range Column Chart?

## Question

**Mar** asked on 13 Dec 2023

Hi We have run into some difficulties with charting a 'floating' stacked series. Is it possible to 'stack' series in a Range Column Chart? Where the data in this REPL would be represented by one column with two regions: [https://blazorrepl.telerik.com/cRPGbRkN53vvK3Y152](https://blazorrepl.telerik.com/cRPGbRkN53vvK3Y152) We have been working around the issue by using a Column chart and creating an invisible stacked series to move the real series into position. However, we struggle when negative values are required, specifically if a column is to range between a positive value to a negative value, e.g. From 47 to -10. Thanks Mark

## Answer

**Mark** answered on 08 Jan 2024

My feature request was declined, Stackable range column/bar series (telerik.com). Latest Workaround Within the context of our Telerik Charts, Telerik staff found a new workaround tailored for stacked charts. You can explore and test the solution using this REPL link.

### Response

**Dimo** answered on 15 Dec 2023

Hello Mark, Indeed, we don't support this currently. A possible hack is to show two Charts on top of one another. If you fancy this approach and it works for you, then go for it. [https://blazorrepl.telerik.com/wHPclTFm28WuoSOp57](https://blazorrepl.telerik.com/wHPclTFm28WuoSOp57) The major downside is that the bottom Chart will have no interactivity. You also can't have legends. Regards, Dimo Progress Telerik

### Response

**Mark** commented on 19 Dec 2023

Thanks, Dimo. Is there any way to stack series on a waterfall chart?

### Response

**Dimo** commented on 20 Dec 2023

Sorry, Mark, stacked waterfall series are not supported either.
