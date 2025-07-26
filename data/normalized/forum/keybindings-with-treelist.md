# KeyBindings with TreeList

## Question

**mic** asked on 27 Jan 2025

Hello, we are currently evaluating Telerik for use in a new application. One major hurdle we are facing at the moment are key bindings. The application we are working on contains quite a bit of shortcuts as it aims at power users and key bindings are important for the efficiency of the workflows. The main component we are using is the TreeList, and one basic use case would be to expand and collapse all items in the TreeList with "*"/"-". I read the forum articles about introducing keybindings to other components by wrapping the component in a div and using onkeydown on the div. That does not work with TreeList however (as I suspect the TreeList captures key events itself). I suspect using JS Interop might be the only option we have, but I just wanted to check if I am missing anything obvious. Thank you, Michael

## Answer

**Tsvetomir** answered on 28 Jan 2025

Hello Michael, Indeed, by design, the TreeList component captures the onkeydown event. With that in mind, to achieve the desired result I recommended using the onkeyup event. As you mentioned, the approach relies on wrapping the Grid in the HTML div container and using the onkeyup event. Also, setting the tabindex="0" to the div wrapper is required, because the container needs to be focusable. The only pre-requisite of such a scenario is that the Grid should be focused. For example, clicking on the column header and then pressing the `* ` or ` - ` key will achieve the desired result. Here is a code snippet that utilizes the above approach: <div @onkeyup="@OnKeyUp" tabindex="0"> <TelerikTreeList @ref="TreeListRef" Data="@Data" ItemsField="@(nameof(Employee.DirectReports))" OnStateInit="((TreeListStateEventArgs<Employee> args)=> OnStateInitHandler(args))" Reorderable="true" Resizable="true" Sortable="true" FilterMode="@TreeListFilterMode.FilterRow" Pageable="true" Width="850px"> <TreeListColumns> <TreeListColumn Field="@nameof(Employee.Name)" Expandable="true" Width="320px" /> <TreeListColumn Field="@nameof(Employee.EmailAddress)" Width="220px" /> <TreeListColumn Field="@nameof(Employee.HireDate)" Width="220px" /> </TreeListColumns> </TelerikTreeList> </div> @code {
private TelerikTreeList <Employee> TreeListRef { get; set; }=new TelerikTreeList <Employee> ();
private List <Employee> Data { get; set; }
private int LastId { get; set; }=1; private async Task OnKeyUp(KeyboardEventArgs args)
{
if (args.Key=="*" || args.Key=="-")
{
await SetTreeListExpandedItems();
}
} private async Task SetTreeListExpandedItems()
{
if (!(TreeListRef.GetState().ExpandedItems.Any()))
{
List <Employee> toExpand=new List <Employee> ();
foreach (Employee item in Data)
{
toExpand.Add(item);
if (item.DirectReports.Any())
{
foreach (Employee child in item.DirectReports)
{
toExpand.Add(child);
}
}
}

var expandedState=new TreeListState <Employee> ()
{
ExpandedItems=new List <Employee> (toExpand)
};

await TreeListRef.SetStateAsync(expandedState);
}
else
{
var expandedState=new TreeListState <Employee> ()
{
ExpandedItems=new List <Employee> ()
};

await TreeListRef.SetStateAsync(expandedState);
}

}

private async Task OnStateInitHandler(TreeListStateEventArgs <Employee> args)
{
var collapsedItemsState=new TreeListState <Employee> ()
{
//collapse all items in the TreeList upon initialization of the state
ExpandedItems=new List <Employee> ()
};

args.TreeListState=collapsedItemsState;
}

protected override async Task OnInitializedAsync()
{
Data=await GetTreeListData();
}

private async Task<List <Employee>> GetTreeListData()
{
List <Employee> data=new List <Employee> ();

for (int i=1; i <15; i++)
{
Employee root=new Employee
{
Id=LastId,
Name=$"root: {i}",
EmailAddress=$"{i}@example.com",
HireDate=DateTime.Now.AddYears(-i),
DirectReports=new List <Employee> (), // prepare a collection for the child items, will be populated later in the code
};
data.Add(root);
LastId++;

for (int j=1; j <4; j++)
{
int currId=LastId;
Employee firstLevelChild=new Employee
{
Id=currId,
Name=$"first level child {j} of {i}",
EmailAddress=$"{currId}@example.com",
HireDate=DateTime.Now.AddDays(-currId),
DirectReports=new List <Employee> (), // collection for child nodes
};
root.DirectReports.Add(firstLevelChild); // populate the parent's collection
LastId++;

for (int k=1; k <3; k++)
{
int nestedId=LastId;
// populate the parent's collection
firstLevelChild.DirectReports.Add(new Employee
{
Id=LastId,
Name=$"second level child {k} of {j} and {i}",
EmailAddress=$"{nestedId}@example.com",
HireDate=DateTime.Now.AddMinutes(-nestedId)
}); ;
LastId++;
}
}
}

return await Task.FromResult(data);
}

public class Employee
{
public List <Employee> DirectReports { get; set; }

public int Id { get; set; }
public string Name { get; set; }
public string EmailAddress { get; set; }
public DateTime HireDate { get; set; }
}
} I hope this serves you well. Regards, Tsvetomir Progress Telerik

### Response

**michael.pisula@tngtech.com** commented on 28 Jan 2025

That worked, thanks a lot, would have never found that by myself :)
