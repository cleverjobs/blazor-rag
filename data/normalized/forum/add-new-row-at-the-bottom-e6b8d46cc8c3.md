# Add new row at the bottom

## Question

**loeloe** asked on 15 Mar 2021

Hi Is there a way to programmatically trigger the "Add" Command and have the new row displayed as the last item of the grid?

## Answer

**Nadezhda Tacheva** answered on 18 Mar 2021

Hi Monika, You can programmatically trigger the "Add" command through the Grid State. An example of such setup is available here - Initiate Editing or Inserting of an Item. The sample also demonstrates how to programmatically set item in edit mode (if needed at some point). With the current Grid structure, the newly added item will appear at the top of the Grid. However, as I consider your request for ability to add the new row at the bottom of the Grid page, I opened a feature request on your behalf in our public feedback portal - Add new row at the bottom of the page. You are subscribed to receive email notifications when its status changes (this is the best way to know when a feature is implemented as we announce such information in the portal). I've also added your vote to keep proper track of the request. In the meantime, depending on your specific scenario and the data you are working with, another approach you might want to try is to use Observable collection (the Telerik components subscribe to its CollectionChanged event to update). Using its Add method will append the new item at the end of the collection - an example is available here (a drawback of this approach could be if you deal with a long list of data, as the item will be added at the end of the collection, on the last page, the user might find it hard to notice if a new item has been added. In this case you can add a Notification for example). The above mentioned approach could also be achieved by creating a new collection reference (in case you don't want to use Observable data). Here is a sample of implementing it: @* Add/ remove employee to see how the Grid reacts to that change. *@<TelerikButton OnClick="@AddEmployee">Add employee</TelerikButton>

<TelerikButton OnClick="@RemoveEmployee">Remove last employee</TelerikButton>

<TelerikGrid Data="@MyData" Height="400px" Pageable="true" Sortable="true">
<GridColumns>
<GridColumn Field="@(nameof(SampleData.Id))" Width="120px" />
<GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" />
<GridColumn Field="@(nameof(SampleData.Team))" Title="Team" />
<GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code { void AddEmployee ( ) { var x=MyData.Count + 1;
MyData.Add( new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
});
MyData=new List<SampleData>(MyData);
} void RemoveEmployee ( ) { if (MyData.Count> 0 )
{
MyData.RemoveAt(MyData.Count - 1 );
MyData=new List<SampleData>(MyData);
}
} public List<SampleData> MyData=Enumerable.Range( 1, 5 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}).ToList(); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Nadezhda Tacheva Progress Telerik

### Response

**loe** answered on 18 Mar 2021

Thanks a lot for these detailed inputs!

### Response

**Nadezhda Tacheva** answered on 23 Mar 2021

Hi Monika, Another approach you might want to try that comes to my mind is the following: Use the Grid State to programmatically initiate new item insertion and also pass the position you want to insert the item at (last position on the current page). That position could be calculated based on the page size times current page minus 1 (as the indexes start from 0). With this setup on insert you will have the editors displayed at the top of the Grid but on save the item will be added at the bottom of the page (see the attached project for reference, comments in the code for more details on the spot). Regards, Nadezhda Tacheva Progress Telerik
