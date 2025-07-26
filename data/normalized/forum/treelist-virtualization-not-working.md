# Treelist virtualization not working

## Question

**Jas** asked on 30 Jul 2021

I've been working with the treelist, but have hit a snag on performance when I have>30 items (and I need>1000). I had hoped that virtualization would save me, but once I included it I found it didn't really help at all. I've greatly simplified my functionality for my sample code, as my actual code uses OnRowRender, hierarchy, etc etc etc that significantly slows performance. But even in this simple example, you can notice a significant difference. Notably, paging the treelist is much faster than virtualising it. But I see no reason this should be the case, and hence I think virtualization is not working at all. Just for completeness, I have included lists and a virtualised list for comparison. You can really spot the big difference when you jump between the tabs. (note: the refresh button crashes on the virtualized tree list tab example, and doesn't if you turn off virtualization. That's another problem, but not the priority.) Is this a bug, or am I doing it wrong, or is the Treelist not suitable for 1000 rows? @page "/" <TelerikTabStrip Class="LeftPanelTabstrip" TabPosition="Telerik.Blazor.TabPosition.Top"> <TabStripTab Title="paging"> <button @onclick="buttonClick"> Refresh </button> <TelerikTreeList Data="@Data" IdField="EmployeeId" ParentIdField="ReportsTo" Pageable="true" Class="MyTreeList"> <TreeListColumns> <TreeListColumn Field="FirstName"> </TreeListColumn> <TreeListColumn Field="LastName"> </TreeListColumn> <TreeListColumn Field="DOB"> </TreeListColumn> <TreeListColumn Field="EmployeeId"> </TreeListColumn> </TreeListColumns> </TelerikTreeList> </TabStripTab> <TabStripTab Title="virtualized"> <button @onclick="buttonClick"> Refresh </button> <TelerikTreeList Data="@Data" IdField="EmployeeId" ParentIdField="ReportsTo" ColumnVirtualization="true" Width="700px" Height="700px" Class="MyTreeList"> <TreeListColumns> <TreeListColumn Field="FirstName"> </TreeListColumn> <TreeListColumn Field="LastName"> </TreeListColumn> <TreeListColumn Field="DOB"> </TreeListColumn> <TreeListColumn Field="EmployeeId"> </TreeListColumn> </TreeListColumns> </TelerikTreeList> </TabStripTab> <TabStripTab Title="Not virtualized"> <button @onclick="buttonClick"> Refresh </button> <TelerikTreeList Data="@Data" IdField="EmployeeId" ParentIdField="ReportsTo" Width="700px" Height="700px" Class="MyTreeList"> <TreeListColumns> <TreeListColumn Field="FirstName"> </TreeListColumn> <TreeListColumn Field="LastName"> </TreeListColumn> <TreeListColumn Field="DOB"> </TreeListColumn> <TreeListColumn Field="EmployeeId"> </TreeListColumn> </TreeListColumns> </TelerikTreeList> </TabStripTab> <TabStripTab Title="List View"> <button @onclick="buttonClick"> Refresh </button> <TelerikListView Data="@Data" Width="700px" Height="700px"> <Template> <div style="display: grid;height: 40px;grid-template-columns: 1fr 1fr 1fr 1fr;grid-column-gap: 20px;"> <div> @context.FirstName </div> <div> @context.LastName </div> <div> @context.DOB </div> <div> @context.EmployeeId.ToString() </div> </div> </Template> </TelerikListView> </TabStripTab> <TabStripTab Title="virtualize"> <button @onclick="buttonClick"> Refresh </button> <div style="height:700px"> <Microsoft.AspNetCore.Components.Web.Virtualization.Virtualize Items="Data" Context="context"> <tr> <td> <div style="display: grid;height: 40px;grid-template-columns: 1fr 1fr 1fr 1fr;grid-column-gap: 20px;"> <div> @context.FirstName </div> <div> @context.LastName </div> <div> @context.DOB </div> <div> @context.EmployeeId.ToString() </div> </div> </td> </tr> </Microsoft.AspNetCore.Components.Web.Virtualization.Virtualize> </div> </TabStripTab> </TelerikTabStrip> @code {
public List <Employee> Data { get; set; }

public class Employee
{
public int EmployeeId { get; set; }
public string FirstName { get; set; }
public string LastName { get; set; }
public string DOB { get; set; }

}

protected override void OnInitialized()
{
Populate();
}

public void Populate()
{
Data=new List <Employee> ();
var rand=new Random();
int currentId=1;

for (int i=1; i <3000; i++)
{
string text=rand.Next().ToString();
Data.Add(new Employee()
{
EmployeeId=currentId,

FirstName=text + i.ToString(),
LastName=text + i.ToString(),
DOB=text + i.ToString()
});

currentId++;
}
}

public void buttonClick()
{
Populate();
}
} Cheers, Jason

### Response

**Jason** commented on 30 Jul 2021

OH, it's column virtualization. How do I do real virtualization:(

### Response

**Eric R | Senior Technical Support Engineer** commented on 03 Aug 2021

At this time, the described virtualization approach is better handled by Paging as you mentioned. I would also like to mention that we do include the ability to Load on Demand. However, I am not certain this will meet your needs. As a result, I don't believe the described approach will be possible and may require a feature request. I will follow up with the development team to review the feasibility of this and either they or I will reply with the results.

### Response

**Marin Bratanov** commented on 03 Aug 2021

To add a little to what Eric said - you can Follow this page for news on row virtualization in the treelist: [https://feedback.telerik.com/blazor/1481171-support-for-row-virtualization.](https://feedback.telerik.com/blazor/1481171-support-for-row-virtualization.) I've added your Vote for it on your behalf, and to get emails for status updates (such as when a release is known), click the Follow button. At the moment, enabling: paging load on demand column virtualization (if you have many columns) are the ways to optimize the performance of the treelist. The load-on-demand may also let you optimize the database queries too, by requesting a smaller, filtered portion of data (e.g., something like select * from myTable where parentId=@theParentId) as opposed to pulling all the data at once. Another point I want to make is that if you don't actually have hierarchical data, you may want to use the grid which offers row virtualization. Perhaps this is just the plain sample but I had to mention it since I don't see hierarchy in this data. Lastly, I would also like to note that comparing a treelist component with a plain virtualized foreach loop (which is what the Virtualize component is), is a bit like comparing apples to oranges, because the treelist does so much more than a virtualized list and were you to start adding such functionality to the virtualize component, you'd quickly hit many snags (such as - hierarchy is very, very tricky to virtualize) and performance will start deteriorating fast.

### Response

**Jason** commented on 03 Aug 2021

Thanks guys I've looked at the options like Load on Demand etc and they don't really meet my needs. I've reimplemented it with a virtualized foreach loop for now. I managed to get it working with the hierarchy, and it also allows for better mouse over support (see my previous post). There are some features of Treelist that I would have loved to use, but paging is just too 2005 and would interfere with usability too much. A bit of a shame, but them the breaks. Thanks for your support. Cheers, Jason
