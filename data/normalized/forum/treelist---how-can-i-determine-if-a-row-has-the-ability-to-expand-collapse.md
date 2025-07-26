# TreeList - How can I determine if a row has the ability to expand/collapse?

## Question

**TedTed** asked on 10 Jun 2022

Hi, I've bound a TreeList to flat data. How can I determine if the TreeList has determined that a given row can be expanded/collapsed based upon the flat data, (i.e., how can I determine whether or not an expend/collapse arrow has been placed on the row)? This has an additional complexity in that the list cannot expand/collapse a row if it does not have children. A use case for this would be to react to a double-click in a row and expand or collapse the row if the row is allowed to do that.

## Answer

**Dimo** answered on 15 Jun 2022

Hi Ted, Expandability and arrow rendering with flat data depends entirely on the HasChildren property of the model. Regards, Dimo

### Response

**Ted** commented on 15 Jun 2022

Dimo, That's not true for flat data. The HasChildren property is optional and not required. If it is not specified, the control itself determines whether or not to display the expand arrow for flat data based upon whether or not the parent row actually has children specified in the flat data. If the parent row does not have any children, an expand arrow does not show. I'm attaching a screenshot from our test data, but you can repo this in your own test case. It would be nice if a public method or property could be added that would indicate whether a row in the TreeList is showing an expand arrow or not when bound to flat data, since it must already have this info internally determined.

### Response

**Dimo** commented on 17 Jun 2022

@Ted - yes, HasChildren is not required, but it will still do the job. I assume you prefer to avoid HasChildren in the data? This is possible if the data is not much, and you load it at once, instead of loading it on demand via the OnExpand event. Since all the data is available, here are some other options: Assign HasChildren on the fly in the view model, when the data loads. Create a Dictionary map with all items that have children. Expand or collapse an item, even if it has no children. The TreeList will not throw an error, simply nothing will happen. This example below shows all mentioned options. <TelerikTreeList Data="@Data" @ref="@TreeList" IdField="Id" ParentIdField="ParentId" Pageable="true" Width="850px" Height="400px" OnRowDoubleClick="@OnRowDoubleClick"> <TreeListColumns> <TreeListColumn Field="HasChildren" Width="120px" /> <TreeListColumn Field="Name" Expandable="true" /> </TreeListColumns> </TelerikTreeList>

@code {
List<Employee> Data { get; set; }
TelerikTreeList<Employee> TreeList { get; set; }
Dictionary<int, bool> HasChildrenDictionary { get; set; } async Task OnRowDoubleClick ( TreeListRowClickEventArgs args ) { var item=args.Item as Employee; var state=TreeList.GetState(); var expandedExists=state.ExpandedItems.FirstOrDefault( x=> x.Id==item.Id); if (expandedExists !=null )
{
state.ExpandedItems.Remove(item);
} else {
state.ExpandedItems.Add(item);
}

args.ShouldRender=true; await TreeList.SetState(state);
}

protected override async Task OnInitializedAsync ( ) {
Data=await GetTreeListData();
SetHasChildren();
} void SetHasChildren ( ) {
foreach ( var item in Data)
{ if (item.ParentId !=null )
{
Data.Where( x=> x.Id==item.ParentId).First().HasChildren=true;
HasChildrenDictionary[item.ParentId.Value]=true;
}
}
} // sample model public class Employee {
public int Id { get; set; }
public int? ParentId { get; set; }
public bool HasChildren { get; set; }

public string Name { get; set; }
} // data generation async Task<List<Employee>> GetTreeListData ( ) {
List<Employee> data=new List<Employee>(); for (int i=1; i <=5; i++)
{
data.Add( new Employee
{
Id=i,
ParentId=null, // indicates a root-level item Name=$ "root: {i}" }); ; if (i> 2 )
{ for (int j=1; j <=3; j++)
{
int currId=i * 100 + j;
data.Add( new Employee
{
Id=currId,
ParentId=i,
Name=$ "first level child {j} of {i}" });
}
}
} return await Task.FromResult(data);
}
}

### Response

**Ted** commented on 17 Jun 2022

Dimo, Yeah, I get all this, and the above is possible, but it's a bunch of unnecessary work, since the TreeList must already have a variable or method that determines whether or not a row has an expand arrow when bound to flat data. What I'm hoping is that the TreeList can expose this property or method to clients so that it can be used without have to go through all of the code above. Could we add this as a feature request? The feature request would be to add a public method or property that returns a boolean (i.e., bool IsExpandable) indicating whether or not a given row has an expand arrow when the TreeList is bound to flat data.

### Response

**Dimo** commented on 17 Jun 2022

@Ted - I already asked our developers before my previous reply. They were reluctant about such a feature request, as it repeats existing functionality (HasChildren) or possible custom implementation.
