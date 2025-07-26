# Scheduler - Multiday All-Day Rows Only with Grouping

## Question

**Pau** asked on 13 Aug 2022

Hello, I am looking to show create a multiday scheduler view (with resource grouping) that only displays the all day events. Without grouping, adding the css rule .k-scheduler-group:not(.k-scheduler-all-day-row){ display: none; } works to remove the non-all day rows, but once grouping is introduced I haven't been able to find a way to make this work. Please advise - a demo photo has been attached.

## Answer

**Nadezhda Tacheva** answered on 17 Aug 2022

Hello Paul, Generally speaking, such CSS modifications could be tricky as they may result in breaking the component rendering. I would recommend another approach - using the Timeline View. You can make some view configurations to get the desired result. Additionally, you can alter the data shown in this view to display only the all-day appointments. The result will look like this: [https://blazorrepl.telerik.com/QwOsvLbL10qyVCBk48.](https://blazorrepl.telerik.com/QwOsvLbL10qyVCBk48.) Please consider and let me know your thoughts. I look forward to hearing from you! Regards, Nadezhda Tacheva Progress Telerik

### Response

**Paul** commented on 18 Aug 2022

This looks like it will do the trick! Thank you.

### Response

**Chinmay** commented on 10 Feb 2023

Thanks I am looking for the similar solution.
