# treelist paging selection

## Question

**Joe** asked on 13 Jun 2025

I have a treelist with a checkbox for selection. However, my list is long so I added pagination. I help the user by pre-selecting a node and I need to display the page that exposes the first selected node. How do I do this? | <TelerikTreeList @ref=@TreeListRef Class="gsi-padding-0" Data="@UserGroups" SelectedItems="@SelectedGroups" IdField="Id" Pageable=true PageSize="10" ParentIdField="ParentId" SelectionMode="TreeListSelectionMode.Single" OnRowRender="@HandleRowRender" SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Group> m)=> OnGroupSelected(m))"> <TreeListColumns> <TreeListCheckboxColumn SelectAll="false" SelectChildren="false" CheckBoxOnlySelection="true" Width="64px" /> <TreeListColumn Field="Name" Title="Name" Expandable="true"> <Template> @{
var item=context as Gsi.Customer.Models.Group; <img height="32" width="32" src="@item.ImageUrl" /> @item.Name
} </Template> </TreeListColumn> </TreeListColumns> </TelerikTreeList>

## Answer

**Hristian Stefanov** answered on 17 Jun 2025

Hi Joel, To automatically show the page that contains the first pre-selected node in your Telerik TreeList with paging enabled, you need to programmatically set the TreeList's Page property based on the index of the selected node in your data. Steps to Implement Find the Index of the First Selected Node Identify the index of the first selected node in your data source. Calculate the Page Number Use the PageSize to determine on which page the node appears. Set the Page Property Assign the calculated page number to the TreeList's Page parameter before rendering. Example Implementation <TelerikTreeList Data="@TreeListData" IdField="@nameof(Employee.Id)" ParentIdField="@nameof(Employee.ParentId)" SelectionMode="@TreeListSelectionMode.Multiple" @bind-SelectedItems="@SelectedEmployees" Pageable="true" @bind-PageSize="@PageSize" @bind-Page="@CurrentPage"> <TreeListColumns> <TreeListCheckboxColumn Width="50px" /> <TreeListColumn Field="@nameof(Employee.FirstName)" Title="First Name" Width="350px" Expandable="true" /> <TreeListColumn Field="@nameof(Employee.LastName)" Title="Last Name" /> <TreeListColumn Field="@nameof(Employee.Position)" Title="Position" Width="200px" /> </TreeListColumns> </TelerikTreeList> @code {
private List <Employee> TreeListData { get; set; }=new();
private IEnumerable <Employee> SelectedEmployees { get; set; }=Enumerable.Empty <Employee> ();
private int PageSize=10;
private int CurrentPage=1;

protected override void OnInitialized()
{
TreeListData=new List <Employee> ();

for (int i=1; i <=59; i++)
{
TreeListData.Add(new Employee()
{
Id=i,
ParentId=i <=3 ? null : i % 3 + 1,
FirstName="First " + i,
LastName="Last " + i,
Position=i <=3 ? "Team Lead" : "Software Engineer"
});
}

SelectedEmployees=new List <Employee> () { TreeListData.ElementAt(2) };

var selectedId=SelectedEmployees.FirstOrDefault()?.Id;
if (selectedId !=null)
{
// Step 1: Flatten the tree as it would appear expanded
var flatList=new List <Employee> ();
foreach (var root in TreeListData.Where(e=> e.ParentId==null))
{
FlattenHierarchy(root, flatList);
}

// Step 2: Find index of selected item in flattened list
var index=flatList.FindIndex(e=> e.Id==selectedId);
if (index>=0)
{
CurrentPage=(index / PageSize) + 1;
}
}
}

private void FlattenHierarchy(Employee node, List <Employee> result)
{
result.Add(node);
var children=TreeListData.Where(e=> e.ParentId==node.Id);
foreach (var child in children)
{
FlattenHierarchy(child, result);
}
}

public class Employee
{
public int Id { get; set; }
public int? ParentId { get; set; }
public string FirstName { get; set; }=string.Empty;
public string LastName { get; set; }=string.Empty;
public string Position { get; set; }=string.Empty;
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Joel** answered on 15 Jul 2025

Your solution didn't work for me but it got me on the right track. Your "Flatten the tree as it would appear expanded" comment got me there. I have a "Depth" field which is calculated as distance from the root. I then order the tree node by their name (same depth; same parentId, different name). So, I was able to get the flat structure using a sort against those properties. var orderedGroups=FlatGroups.OrderBy(x=> x.Depth)
.ThenBy(x=> x.ParentId).ThenBy(x=> x.Name);

int index=orderedGroups.ToList().FindIndex(x=> x.Id==Group.Id);
if (index>=0)
{
GroupCurrentPage=(index / GroupPageSize) + 1;
} How I set depth... keep in mind, I have only 1 root. /// <summary> /// Sets the depth of each group in the list based on the hierarchy.
/// </summary> public void SetDepth()
{
Group root=this.GetRoot();
if (root !=null)
{
SetDepthRecursive(root, 0);
}
}

/// <summary> /// Recursively sets the depth of each group in the list based on the hierarchy.
/// </summary> /// <param name="group"> </param> /// <param name="depth"> </param> private void SetDepthRecursive(Group group, int depth)
{
group.Depth=depth;
var children=this.Where(g=> g.ParentId==group.Id).ToList();
foreach (var child in children)
{
SetDepthRecursive(child, depth + 1);
}
}
