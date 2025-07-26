# Date Picker Preview event?

## Question

**Azt** asked on 30 Nov 2021

After selecting a date from the calendar control, control goes to the field with the date value but doesn't fire the OnChanged event until after an action draws focus away. Is there a event that I can hook into at this state (after the selection and before the OnChanged event)? I need update the page when the visible date in the field is different and OnChanged is firing too late because of this preview. I've looked into using ValueChanged but haven't been able to pre-set the value.

### Response

**Dimo** commented on 01 Dec 2021

The ValueChanged event should do the job, because it fires immediately after date selection in the Calendar popup and before the DatePicker is blurred. Can you explain what do you mean by "haven't been able to pre-set the value"?
