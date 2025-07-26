# DateTimePicker Set Dates

## Question

**con** asked on 14 Jun 2020

How can I fill DateTimePicker with specific dates and times (say based on List<T>)?

## Answer

**Marin Bratanov** answered on 14 Jun 2020

Hello, You can pre-set the time by setting the Value field. As for controlling the list of options in the dropdown - you can Follow its implementation in this page: [https://feedback.telerik.com/blazor/1451572-time-intervals-larger-than-second.](https://feedback.telerik.com/blazor/1451572-time-intervals-larger-than-second.) If you have a proposition or request how that should work, post it there for everyone to see, comment and vote on, and so the dev team can take it into account when working on it. Regards, Marin Bratanov

### Response

**const** answered on 15 Jun 2020

Case: MyMeetingsManager - the Application which is used to manage my meetings. When I'm scheduling a new meeting I would like to pick dates/times which are not used for already scheduled meetings. This is an example of functionality which I would be happy to have for DateTimePicker: <TelerikDateTimePicker Dates="@myDates"></TelerikDateTimePicker> @code{ private List<DatesModel> myDates; protected override async Task OnInitializedAsync() { //populating from call to database myDates=await _db.GetDates(); } } //this is how the model looks like public class DatesModel { public datetime dat { get; set; } } You have similar functionality available for DatePicker "disabledDates". Thank you

### Response

**Marin Bratanov** answered on 15 Jun 2020

Hi, The following sample project shows how you can do this: [https://github.com/telerik/blazor-ui/tree/master/calendar/allowed-dates](https://github.com/telerik/blazor-ui/tree/master/calendar/allowed-dates) Regards, Marin Bratanov

### Response

**const** answered on 15 Jun 2020

Actually I was asking about DateTime not just Date info. Calendar as well as DatePicker (where "disabledDates" feature is represented for) are dealing with dates but I need similar functionality which would work with both Date&Time. Say, if I'm filling the Element with '2020-06-15 11:30:00:000', the only date and the only time I want to allow User to pick are 06 Jun, 2020 and 11:30AM. Thank you

### Response

**Marin Bratanov** answered on 15 Jun 2020

Both the Calendar and the DatePicker have DisabledDates and they take DateTime objects. When this gets implemented, you will be able to control what options the time portions of the time pickers show. Further logic to prevent the user from writing something in the input that you disallow should be handled through forms validation, the OnChange or ValueChanged event by the app. You can also use the Min and Max to set the earliest and latest dates the user can select. Once they get improved to also work for the time (see here ), when the time portions between the Min and Max only allow a few hours, and your format does not display seconds, you can quite limit the user from selecting dates and times. A built-in EnabledDates or Times parameter is very unlikely to become a feature of the component, because having such a short list that it can be enumerated like that indicates a significant limitation for the user input, so that should either be done through events and/or forms validation, or you could simply generate a few options for a simple dropdownlist and let the user pick those. That said, how would you imagine a DisabledDates feature to work for a time picker, considering that each date can have all the possible time slots? Would limiting the time portions through Min and Max (and/or maybe a MinTime MaxTime, if need be) work out for you? Regards, Marin Bratanov

### Response

**const** answered on 15 Jun 2020

Unfortunately, Mix/Max feature isn't working for my purpose. I understand the complexity of what I'm asking about. Apparently, in your DateTimePicker (DTP) you are dealing with a separate, independent of each other scopes of information: Date and Time. So, when you are populating DTP with values somewhere on background, you are supplying a set of Dates for Date part of DTP and another set of Times for Times part of one. This absolutely does make sense for most of cases but is not gonna work for my one. Anyway thank you for nice discussion.

### Response

**Marin Bratanov** answered on 15 Jun 2020

The DateTimePicker is basically two components tied together - a calendar (date picker) that shows months, for example, and a time picker that shows hours, minutes and seconds. The calendar is always Gregorian so there isn't much to control there (although perhaps DisabledDates might be exposed), and the time picker can mostly benefit from a way to choose the intervals through which it generates entries in the spinners. That said, if you want to limit and control things in more detail, a simple DateInput will let you handle the ValueCHanged and OnChange events for full control over the values, and perhaps a simple dropdownlist will let you provide a few points in time that you want available. Regards, Marin Bratanov
