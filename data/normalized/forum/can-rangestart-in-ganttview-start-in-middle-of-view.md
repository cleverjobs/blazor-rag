# Can RangeStart in GanttView start in middle of view?

## Question

**Den** asked on 02 Sep 2021

If I change the RangeStart to for example 1 August 2021 in the GanttYearView, the GanttYearView still starts at 1 January 2021 which gives a lot of white noise:

## Answer

**Nadezhda Tacheva** answered on 06 Sep 2021

Hi Dennis, This is the default behavior of the Gantt component in terms of its Timeline views. Different views provide different time slots (see Timeline Views article for details ). Once you set the desired date for the RangeStart parameter, the Gantt will take the part of the date that corresponds to the view along with that view's slot. As per your current question, let me first cover the Year view. If, for example, in the Gantt Year view the RangeStart is set to 1 August 2021, the component will take the year 2021 and the view will display the beginning of this year in month-long slots as per the Year view setup. In the Month view the Timeline will display the beginning of the month defined for the RangeStart parameter in a week-long slots. Same behavior is applied for the Week and Day views. You can also test it in the Gantt Views live demo. I hope you will find this information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
