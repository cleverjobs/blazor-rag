# Empty row at the bottom of the calendar

## Question

**Rya** asked on 30 Sep 2019

What is the empty row at the bottom of the calendar? Is there a way to remove it?

## Answer

**Marin Bratanov** answered on 01 Oct 2019

Hi Ryan, It is needed for some months that span 6 weeks. For example, if the 1st is on a Saturday, and the month has 31 days, there will be a day on the last row that is currently empty. It may also start showing dates from the next month once we implement that, so the user has a little more context. That said, you can remove this last row and shorten the calendar by doing something like this (but there is a slight risk to hide a couple of days at the end of a peculiar month): <style>.k-content.k-calendar-content.k-month tbody tr:last-of-type { display:none;
}.k-calendar div.k-calendar-view { height: 15em;
}
</style>

<TelerikCalendar></TelerikCalendar> Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 19 Dec 2019

For anyone experiencing this - there is now a feature request for implementing the next/prev month dates in the current month view that you can Follow here: [https://feedback.telerik.com/blazor/1446687-empty-row-at-the-bottom-of-the-calendar-should-show-the-next-month.](https://feedback.telerik.com/blazor/1446687-empty-row-at-the-bottom-of-the-calendar-should-show-the-next-month.) --Marin
