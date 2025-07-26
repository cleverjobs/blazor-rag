# Links within Grid

## Question

**Cam** asked on 14 Jun 2019

Hey guys, I currently have a grid that outputs values from a database within a grid. This works well however I have one field that contains sets of Url's. This is currently output as text. Is there anyway to make it a href/link or can you only output text within the grid? Thanks, Cameron

## Answer

**Marin Bratanov** answered on 14 Jun 2019

Hi, You can use a template and render in it a markup string. Here's a small example I made for you: @using Telerik.Blazor.Components.Grid <TelerikGrid Data="@MyData" Height="500px"> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> <Template> @{ var employee=context as SampleData; @((MarkupString)$ "<a href=\" [http://mysite.com/employee/](http://mysite.com/employee/) {employee.ID}\" target=\"_blank\">{employee.Name}</a>" ) } </Template> </TelerikGridColumn> <TelerikGridColumn Field="HireDate" Title="Hire Date - Default string"> </TelerikGridColumn> </TelerikGridColumns> </TelerikGrid> @functions { public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; } } public IEnumerable<SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData { ID=x, Name="name " + x, HireDate=DateTime.Now.AddDays(-x) }); } Regards, Marin Bratanov

### Response

**Cameron** answered on 14 Jun 2019

Excellent, I'll give it a go. Thanks

### Response

**Dustin** answered on 10 Dec 2019

This worked for me in the sense that the cell now acts as a hyperlink and downloads my target file, but the text in the cell is not blue or underlined. Are there additional formatting options that will help indicate to the user that the cell acts like a hyperlink?

### Response

**Adam** commented on 05 Oct 2023

Did you come up with a solution on how to get the contents to appear as the hyperlink it is? Preferrably to actually have the actions of the anchor tag. I can use OnCellRender to underline the cell contents but that doesn't make it work like a hyperlink that changes color when clicked.

### Response

**Adam** commented on 06 Oct 2023

Here is what seems to work (but maybe there is a better way): Use css to create selector: .k-grid a.gridcolumn-hyperlink { color: blue; text-decoration: underline;
}.k-grid a.gridcolumn-hyperlink:visited { color: green
} And use the class on the anchor <a href="@MyClass.SomeLink" target="_blank" class="gridcolumn-hyperlink"> @MyClass.TextForLink </a>

### Response

**Dimo** commented on 10 Oct 2023

@Adam - your approach is valid. Another option is to implement the CSS selectors through table cell classes instead of setting class to each <a>. This is worth using if you have more than one link inside the same table cell. Grid Column OnCellRender event

### Response

**Marin Bratanov** answered on 11 Dec 2019

Hello Dustin, This was just one example of rendering an HTML link inside the grid cell. You can alter it as needed (e.g., to use an actual anchor, without a markup string cast), or to add a class to it that will provide the desired appearance (like altering the color and adding some underlining). This is entirely up to your preferences, the template lets you put the desired content in it. You may also find this KB article useful on altering the cell background. Regards, Marin Bratanov

### Response

**Dustin** answered on 13 Dec 2019

Thank you for the response! I'll check out your link.

### Response

**Bob** answered on 06 Oct 2020

I am doing this with a mailto link, however I also have Selection Turned on for the grid. The link works to open an email but I need to stop the row selection as it is causing an error. Is there any way to have the link work as a link when clicked on but have row selection work for anything else clicked on in the row?

### Response

**Marin Bratanov** answered on 07 Oct 2020

Hi Bob, You can stop the event propagation in the template to prevent selection, you can see an example here: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selection-in-template](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selection-in-template) Regards, Marin Bratanov
