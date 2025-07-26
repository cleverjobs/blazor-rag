# How do I right-align a GridColumn content?

## Question

**SLSL** asked on 14 Jan 2020

How do I right-align grid column values? I tried the Template with a span but it does not seem to work and it also adds another element. This does not work: <GridColumn Field="Amount"> <Template> <span style="text-align:right"> @((context as BO).Amount.ToString("C")) </span> </Template> </GridColumn> Thanks. Joel

## Answer

**Marin Bratanov** answered on 14 Jan 2020

Hi, EDIT: There is a better (easier) approach described in a later comment. A span is an inline element and is as wide as its content, you'd need a block element that is as wide as its container (the cell) so you can move the contents inside it. Here's an example I made for you and at the end of this post is a screenshot of the result I get from it <TelerikGrid Data="@MyData" Height="500px">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name">
<Template> <div style="text-align: right;"> @((context as SampleData).Name) </div> </Template>
</GridColumn>
<GridColumn Field="HireDate" Title="Hire Date - Default string">
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov

### Response

**Bill** answered on 09 Nov 2020

So if we have a grid with 26 colums, one for each hour of the day, then I need to add a Template to each of the 26 GridColumns?

### Response

**Marin Bratanov** answered on 09 Nov 2020

Hi Bill, With versions prior to 2.18.0 - yes. With 2.18.0 and later - no, you could set the class on the cell through the CellRender event of the column. You may also want to Vote for and Follow this feature request in case this does not fit your preferences. Here's a basic example: <style>.k-grid td.right-align {
text-align: right;
}

.k-grid td.left-align {
text-align: left;
} </style>

<TelerikGrid Data="@MyData" Height="400px" Pageable="true" Width="750px">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" OnCellRender="@( (e)=> e.Class=" left-align " )" />
<GridColumn Field="@(nameof(SampleData.Name))" OnCellRender="@( (e)=> e.Class=" right-align " )" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" OnCellRender="@RepeatedCode" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" OnCellRender="@RepeatedCode" />
</GridColumns>
</TelerikGrid>

@code { void RepeatedCode ( GridCellRenderEventArgs e ) {
e.Class="right-align";
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**murat** commented on 15 May 2021

Hi Marin, Alignment is the key property for grid columns (web or desktop applicaion) If I'm not wrong kendo javascript also does not has this property. I apologise for this question but Why don't you add a simple property for this? Really, really I wonder what's the point of it. Best regards.

### Response

**Marin Bratanov** commented on 17 May 2021

You can Follow the implementation of such a built-in feature for that here [https://feedback.telerik.com/blazor/1431848-grid-column-header-and-content-alignment-horizontal-vertical](https://feedback.telerik.com/blazor/1431848-grid-column-header-and-content-alignment-horizontal-vertical) The problem with that is adding more and more parameters adds a performance hit in Blazor, and opens the door for a heavy bloated API for things that are easily done with CSS (e.g., through the CellRender, or RowRender events, or through an upcoming static Class parameter for the column). Nevertheless, this is something that is underway already.

### Response

**Leland** answered on 19 Mar 2024

For those seeing this old question, there is now a simple property on the GridColumn component that can handle this: TextAlign="ColumnTextAlign.Right" See more info at the following link: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#appearance](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#appearance)
