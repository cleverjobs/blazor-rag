# Grid's virtual scrolling doesn't work past 559,240 rows

## Question

**Joh** asked on 28 Apr 2023

I've created a sample REPL to demonstrate the issue: [https://blazorrepl.telerik.com/mHaSmsvW31IZ0rar47](https://blazorrepl.telerik.com/mHaSmsvW31IZ0rar47) In Grid.OnRead event handler, if you set args.Total to an amount> 559240, then the Grid will only scroll to 559240. In my example, I used 1,000,000 for my virtual data source size.

## Answer

**Dimo** answered on 28 Apr 2023

Hi John, I think you are hitting the CSS limit for maximum possible element height. If possible, use a smaller row height and override the theme to apply smaller vertical cell paddings. If that's not enough to reach the last row, you will have to apply some default filtering, so that the total number of items (and resulting scrollable height) is smaller. <TelerikGrid Class="smaller-padding" /> <style>.smaller-padding.k-master-row.k-table-td { padding: 0 8px;
} </style> Regards, Dimo Progress Telerik

### Response

**John** commented on 28 Apr 2023

Thank you Dimo - that was it! I set RowHeight to 30, and used your smaller-padding CSS and was able to get to 1 million virtual rows.
