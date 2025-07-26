# Grid filter value resulting in no rows removes horizontal scroll bar

## Question

**Dou** asked on 23 Mar 2021

If you have a filterable grid whose width is limited, and you have a lot of columns, the horizontal scroll bar shows up correctly. If you scroll to the right and enter a value in a column filter which results in no rows being displayed, the grid scrolls back to the left, displaying the first column again and hiding the filtered column, and the scroll bar disappears so you can't get back to the column with the filter so you're stuck. You can't get back to the filtered column to remove the filter. Any way to avoid this?

## Answer

**Marin Bratanov** answered on 24 Mar 2021

Hello Doug, You can Follow the fix for this here: [https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered.](https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered.) The thread offers a couple of workarounds you can consider as well. Regards, Marin Bratanov Progress Telerik

### Response

**Doug** answered on 24 Mar 2021

Thanks Marin. I keep forgetting to check the

### Response

**Claudio** answered on 19 Jun 2023

Hi, i have an related issue, i added a comment on [https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered](https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered) I have a grid with horizontal scroll, row filter, and invisible no data template as requirement. If i filter a column with the scrollbar shifted and the result produce at least one row, i show correcly the result Now, if i change the filter obtaining no row result the grid is correcly empty and horizontal scrollbar disappear Now, if i restore the previous filter, obtaining at least one row, the result is correct, but horizontal scrollbar is positioned at start position, and column data does not match column filters In the link on feedbackportal i added some pictures to better explain the issue. How to solve? Thanks

### Response

**Nadezhda Tacheva** answered on 22 Jun 2023

Hello Claudio, I am testing the scenario but I am not able to reproduce such a behavior. You can check it yourself here: [https://blazorrepl.telerik.com/QxuKcGai270IFMd716.](https://blazorrepl.telerik.com/QxuKcGai270IFMd716.) My advice will be similar to what my colleague shared in the
