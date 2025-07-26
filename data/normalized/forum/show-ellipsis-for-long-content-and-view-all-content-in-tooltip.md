# Show Ellipsis for Long Content and view all Content in Tooltip

## Question

**Jes** asked on 23 Mar 2021

I'm essentially trying to achieve what's been solved for Kendo UI for JQuery in Blazor Grid: [https://docs.telerik.com/kendo-ui/knowledge-base/grid-ellipsis-text-show-tooltip](https://docs.telerik.com/kendo-ui/knowledge-base/grid-ellipsis-text-show-tooltip) "How can I show ellipsis in the Grid cells where the text does not fit the specified width and display the full content in a tooltip when the user hovers over the cell?" Thanks

## Answer

**Marin Bratanov** answered on 24 Mar 2021

Hello Jesse, This sample relies on DOM manipulations, which is not something that you can easily do with Blazor. So, the Blazor approach would be to use the template of a column, render the text as desired (say, call .Substring(0, 10) if the text is long) and add a tooltip to the cell to target that text in case it will need a tooltip. You can find example of adding tooltips to grid cells here: [https://github.com/telerik/blazor-ui/tree/master/tooltip/in-grid.](https://github.com/telerik/blazor-ui/tree/master/tooltip/in-grid.) Here's an example I made for you that also utilizes the CellRender event of the column to set its CSS rules so that it has the required appearance: In this sample rows 10 and later have tooltips in the Name column, which has ellipsis overflow set. <style>
.ellipsis-overflow {
text-overflow: ellipsis;
white-space:nowrap;
}
</style> <TelerikGrid Data="@GridData" PageSize="15" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true">
<GridColumns>
<GridColumn Field="@(nameof(BasicEmployee.Id))" Width="120px" />
<GridColumn Field="@(nameof(BasicEmployee.Name))" Title="Name" Groupable="false" Width="70px" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" ellipsis-overflow " )"> <Template>
@{
BasicEmployee employee=context as BasicEmployee; if (employee.Name.Length> 6 ) // in this sample this is "name 10" {
<span title="@employee.Name" id="@( " tooltip-target " + employee.Id)">@employee.Name.Substring( 0, 6 )</span>
<TelerikTooltip TargetSelector="@( " #tooltip-target" + employee.Id)" Position="@TooltipPosition.Right">
</TelerikTooltip>
} else {
<text>@employee.Name</text>
}
}
</Template> </GridColumn>
<GridColumn Field="@(nameof(BasicEmployee.Team))" Title="Team" />
</GridColumns>
</TelerikGrid>

@code { public List<BasicEmployee> GridData { get; set; }=Enumerable.Range( 1, 90 ).Select(x=> new BasicEmployee
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
}).ToList(); public class BasicEmployee { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; }
}
} Regards, Marin Bratanov Progress Telerik

### Response

**Jesse** answered on 24 Mar 2021

Hello, Marin. Thanks for the quick response and handy solution! Regards, Jesse

### Response

**Marin Bratanov** answered on 25 Mar 2021

Happy to see you move forward, Jesse! --Marin

### Response

**Larry** commented on 03 Feb 2023

I did something similar to this. I ran into an issue with how the tooltip seems to be handling characters that its jquery selector doesn't like. As an example, when I try to save a '!' it makes it to my database but when I 'refresh' the data to be reflected in the textbox after the save I get this error: "Failed to execute 'querySelectorAll' on 'Document': '.tooltip-target!, [data-telerik-tooltip-id]' is not a valid selector. Is there a workaround for this? Can a tooltip be used to display a less restrictive string rather than using a jquery selector? I'm concatenating the id attribute with whatever text a user types into the text box and it's not uncommon for the end-users to use @characters and parenthesis

### Response

**Svetoslav Dimitrov** commented on 08 Feb 2023

Hello Larry, I have opened a new feature request on your behalf - Use document.getElementsByClassName() instead of document.querySelectorAll(). I have made it status to Under Review so that the dev team and I further evaluate it and see if the two methods can be just replaced or if there should be some additional logic.
