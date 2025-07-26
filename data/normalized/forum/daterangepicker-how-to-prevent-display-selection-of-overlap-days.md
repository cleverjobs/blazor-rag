# DateRangePicker: How to prevent display/selection of "overlap" days?

## Question

**Tec** asked on 19 Apr 2022

Hi, The date range picker confusingly displays and selects days from different months multiple times. Our users (and we developers) find this very confusing and unnatural: How can we turn off this behavior so that each month displays JUST the dates IN THAT MONTH and no other days? Thanks!

### Response

**Joana** commented on 22 Apr 2022

Hi, Thank you for sharing your feedback. Currently, you can hide the dates from the other month through css. I have prepared a REPL snippet demonstating the customization: [https://blazorrepl.telerik.com/cmaSGcYA52zS12pu28.test](https://blazorrepl.telerik.com/cmaSGcYA52zS12pu28.test) .k-other-month {
visibility: hidden;
} However, I understand that it is beneficial to expose a setting for this behavior and revise the default rendering. That is why I logged a feature request on your behalf so that we look into the issue in more details: [https://feedback.telerik.com/blazor/1562492](https://feedback.telerik.com/blazor/1562492)
