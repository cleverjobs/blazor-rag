# Syncing initial calendar view to min date

## Question

**Nei** asked on 07 Apr 2021

Is it possible to sync the initial calendar view to min date? I've set min to DateTime.Now.AddDays(30) but when I click the calendar it defaults to showing the month of April, with April 7th highlighted. This confuses the user as they try clicking various dates in April.

## Answer

**Marin Bratanov** answered on 09 Apr 2021

Hello Neil, To set the current date (month, year, decade) the user starts in the calendar, set its Date parameter to the desired date. You can find more details and example in the documentation about calendar nagivation: [https://docs.telerik.com/blazor-ui/components/calendar/navigation](https://docs.telerik.com/blazor-ui/components/calendar/navigation) Here's also an example that starts the calendar in the min date because the Date and Min parameters have the same value: <TelerikCalendar @bind-Date="@startDate" Min="@minDate" Max="@maxDate"></TelerikCalendar>
@code {
DateTime startDate=DateTime.Now.AddDays( -30 ); DateTime minDate=DateTime.Now.AddDays( -30 ); DateTime maxDate=DateTime.Now.AddDays( 230 );
} Regards, Marin Bratanov Progress Telerik

### Response

**Neil N** answered on 12 Apr 2021

I am using the DatePicker component, not the Calendar, as I need to accept null dates.

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hi Neil, How would you expect a picker to expose this, considering a few factors: unlike the calendar, its calendar is not always visible, so it will re-render from scratch every time it opens unlike the calendar, the date it shows is bound to it like an input - through @bind-Value - and this is its main driving parameter, it is, first and foremost, an input - in the calendar the date selection is a separate feature which is not the primary display of the component there is a default min date that is about a century ago, and for most people and use cases that's too far back in time to be useful The popup calendar in Windows has the same behavior - whatever you scroll to, when you close and open it again it starts in the month with Today's date. Regards, Marin Bratanov Progress Telerik

### Response

**Neil N** answered on 13 Apr 2021

Hi Marin, The current behaviour is: if date is set, show month of set date else show month of current date (today) Desired behaviour: if date is set, show month of set date else if min date's month is greater than current date month then show month of min date else show month of current date The Windows popup calendar is not for date input, nor is there a way to set a min date for it. I'm trying to create a UX which isn't user hostile. If the min date is six months in the future (for example), it's not very user-friendly to scroll through six months if they want to set a date.

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hello Neil, If the min date is not near the current date, then you can consider setting the Value to the min date and checking if that changed in the business logic to indicate whether the user made a choice or not. The Value is the main driver of this component and it determines what the user sees. How else would you like to see this configured? What about other cases where the min date is not larger than the current date? What about people who'd rather start near today's date? How should the component accommodate those scenarios? Regards, Marin Bratanov

### Response

**Neil N** answered on 13 Apr 2021

70% of users will not want to set a date - it will only confuse them if they see a date set for them. What about other cases where the min date is not larger than the current date? Answered above: * else if min date's month is greater than current date month then show month of min date * else show month of current date What about people who'd rather start near today's date? Can you please explain how defaulting to showing unpickable dates in a datepicker is a good UX?

### Response

**Neil N** answered on 13 Apr 2021

I had a look at ASP.NET AJAX datepicker and it looks like it has this functionality: RadDatePicker1.FocusedDate=DateTime.Today.AddDays(30);

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hello Neil, I made the following enhancement request on your behalf where you can Follow the status of this idea: [https://feedback.telerik.com/blazor/1515267-set-focused-initial-date-that-is-different-than-the-value.](https://feedback.telerik.com/blazor/1515267-set-focused-initial-date-that-is-different-than-the-value.) If it gets sufficient traction with the community, its implementation will be prioritized by management. Regards, Marin Bratanov

### Response

**Neil N** answered on 13 Apr 2021

Thank you.
