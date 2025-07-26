# Individual cell back color

## Question

**Ran** asked on 25 Nov 2019

Hi, I'd like to be able to set the backcolor on a cell by cell basis. I think the way is to do this with a template, but I don't know how to get the <td> element to style. Any pointers would be greatly appreciated. Thanks .. Ed

## Answer

**Marin Bratanov** answered on 25 Nov 2019

Hello Ed, If you use a row template, you can do that with any markup and logic (css classes, inline rules) you like because you control the entire markup: [https://docs.telerik.com/blazor-ui/components/grid/templates#row-template.](https://docs.telerik.com/blazor-ui/components/grid/templates#row-template.) When using a cell template, however, you put content inside the <td> element the grid renders, so the only way to target would be (theoretically!) by adding a specific element and using CSS rules like the :has(your special selector) pseudoselector (see here and here ) because in CSS you can't go up the DOM (see here ). The solution for that is to remove the default padding of the cells and to apply the desired padding and backgrounds with your own CSS, something like this: <style> /* replace the default cell padding with custom element padding to remove traces of the original background */.k-grid-table td { padding: 0; /*height: 40px;*/ /*you may want to set height to the cells so the height:100% to the child div works better*/ }.k-grid-table td.my-padding { height: 100%; padding: 5px; /* or copy the original ones from our rendering */ } /* set custom background */.k-grid-table td.special { background: yellow;
}
</style>

<TelerikGrid Data="@MyData " Height="500px">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.ID))" Title="Photo">
<Template>
@{ var employee=context as SampleData;
<div class="@( employee.ID % 3==0? "special my-padding": "my-padding" ) ">@employee.ID</div>
}
</Template>
</GridColumn>
<GridColumn Field=" @(nameof(SampleData.Name)) " Title=" Employee Name ">
</GridColumn>
<GridColumn Field=" HireDate " Title=" Hire Date - Default string ">
</GridColumn>
<GridColumn Field=" HireDate " Title=" Hire Date - Custom string ">
<Template>
@((context as SampleData).HireDate.ToString(" dd MMM yyyy "))
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid>

@code {
public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

public IEnumerable<SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData
{
ID=x,
Name=" name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 26 Nov 2019

Outstanding! Thanks so much for all the help. I know I'm not the only one with these questions and I really appreciate your kind assistance.

### Response

**Marin Bratanov** answered on 26 Nov 2019

Hi Ed, I made a KB with this information as well, leaving it here for anyone else with a similar question: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background.) Regards, Marin Bratanov

### Response

**Robert** answered on 21 Oct 2020

This doesn't work, since.k-grid td has higher priority. Doing .k-grid-table td { padding: 0 !important; } makes it work, but of course leads to that all td:s are without padding. You of course only want the td:s in question to be without padding, or preferably a much simpler solution to such a common requirement.

### Response

**Marin Bratanov** answered on 21 Oct 2020

Hi Robert, By the end of the week (or maybe even later today) the 2.18.0 release will bring a much easier and better way to do this - an event for the column will let you set a class to the <td> element so you can style it as needed, conditionally. The KB article above will be updated with that, and there will be documentation and a demo. You can preview this bit of the documentation here right now. Regards, Marin Bratanov

### Response

**Steve** answered on 16 Nov 2020

That looks pretty good, but is there any way of finding out which cell column in the grid actually fired. I know the Item property of GridCellRenderEventArgs gives me the model object which contains data for the whole row and the Value property gives me the value of the cell but is there any way of knowing that it was the "Employee Name" item that fired? In the use case i have in mind, multiple GridColumns will share the same OnCellRenderHandler but i need to be able to determine which column fired the event.

### Response

**Marin Bratanov** answered on 16 Nov 2020

Hi Steve, You could add a lambda expression in the column definition that will pass additional data to the handler as needed. Regards, Marin Bratanov

### Response

**Steve** answered on 16 Nov 2020

Thanks Marin. That worked.
