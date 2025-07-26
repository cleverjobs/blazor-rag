# Use ICS data in scheduler?

## Question

**Tin** asked on 27 May 2020

Hi, I'm playing with the Telerik Blazor components. Is there a way to use the scheduler with ics data? Thanks Martin

## Answer

**Svetoslav Dimitrov** answered on 29 May 2020

Hello Martin, We do not provide built-in support for the ICS files. That being said, the Data parameter we provide with the Scheduler can work with any type of data so you can cast your iCalendar appointments using a custom tool like [https://gist.github.com/nozzlegear/0d42673f64e5c9a9862a](https://gist.github.com/nozzlegear/0d42673f64e5c9a9862a) to JSON, in this example, or a C# model and use it for the Scheduler. Regards, Svetoslav Dimitrov

### Response

**Tinus** answered on 29 May 2020

Thanks Svetoslav, can you please add ICS support (import/export) in a later version (feature request). Thanks Martin

### Response

**Svetoslav Dimitrov** answered on 03 Jun 2020

Hello Martin, We have created a demo project to showcase how to create a custom ICS data converter. You can see it from here: [https://github.com/telerik/blazor-ui/tree/master/scheduler/ICS-data-convertion.](https://github.com/telerik/blazor-ui/tree/master/scheduler/ICS-data-convertion.) Regards, Svetoslav Dimitrov

### Response

**Tinus** answered on 04 Jun 2020

Thanks, will look into it. Martin
