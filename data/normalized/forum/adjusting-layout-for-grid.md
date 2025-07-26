# Adjusting layout for Grid

## Question

**Mic** asked on 07 Apr 2020

What's the best way to adjust the margins, padding and alignment for the contents of a row using the Telerik Grid? I'm using the Bootstrap theme if it matters.

## Answer

**Marin Bratanov** answered on 07 Apr 2020

Hi Michael, You can inspect the rendered HTML and its CSS rules that come from the themes in order to devise heavier selectors that will achieve the desired look. The following blog post can help you do that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools) I also made the following example for you that you can use as base, and it results in the screenshot attached to this message. <style>.special-grid-paddings th.k-header { padding: 40px;
}.special-grid-paddings.k-master-row td { padding: 20px;
}
</style>

<TelerikGrid Class=" special-grid-paddings " Data=" @MyData " Height="300px" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterMenu">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.ID))">
</GridColumn>
<GridColumn Field="@(nameof(SampleData.Name))">
</GridColumn>
<GridColumn Field="HireDate" Width="350px">
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { public class SampleData {
public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable <SampleData> MyData=Enumerable.Range (1, 50).Select ( x=> new SampleData {
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov
