# Sort shortdate doesn't work

## Question

**Mau** asked on 11 Sep 2020

I have these two variables public DateTime? StartDate { get; set; } public string StartDateShortDate=> StartDate?.ToShortDateString(); If I filter on StartDate the sorting start with 2016 then 2017 then 2018 ... like expected. If I filter on StartDateShortDate the sorting is at "random". Maurice

## Answer

**Marin Bratanov** answered on 11 Sep 2020

Hi Maurice, The sort rules for strings differ from those for numbers and from those for dates, so the behavior is expected to be different. I'm attaching below a short video that shows the expected and correct behavior of the string sort operation and the difference between sorting a real DateTime. It results from the code snippet below. If you need a display for the dates, I would, however, recommend two other options that will also save you the extra string field in the model: Use the cell template to format the date: [https://docs.telerik.com/blazor-ui/components/grid/templates/column](https://docs.telerik.com/blazor-ui/components/grid/templates/column) Follow the feature where the column will be able to apply a C# string format to the field for you, and use it when it becomes available: [https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats](https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats) Code snippet for sorting example: <TelerikGrid Data="@MyData" Sortable="true" AutoGenerateColumns="true" Pageable="true">
</TelerikGrid>

@code { public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
Id=x,
TheName="name " + x,
StartDate=DateTime.Now.Date.AddDays(-x)
}); public class SampleData { public int Id { get; set; } public string TheName { get; set; } public DateTime? StartDate { get; set; } public string StartDateShortDate=> StartDate?.ToShortDateString();
}
} Regards, Marin Bratanov
