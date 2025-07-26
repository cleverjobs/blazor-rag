# I want to be able to group by date and sort by date/time

## Question

**Gle** asked on 24 Apr 2024

Here is my sample. [https://blazorrepl.telerik.com/wIYIwokW39rcHMFE31](https://blazorrepl.telerik.com/wIYIwokW39rcHMFE31) Can you help please?

## Answer

**Dimo** answered on 25 Apr 2024

Hello Glendys, There are two ways to achieve the desired behavior: Bind the Grid with OnRead and implement your own custom data operations. OR Use two model class properties - one with date only and one with date/time. When the user groups by the date/time property, switch the grouping to be on the date-only property and update the Grid state. You will also need a GroupHeaderTemplate for the date-only column, in order to render the date/time column title. Here is a REPL example: [https://blazorrepl.telerik.com/GoaScfbz43JHYuzT11](https://blazorrepl.telerik.com/GoaScfbz43JHYuzT11) If you need to group programatically, the task is even easier, because you won't need OnStateChanged. Regards, Dimo Progress Telerik
