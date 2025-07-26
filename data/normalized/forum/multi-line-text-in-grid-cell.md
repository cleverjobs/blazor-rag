# Multi-line text in grid cell

## Question

**Pat** asked on 14 May 2020

Hello, I need to display a multi-line text in a grid cell. How must I format it? If I try to replace \n\r with <br />, the "<br />" test is displayed in the output.

## Answer

**Marin Bratanov** answered on 14 May 2020

Hi Patrick, Blazor escapes HTML by default - to prevent XSS issues. If you explicitly want to render HTML coming from the code/data, you must use a MarkupString in the cell template. Here's a modified example from the docs: <TelerikGrid Data="@MyData" Height="500px">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.ID))" Title="Photo">
<Template>
@{ var employee=context as SampleData;
<img class="rounded" src="@($" /images/{employee.ID}.jpg ")" alt="employee photo" />
}
</Template>
</GridColumn>
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name">
<Template>
Employee name is:
<br />
@( new MarkupString( (context as SampleData).Name ) )
</Template>
</GridColumn>
<GridColumn Field="HireDate" Title="Hire Date - Default string">
</GridColumn>
<GridColumn Field="HireDate" Title="Hire Date - Custom string">
<Template>
@((context as SampleData).HireDate.ToString( "dd MMM yyyy" ))
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
ID=x,
Name=" <strong> name </strong><br /> " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov

### Response

**Patrick** answered on 15 May 2020

Thank you Marin, it works, with additional work for managing of spaces and end of lines.

### Response

**David** commented on 28 Jun 2022

I just did the template part as: <Template> @( new MarkupString((context as SampleData).Name) ) </Template> And put all of the text/HTML in the Name, or whatever, property. I envisaged a problem puting <br/> directly in the Template. This works for me.
