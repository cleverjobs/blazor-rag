# When the TelerikTimePicker is cleared, the input is marked as invalid, even if the backing variable isn't required

## Question

**And** asked on 05 May 2025

I have a TelerikTimePicker component and I have set the ShowClearButton="true". The Value property of the component is bound to a nullable DateTime variable (e.g., DateTime? MyTime). If I first input/select a valid time and then clear the value (using the "x" button in the input field), the component is highlighted in red because the .k-invalid class has been added to the HTML markup. However, the value in the TelerikTimePicker is not actually invalid because a null value is allowed. This is very similar to this issue for the TelerikDateTimePicker: [https://feedback.telerik.com/blazor/1660917-datetimepicker-should-not-get-red-border-when-bound-to-nullable-datetime-and-the-input-is-empty](https://feedback.telerik.com/blazor/1660917-datetimepicker-should-not-get-red-border-when-bound-to-nullable-datetime-and-the-input-is-empty)

## Answer

**Dimo** answered on 08 May 2025

Hi Andrew, Yes, the issue is the same, and the suggested workaround is the same. I hope it's not too much work to apply it everywhere where needed. Regards, Dimo Progress Telerik
