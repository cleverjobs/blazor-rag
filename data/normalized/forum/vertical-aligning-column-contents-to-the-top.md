# Vertical Aligning Column Contents to the top

## Question

**aeh** asked on 23 Apr 2021

So...what's the secret? I have a couple of columns in the grid with a ton of data and I want the contents of the cells with less text to be aligned to the top. I have no issues doing this in a web forms app, but for the life of me, I cannot get it to behave in blazor.

## Answer

**Marin Bratanov** answered on 26 Apr 2021

Hi, You can use the CellRender event to add a CSS class to such cells and then a bit of CSS to produce the desired vertical-align setting (note that the selector has to be heavier than the one that comes from the grid theme). You may find this blog post useful in reviewing the applied CSS rules. <style>
.k-grid td.vertical-aligned-cell {
vertical-align: top;
}
</style> <TelerikGrid Data="@MyData" Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true" RowHeight="100">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code { public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov Progress Telerik

### Response

**aehlert** commented on 27 Apr 2021

Thanks for the reply. I have found trying to format grids a complete horrible chore. Can we please have a good example of css that can be applied to the grid that: 1. Allows us to define the header, e.g. : set the text to the cell center, aligned to the bottom, of X - color, and x - font size. 2. define the cell elements with the same types of values. 3. Set the footer styles The styling for these blazor components is very underwhelming right now. Is there a block of styles that will allow you to define how the grids appear?

### Response

**Marin Bratanov** commented on 28 Apr 2021

The grids for Blazor are styled according to modern web standards - adding CSS rules with high enough specificity to override the built-in behavior is the correct way to do this. There are some more examples of this here. You may also want to Vote for and Follow this feature to see whether specific parameters will be exposed for that and how it will be implemented. To answer each individual question: 1. Allows us to define the header, e.g. : set the text to the cell center, aligned to the bottom, of X - color, and x - font size. You can use the Title parameter of the column or the Header template for this. If you want to add special styling per column, the header template will serve you better. If you want to affect all headers in a grid - a few CSS rules are the way to go. 2. define the cell elements with the same types of values. The cell template or the CellRender event are the ways to do this. 3. Set the footer styles The footer template and group footer template are the way to do this. Generally, Blazor is very much template-driven when you want to customize content and layouts, much more so than WebForms. Thus, there cannot be a predefined block of styles, because each design is unique and will require its own collection of css selectors and rules to achieve the desired styling.
