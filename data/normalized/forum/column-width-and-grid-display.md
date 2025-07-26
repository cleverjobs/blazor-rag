# Column width and grid display

## Question

**Ste** asked on 27 Nov 2020

I've hardcoded every column's width, still when the grid loads it'll span to the whole page's width. I expand the browser window, the grid grows with it. When I manually resize one of the column, the grid starts behaving like expected and stops growing with the window but it'll keep the arbitrary column sizes from start up (the the ones I coded). The only way I could get out of this was to set the width of the grid itself. But now if I expend a column manually, I'm getting a scrollbar because the width is limited. At render the grid is enclosed in div with "k-grid k-widget telerik-blazor" class. I tried messing with those a little with no avail. I need the grid to appear as an inline block, with a total width that amounts to the sum of the columns widths I hardcoded.... Any help appreciated. Thanks

## Answer

**Marin Bratanov** answered on 27 Nov 2020

Hello, I advise you first review the following article on how column widths behave: [https://docs.telerik.com/blazor-ui/components/grid/columns/width](https://docs.telerik.com/blazor-ui/components/grid/columns/width) The key thing is that the grid has table-layout:fixed, and its main wrapping element is a div (which has, by default, width: auto), so it will behave like the corresponding HTML elements with those CSS rules. Then, you should take a look at the following Knowledge Base article on a similar issue caused by Bootstrap layouts and display:flex with table-layout:fixed: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue.) Generally, our components fit in a layout, they don't create it. If you want the grid to have a certain width, either make its parent element have the desired dimensions and set the grid's Width and Height parameters to 100%, or directly set the desired dimensions to the grid. You can read more about setting sizes on the Telerik components here: [https://docs.telerik.com/blazor-ui/common-features/dimensions.](https://docs.telerik.com/blazor-ui/common-features/dimensions.) Regards, Marin Bratanov

### Response

**Stephane** answered on 28 Nov 2020

<div class="d-flex flex-row"> <div class="p-3 border"> <TelerikGrid Data="@MyData" Height="400px" Pageable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" Width="120px" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" Width="120px" /> </GridColumns> </TelerikGrid> </div> <div class="p-3 border">Div2</div> <div class="p-3 border">Div3</div> </div> @code { public IEnumerable<SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData { Id=x, Name="name " + x, Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } } Img 1: at startup, the grid expands the div included in a flex container to full width with no consideration to the fixed comlumn widths. Img 2: The browser is resized smaller (the grid shrinks). One column is resized manually. If a column was not resized manually, the grid would expand again with the browser resize. The browser is resized to the original size, the grid stops expanding with the browser. It will expand/shrink with a column resize. This is the behavior I'm looking for at start up without having to hardcode the grid's width. In any case, from what I observed, if the grid's width is not fixed (hardcoded), the columns width are never respected. Or I'm simply missing something...

### Response

**Marin Bratanov** answered on 30 Nov 2020

This looks like the issue from the KB article I linked: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bootstrap-flex-width-issue) If the information from it does not help, please open a support ticket and send us a simple runnable example that shows the Telerik issue. Regards, Marin Bratanov

### Response

**Peili** answered on 15 Jan 2024

For anyone interested in this, an workaround seems to be set width for all your columns, and add an empty column in the end. Thus this empty column in the end will expand if the container is wider than the grid itself.

### Response

**Hristian Stefanov** commented on 17 Jan 2024

Hi Peili, Thank you for sharing what is working for you. This can be helpful for other developers. Kind Regards, Hristian
