# Passing other data to Change Event

## Question

**Rog** asked on 28 Jan 2020

I am using a TelerikDropDownList inside of a @foreach. What I would like when the change event fires is to pass another piece of data from the foreach iteration as well as the selected item in the drop down. Is this possible with the current drop down? Here is a code sample: @foreach (WorkItem workItem in workItemGroup.WorkItems) { <tr> <td>@workItem.WorkItemType.WorkItemTypeCategory.Title - @workItem.WorkItemType.Title</td> <td> <TelerikDropDownList Class="tlk-dd-sm tlk-dd-bg-white w-100" Data="@departments" TextField="Title" ValueChanged="@((v)=> Test(v))"/> </td> <td>@workItem.WorkItemStatus.Title</td> </tr> } The only solution that I can think of currently is to create each <td> as its own razor component. Roger

## Answer

**Marin Bratanov** answered on 29 Jan 2020

Hi Roger, Adding another argument to the method that takes its value from the local variable in the loop should let you do this. Here's an example I made for you that seems to work fine for me (I highlighted the key aspects, the rest of the changes are to get this snippet off the ground): @result
@foreach (WorkItem workItem in theWorkItems@*workItemGroup.WorkItems*@)
{
<tr>
<td>@workItem.Title @*@workItem.WorkItemType.WorkItemTypeCategory.Title - @workItem.WorkItemType.Title*@</td>
<td>
<TelerikDropDownList Class="tlk-dd-sm tlk-dd-bg-white w-100" Data="@departments" TextField="Title" ValueChanged="@(( int v)=> Test(v, workItem.Title ))" />
</td>
<td>@*@workItem.WorkItemStatus.Title*@</td>
</tr>
}

@code{
MarkupString result { get; set; } void Test ( int ddlValue, string workItemTitle ) {
result=new MarkupString(result + $"ValueChange on ddl in row {workItemTitle}, chosen value: {ddlValue} <br />" );
} public List<WorkItem> theWorkItems { get; set; }=new List<WorkItem>()
{ new WorkItem { Title="first" }, new WorkItem { Title="second" }, new WorkItem { Title="third" },
}; public List<Department> departments { get; set; }=new List<Department>()
{ new Department{ Value=1, Title="one" }, new Department{ Value=2, Title="two" }, new Department{ Value=3, Title="three" },
}; public class WorkItem { public string Title { get; set; }
} public class Department { public int Value { get; set; } public string Title { get; set; }
}
} Regards, Marin Bratanov

### Response

**Roger** answered on 29 Jan 2020

Wow, way easier than I thought it would be. Thanks for putting in the extra work to provide the most helpful response. Perfect! Roger

### Response

**Roger** answered on 29 Jan 2020

An issue that I am having after implementing this is that I need to provide an initial value by adding Value="@workItem.AssignedDepartmentId" but this gives me the following error: The type arguments for method 'TypeInference.CreateTelerikDropDownList_0<TItem, TValue>(RenderTreeBuilder, int, int, string, int, IEnumerable<TItem>, int, string, int, string, int, EventCallback<TValue>, int, TValue)' cannot be inferred from the usage. Try specifying the type arguments explicitly. Here is the DDL <TelerikDropDownList Class="tlk-dd-sm tlk-dd-bg-white w-100" Data="@departments" ValueField="DepartmentId" TextField="Title" ValueChanged="@((string v)=> WorkItemAssignedGroupChanged(v, workItem))" Value="@workItem.AssignedDepartmentId"/>

### Response

**Roger** answered on 29 Jan 2020

Sorry, this the post above was my own issue. I had it as a string instead of an int.
