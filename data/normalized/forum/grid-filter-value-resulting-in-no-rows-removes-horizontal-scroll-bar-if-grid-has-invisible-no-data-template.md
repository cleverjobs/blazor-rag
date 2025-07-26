# Grid filter value resulting in no rows removes horizontal scroll bar if grid has invisible no data template

## Question

**Cla** asked on 27 Jun 2023

I have a grid with horizontal scroll, row filter, and invisible no data template (done via css class) as requirement. Note: if i use NoDataTemplate element as follow, it create an empty row <NoDataTemplate> <div> </div> </NoDataTemplate> but i need no rows if the result is empty, so i managed via css with: .hide-no-data-template .k-grid-norecords {
display: none;
} <TelerikGrid... Class="hide-no-data-template"></TelerikGrid> having a grid with no row and no template for empty result create the issue. If i filter a column with the scrollbar shifted and the result produce at least one row, i show correcly the result Now, if i change the filter obtaining no row result the grid is correcly empty and horizontal scrollbar disappear Now, if i restore the previous filter, obtaining at least one row, the result is correct, but horizontal scrollbar is positioned at start position, and column data does not match column filters you can reply the issue with this code: [https://blazorrepl.telerik.com/mHYKGhPy15rgDbLM16](https://blazorrepl.telerik.com/mHYKGhPy15rgDbLM16) Related issues: [https://www.telerik.com/forums/grid-filter-value-resulting-in-no-rows-removes-horizontal-scroll-bar](https://www.telerik.com/forums/grid-filter-value-resulting-in-no-rows-removes-horizontal-scroll-bar) [https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered?_ga=2.196089516.1410422363.1687873194-1919299615.1685452956&_gl=1*1f4kvho*_ga*MTkxOTI5OTYxNS4xNjg1NDUyOTU2*_ga_9JSNBCSF54*MTY4Nzg3MzE5NC4xNC4xLjE2ODc4NzU0MjkuNC4wLjA.](https://feedback.telerik.com/blazor/1451961-grid-horizontal-scroll-is-disabled-when-no-data-items-are-rendered?_ga=2.196089516.1410422363.1687873194-1919299615.1685452956&_gl=1*1f4kvho*_ga*MTkxOTI5OTYxNS4xNjg1NDUyOTU2*_ga_9JSNBCSF54*MTY4Nzg3MzE5NC4xNC4xLjE2ODc4NzU0MjkuNC4wLjA.)

### Response

**Claudio** commented on 28 Jun 2023

I currently solved the issue with this css: .hide-no-data-template .k-grid-norecords .k-table-td {
padding: 1px;
font-size: 0;
} it still show a row of no-data-template but is 1px height, if i set to 0 the scrollbar disappear. It would be great to have a solution who hide completely the no-data-template row.

### Response

**Yanislav** commented on 30 Jun 2023

Hello Claudio, Scrolling is a feature that enables users to access content beyond the visible area of an element. For scrolling to work, the element must contain content that exceeds its dimensions. With the following CSS rule: <style>.hide-no-data-template.k-grid-norecords { display: none;
} </style> The content of an empty Grid is no longer visible. Therefore, there is no element that exceeds the dimensions of the Grid, and as a result, the scrollbar is not displayed. However, the Grid headers are still shown, but in general, they are scrolled when the body is scrolled. Since the body is hidden, the headers cannot be scrolled. That being said, the solution you've shared seems like the best option if you do not want to display anything when there is no data in the Grid while still allowing the user to scroll both the body and the headers. I trust that this provides clarity regarding the situation. If you have any specific suggestions on how this scenario could be enhanced, and how the Grid should behave please feel free to share them without hesitation.
