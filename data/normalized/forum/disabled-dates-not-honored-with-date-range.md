# Disabled Dates not honored with date range

## Question

**Ric** asked on 05 Sep 2024

Using the following example: [https://blazorrepl.telerik.com/mIODuTlt02gFnIYp00](https://blazorrepl.telerik.com/mIODuTlt02gFnIYp00) What I am trying to accomplish is the following: I want the user to be able to pick a start date and end date using the range selector, if there are disabled dates between the range, the range should not be accepted since one or more of the dates are disabled.

## Answer

**Dimo** answered on 05 Sep 2024

Hello Ricky, Use the RangeStart and RangeEnd parameters together with their respective ... Changed handlers. This will allow you to: know what the user is selecting check if the selection meets your criteria and if not, override the RangeStart and RangeEnd parameter values notify the user Regards, Dimo Progress Telerik
