# Blazor TelerikDatePicker ReadOnly parameter allows arrow keys to change date.

## Question

**Way** asked on 10 Aug 2023

Telerik.UI.for.Blazor Version=4.4.0 When TelerikDatePicker ReadOnly parameter is set to true, arrow keys can still be used to increment date values. For example with the year portion of a date selected one can press the up and down keys to increment and decrement the year. Typing a numeric value is prevented and the calendar popup is also prevented and functions as expected. I did a check to see that the rendered input tag contains the readonly attribute, it is there. Looks like the arrow keys are handled outside of normal input tag behavior. I have not checked the TelerikDateTimePicker or related components, but they may have the same issue.

## Answer

**Yanislav** answered on 11 Aug 2023

Hello Wayne, As we have discussed, the reported behavior is indeed incorrect and not intended. I have taken the initiative to log a feedback portal item on your behalf and am sharing the link to the feedback portal item in case anyone comes across our discussion here on the forum: [https://feedback.telerik.com/blazor/1619607-value-modifications-with-the-arrow-keys-should-be-prevented-when-readonly-true](https://feedback.telerik.com/blazor/1619607-value-modifications-with-the-arrow-keys-should-be-prevented-when-readonly-true) In the meantime, if we discover a possible workaround, we will promptly post it as a comment in the public post linked above. Regards, Yanislav Progress Telerik
