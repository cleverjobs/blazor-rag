# ui for blazor Timepicker

## Question

**kha** asked on 02 Jan 2020

hello, i wanted to know if returned value of Timepicker could be timespan or not ?

## Answer

**Kristian** answered on 02 Jan 2020

Hello Khashayar, I found a similar thread where we discuss with you how you can extract Timespan from DateTimePicker, Timepicker and other similar components in Telerik UI for Blazor - [https://www.telerik.com/forums/telerikdatepicker-in-blazor](https://www.telerik.com/forums/telerikdatepicker-in-blazor) You can read it and get back to me if you have any additional questions. Regards, Kristian

### Response

**khashayar** answered on 05 Jan 2020

yes thanks but would'nt it be better if TimePickerrequired TimeSpan object instead of DateTime ?

### Response

**Marin Bratanov** answered on 06 Jan 2020

Hello, The TimeSpan structure represents a time interval ( MSDN link ), while a single picker represents one fixed point in time, so it could not give you a TimeSpan. You need to have some business logic that determines that other end of that interval, the picker can't do it on its own. Perhaps a range picker would be able to provide a TimeSpan and you can follow its implementation in the following page: [https://feedback.telerik.com/blazor/1446213-daterangepicker.](https://feedback.telerik.com/blazor/1446213-daterangepicker.) I would encourage you to add a comment with the scenario you have and why it is needed that the picker provides a TimeSpan since you will be able to calculate it from its Start and End dates easily. When we have that information the dev team could consider it when implementing the component. Regards, Marin Bratanov
