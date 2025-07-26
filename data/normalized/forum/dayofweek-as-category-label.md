# DayOfWeek as Category label

## Question

**Ila** asked on 10 May 2023

I'm using ChartCategoryAxis Type="@ChartCategoryAxisType.Date" BaseUnit="@ChartCategoryAxisBaseUnit.Fit" Is there a way to show the labels as DayOfWeek (Wednesday) instead of date (3/1) ?

## Answer

**Yanislav** answered on 15 May 2023

Hi Ilan, You can show the name of the day of the week as text, but you need to set up a label template. This lets you turn the label value into a JavaScript Date object, which has a really handy method called getDay(). This method gives you a number that represents the day of the week. From there, you can use another function to turn that number into the day's name. <ChartCategoryAxisLabels Template="#=dayOfWeekAsString(new Date(value).getDay())#"> </ChartCategoryAxisLabels> <script suppress-error="BL9992"> window.dayOfWeekAsString=( dayIndex )=> { return [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ][dayIndex] || ''; } </script> To demonstrate the approach I've prepared a REPL example: [https://blazorrepl.telerik.com/QxYJvzOz54qUSfbt36](https://blazorrepl.telerik.com/QxYJvzOz54qUSfbt36) I hope this helps. Regards, Yanislav Progress Telerik
