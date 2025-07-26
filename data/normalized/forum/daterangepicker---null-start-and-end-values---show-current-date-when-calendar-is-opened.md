# DateRangePicker - Null Start and End Values - Show Current Date When Calendar Is Opened

## Question

**Vad** asked on 18 Jul 2022

Hello I am implementing DateRangePicker with null start and end date. When user open calendar he sees Min date instead of current date. How can I move the focus from the Min date to the current date at the time the calendar is opened?

## Answer

**Hristian Stefanov** answered on 21 Jul 2022

Hi Vadzim, Let me shed some light on the expected behavior in the situation below. The DateRangePicker provides a time range calculated from two DateTime variables ( Start and End ). The initial focus is always on the Start date because, in most cases, the customer starts their time range from there. If the Start date is not specified, the DateRangePicker component cannot know where exactly the user wants to start. In such a case, the component knows only the specified Min and Max values and needs to choose which to put the focus on. Thus, the initial focus goes on the Min as it makes more sense. If the Min and Max are null as well, the initial focus is on the default Min date. To put the initial focus on the current date, set the Start date to the current date. I hope you find the above information helpful. If we can help with more, I would be glad. Regards, Hristian Stefanov Progress Telerik

### Response

**Vadzim** commented on 16 Aug 2022

Hi Christian! Thanks for the response. Let I try to describe my case in more details. I have a DateRangePicker as a grid column filter. When a user open grid in the first time values for date range were not selected. In this case input fields are empty, filter was not applied and user sees all values in the grid. But when he/she clicks on the date range input the user would like to see current date as selected in the popup or current week without selected date instead of the min date . Do we have an ability to focus on the current date or shift to current week when popup is appearing?

### Response

**Joana** commented on 19 Aug 2022

Hi Vadzim, Indeed, currently there is no way to customize the default focused date within our Calendar integrated in the DateRangePicker. I have logged a feature request on your behalf: [https://feedback.telerik.com/blazor/1576761](https://feedback.telerik.com/blazor/1576761)
