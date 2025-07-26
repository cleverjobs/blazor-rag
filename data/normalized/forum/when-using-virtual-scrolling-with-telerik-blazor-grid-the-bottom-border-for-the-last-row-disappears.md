# When using virtual scrolling with Telerik Blazor Grid the bottom border for the last row disappears.

## Question

**Jas** asked on 23 Sep 2022

I created my application using ASP.NET Core Blazor. I am using the Bootstrap Template. I investigated the CSS that is being generated and the class element is as shown below in the html snippet: <tr role="row" class="k-master-row " I am trying to do conditional formatting of cells. The cell is highlighting correctly. I am using this sample to do that [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background?&_ga=2.240489920.275428779.1663859668-574397901.1663859668#css-only-approach](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background?&_ga=2.240489920.275428779.1663859668-574397901.1663859668#css-only-approach) I am using the first approach OnCellRender with OnRowRender. It only happens if there is one row. My Grid is set to a height of 900 px and the row height is 60 and I am using virtual scrolling only for rows and not columns.

## Answer

**Svetoslav Dimitrov** answered on 28 Sep 2022

Hello Jason, The last row of the Grid does not have a border by design. We have placed an explicit CSS rule that removes the border for the last row. In cases where the Grid has enough rows to fill the entire table the border of the last row will create an overlap with the rendering of the footer. If you want to handle this scenario I would suggest you add override of our CSS rule: k-grid- content tr:last-child> td,.k-grid-content-locked tr:last-child> td { border-bottom-width: 0 } Regards, Svetoslav Dimitrov Progress Telerik
