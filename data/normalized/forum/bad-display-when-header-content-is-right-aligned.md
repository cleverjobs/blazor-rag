# Bad display when header content is right aligned

## Question

**Pat** asked on 20 May 2020

Hello, As you can see with the attached screenshot, the filter icon is over the header text in this case.

## Answer

**Marin Bratanov** answered on 20 May 2020

Hi Patrick, Could you try the workaround from this page: [https://feedback.telerik.com/blazor/1462727-filter-icon-overlapping-the-column-header-text?](https://feedback.telerik.com/blazor/1462727-filter-icon-overlapping-the-column-header-text?) Regards, Marin Bratanov

### Response

**Patrick** answered on 20 May 2020

Hi Marin, I've tried, but the result is the same...

### Response

**Marin Bratanov** answered on 20 May 2020

Hello Patrick, If you are customizing the header through a template, the grid can no longer take care of the styling so the template must ensure it does not overlap the filter icon. You can read details on that particular situation here: [https://docs.telerik.com/blazor-ui/components/grid/templates#header-template](https://docs.telerik.com/blazor-ui/components/grid/templates#header-template) Regards, Marin Bratanov

### Response

**Patrick** answered on 20 May 2020

Hi Marin, Is there a way to define a right aligned header without a template? The column is defined as: <GridColumn Field="Duration" Width="120px"> <HeaderTemplate> <div style="text-align: right"> @Text("RequestsLog.Header.Duration") </div> </HeaderTemplate> <Template> <div style="text-align: right"> @((context as RequestLogEntry).Duration.TotalMilliseconds.ToString("#,##0") + "ms") </div> </Template> </GridColumn>

### Response

**Marin Bratanov** answered on 20 May 2020

Hi Patrick, For your convenience I made two examples, and you can find them attached at the end of this post, together with screenshots of the results: one with header templates for specific columns one with CSS for all columns Both use the workaround from the first page I linked and avoid the overlap through it. Regards, Marin Bratanov

### Response

**Patrick** answered on 20 May 2020

Hi Marin, It works... unless the text of the column is too long (or the column is not wide enough. In this case, there is still an overlap.

### Response

**Patrick** answered on 20 May 2020

It would be much more simpler, if you add HeaderTextAlignment and TextAlignment properties to the Grid.

### Response

**Marin Bratanov** answered on 20 May 2020

Hi Patick, You can Follow and Vote for that here: [https://feedback.telerik.com/blazor/1431848-grid-column-header-and-content-alignment-horizontal-vertical.](https://feedback.telerik.com/blazor/1431848-grid-column-header-and-content-alignment-horizontal-vertical.) It will not fix the situation where the header text is too long for the column width, of course, as that would be basically the same CSS rule. At one point there is no solution for that when the column width becomes smaller than the word width. Regards, Marin Bratanov
