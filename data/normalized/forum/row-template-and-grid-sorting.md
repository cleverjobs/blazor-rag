# Row template and grid sorting

## Question

**Eri** asked on 08 Jan 2020

The documentation here [https://docs.telerik.com/blazor-ui/components/grid/templates](https://docs.telerik.com/blazor-ui/components/grid/templates) says Using the row template takes functionality away from the grid because it no longer controls its own rendering. For example, InCell and Inline editing could not render editors, detail templates will not be available, column sorting and reordering cannot change the data itself, only the headers. However when I take the row template example code from that page and add Sortable=true it appears to sort correctly (example repo at [https://github.com/austineric/TelerikGridSorting).](https://github.com/austineric/TelerikGridSorting).) Column reordering doesn't work as it says but I can't find anything wrong with the sorting. Does the sorting fail in some way I haven't come across or is it okay to use sorting with row templates?

## Answer

**Marin Bratanov** answered on 09 Jan 2020

Hello Eric, Thank you for noticing. That's an issue with me writing the wrong things. It is supposed to say that column resizing and column reordering won't work, but I've messed it up. It should be fixed live by the time you are reading this. Sorting will be fine. Regards, Marin Bratanov

### Response

**Daniel** answered on 17 Feb 2021

Marin, I just found this post. My TelerikGrid is also not sorting. It uses templates for each column. I have version 2.21.1 Is there any way to get the sorting working? Thanks. Dan G.

### Response

**Marin Bratanov** answered on 17 Feb 2021

Hello Dan, I would first test what happens when you remove the row template. If that helps, perhaps you need to add @key to (some of) the elements in the row so the framework will re-render them. If sorting does not work without customizations on the grid, I advise that you open a support ticket and send us an MCVE of the issue so we can have a look. Regards, Marin Bratanov

### Response

**Daniel** answered on 18 Feb 2021

Marin, Here's a snippet where I use both a template and just a simple GridColumn. The simple column does become sortable, the templated one still is not. Can you explain in more detail how and where the @key is used and can help in this example? Thanks! <GridColumns> <GridColumn Title="Sales" Width="34px" Field="@(nameof(SalesData.Sales))" /> <GridColumn Title="Sales"> <Template> <div style="text-align: center;">@((context as SalesData).Sales) </div> </Template> </GridColumn>

### Response

**Marin Bratanov** answered on 19 Feb 2021

Hello Daniel, The most likely reason for such behavior is that there is a Component in the row template, and the framework does not re-render it because it detects that after the sorting the same place in the markup will have an instance of the same component. So, a @key would be usually set inside that component and it would point to a record ID that it receives as a parameter, or you would use its OnParametersSetAsync method to request updated data if that's what you do. The following seems to work fine for me, I made two examples with both the RowTemplate (which is what this thread is about) and the column template which you seem to be using. If comparing against this does not help you move forward, I will need you to either post here a fully runnable example, or open a support ticket with that example so I can have a look. <TelerikGrid Data=@MyData Height="300px" Sortable="true">
<RowTemplate Context="employee">
<td>
<img class="rounded-circle" src="@($" /images/{employee.ID}.jpg ")" alt="employee photo" />
<strong>@employee.Name</strong>
</td>
<td>
Hired on: @(String.Format( "{0:dd MMM yyyy}", employee.HireDate))
</td>
</RowTemplate>
<GridColumns>
<GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" />
<GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" />
</GridColumns>
</TelerikGrid>

<TelerikGrid Data=@MyData Height="300px" Sortable="true">
<GridColumns>
<GridColumn Field=@nameof(SampleData.Name) Title="Employee Name">
<Template>
<div style="text-align: center;">@((context as SampleData).Name) </div>
</Template>
</GridColumn>
<GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" />
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

**Daniel** answered on 19 Feb 2021

Ah, thanks Marin. For my GridColumns that used template, I did not have the Field attribute. Now it's good!
