# TelerikCalendar / MonthCellTemplate - should not show the month "overhang"

## Question

**Pet** asked on 04 Apr 2023

I'm currently working on a multiview calendar. However, I've come across an issue that confuses the user quite a bit. If I allow a selection that goes beyond the boundaries of a single month, then the overflow from the next or previous month is also selected and displayed. This results in the question: "Is it possible to disable the display of overflow from the next or previous month?" In the template, I don't have any information in the context about which month the multiview is displaying, otherwise it would be easy to deactivate the context. The question is, can the calendar be configured to simply not display overflow from other months? For Display this is not a Problem, I override .k-other-month, so the overhang is not visible. But how to solve this in a Multiview Selection?

## Answer

**Dimo** answered on 06 Apr 2023

Hello Peter, It seems that the current CSS override for .k-other-month is not optimal. Use this: <TelerikCalendar Views="3" SelectionMode="@CalendarSelectionMode.Multiple" Class="no-other-month-days" /> <style>.no-other-month-days.k-other-month.k-link { visibility: hidden;
} </style> Regards, Dimo Progress Telerik

### Response

**Peter** commented on 06 Apr 2023

Yes, thanks for removing tomatos from my eyes. That did it! Happy Easter to you and your colleagues! Thank you for the help!

### Response

**Dimo** commented on 06 Apr 2023

:))) Thanks, happy holiday to you too!
