# Gantt support for a minutes view coming in a future release?

## Question

**Jer** asked on 09 Sep 2021

Great to see the new Gantt feature in update 2.26. We immediately starting implementation for tracking our publishing stages at Microsoft for shipping software updates to show the parallelism of the processes and easily identify the relative time each stage takes. This is a great improvement over a list in a table. Sadly, the current implementation of Gantt only supports days whilst our publishing stages take only a few minutes or hours. I'm hoping additional support for a minutes view is coming soon as we had to shelve implementation of a Gantt view of publishing stages using your Gantt chart for the time being. If it's not coming, an announcement of it's in the road map plan or not coming would be greatly appreciated by your marketing team.

### Response

**Nadezhda Tacheva** commented on 14 Sep 2021

Hello Gary, As per the Gantt component specifics and configuration it provides four different views (Day, Week, Month and Year). The smallest (Day view) uses slots with one hour duration. As you correctly stated, it indeed does not support dividing the Timeline into minute segments. However, this looks like a meaningful use case and since this feature is not included in our roadmap to provide it out of the box, I can suggest a possible workaround to achieve your desired scenario. I will prepare and send it once done. Thank you for your patience in the interim!

### Response

**Nadezhda Tacheva** commented on 14 Sep 2021

Hi Gary, You can try the following: Set higher value for the SlotWidth of the Gantt Day View, so it can fit the sections for the minutes. Apply conditional styles for the Day view and set striped background for the slot cells, so they appear divided in sections. You can use something like this to generate the background - [https://stripesgenerator.com/.](https://stripesgenerator.com/.) Depending on the chosen slot width you can calculate and generate the necessary stripes. Check the sample below for reference. You may also set background for the header cells holding the hour values to mark the minutes (it can be an image for example). @if (SelectedView==GanttView.Day)
{
<style>
.k-gantt-columns td {
background-image: linear-gradient( 90 deg, rgba( 0, 0, 0, 0.08 ) 2.08 %, #fff0 2.08%, #fff0 50%, rgba(0, 0, 0, 0.08) 50%, rgba(0, 0, 0, 0.08) 52.08%, #fff0 52.08%, #fff0 100%); background-size: 20.00 px;
}
</style>
}

<TelerikGantt Data="@Data" @bind-View="@SelectedView" Width="1000px" Height="600px" IdField="Id" ParentIdField="ParentId" OnUpdate="@UpdateItem" OnDelete="@DeleteItem">
<GanttViews>
<GanttDayView SlotWidth="600" RangeStart="@(new DateTime(2021, 7, 5, 0, 0, 0))" RangeEnd="@(new DateTime(2021, 8, 31, 0, 0, 0))">
</GanttDayView>
<GanttWeekView SlotWidth="100" RangeStart="@(new DateTime(2021, 7, 5, 0, 0, 0))" RangeEnd="@(new DateTime(2021, 10, 1, 0, 0, 0))">
</GanttWeekView>
</GanttViews>
<GanttColumns>
<GanttColumn Field="Title" Expandable="true" Width="160px" Title="Task Title">
</GanttColumn>
<GanttColumn Field="PercentComplete" Title="Status" Width="60px">
</GanttColumn>
<GanttColumn Field="Start" Width="100px" DisplayFormat="{0:d}">
</GanttColumn>
<GanttColumn Field="End" Width="100px" DisplayFormat="{0:d}">
</GanttColumn>
</GanttColumns>
</TelerikGantt>

@code { public GanttView SelectedView { get; set; }=GanttView.Day;

List<FlatModel> Data { get; set; } class FlatModel { public int Id { get; set; } public int? ParentId { get; set; } public string Title { get; set; } public double PercentComplete { get; set; } public DateTime Start { get; set; } public DateTime End { get; set; }
} public int LastId { get; set; }=1; protected override void OnInitialized ( ) {
Data=new List<FlatModel>(); var random=new Random(); for ( int i=1; i <6; i++)
{ var newItem=new FlatModel()
{
Id=LastId,
Title="Task " + i.ToString(),
Start=new DateTime( 2021, 7, 5, 10, 15, 0 + i),
End=new DateTime( 2021, 7, 11 + i),
PercentComplete=Math.Round(random.NextDouble(), 2 )
};

Data.Add(newItem); var parentId=LastId;
LastId++; for ( int j=0; j <5; j++)
{
Data.Add( new FlatModel()
{
Id=LastId,
ParentId=parentId,
Title=" Task " + i + " : " + j.ToString(),
Start=new DateTime( 2021, 7, 5 + j),
End=new DateTime( 2021, 7, 6 + i + j),
PercentComplete=Math.Round(random.NextDouble(), 2 )
});

LastId++;
}
} base.OnInitialized();
} private void UpdateItem ( GanttUpdateEventArgs args ) { var item=args.Item as FlatModel; var foundItem=Data.FirstOrDefault(i=> i.Id.Equals(item.Id)); if (foundItem !=null )
{
foundItem.Title=item.Title;
foundItem.Start=item.Start;
foundItem.End=item.End;
foundItem.PercentComplete=item.PercentComplete;
}
} private void DeleteItem ( GanttDeleteEventArgs args ) { var item=Data.FirstOrDefault(i=> i.Id.Equals((args.Item as FlatModel).Id));

RemoveChildRecursive(item);
} private void RemoveChildRecursive ( FlatModel item ) { var children=Data.Where(i=> item.Id.Equals(i.ParentId)).ToList(); foreach ( var child in children)
{
RemoveChildRecursive(child);
}

Data.Remove(item);
}
} Please consider and let me know your thoughts on the suggested approach.

### Response

**Jerdobi** commented on 23 Sep 2021

Nadezhda Tacheva Thanks for the code. I make my attempt to implement and it's getting close. There are some rough edges: 1. The data is for 1 hour and the view shows 24-hours when the view should be just the Range. 2. Some items are just a few minutes and really need the view to zoom to the range. So, if the range was 1 hour, the view zooms to show just one hour and you see way more details. 3. Some strange behavior for the rows (see image). Hard to describe. I gave you some data in a Json string that if you want to play with it you can de-serialize the data into the your code. Just a bit too rough around the edges for me to use this approach. They expect perfection here. Maybe you can use this scenario to move the needle and make some impact. Gary Image of Gantt: [https://ibb.co/gRPKHJX](https://ibb.co/gRPKHJX) Data: [{"Id":1,"ParentId":null,"Title":"ARM64 - Succeeded","PercentComplete":0.98,"Start":"2021-09-23T01:24:11.0404792Z","End":"2021-09-23T02:29:04.7481454Z"},{"Id":2,"ParentId":1,"Title":" PkgSvc Package Translation","PercentComplete":0.81,"Start":"2021-09-23T01:24:11.0404792Z","End":"2021-09-23T01:24:12.3373555Z"},{"Id":3,"ParentId":1,"Title":" Submit to Submission Service","PercentComplete":0.79,"Start":"2021-09-23T01:24:12.5404807Z","End":"2021-09-23T01:24:23.3842428Z"},{"Id":4,"ParentId":1,"Title":" Wait for Build Chunks","PercentComplete":0.93,"Start":"2021-09-23T01:25:15.357Z","End":"2021-09-23T01:29:54.6579462Z"},{"Id":5,"ParentId":1,"Title":" Core Packaging","PercentComplete":0.11,"Start":"2021-09-23T01:29:54.9548215Z","End":"2021-09-23T02:29:04.7481454Z"},{"Id":6,"ParentId":null,"Title":"X64 - Succeeded","PercentComplete":0.67,"Start":"2021-09-23T01:24:10.9467291Z","End":"2021-09-23T01:55:36.7426484Z"},{"Id":7,"ParentId":6,"Title":" PkgSvc Package Translation","PercentComplete":0.56,"Start":"2021-09-23T01:24:10.9467291Z","End":"2021-09-23T01:24:12.2436055Z"},{"Id":8,"ParentId":6,"Title":" Submit to Submission Service","PercentComplete":0.32,"Start":"2021-09-23T01:24:12.4467308Z","End":"2021-09-23T01:24:23.2904927Z"},{"Id":9,"ParentId":6,"Title":" Wait for Build Chunks","PercentComplete":0.9,"Start":"2021-09-23T01:25:14.043Z","End":"2021-09-23T01:29:23.2190182Z"},{"Id":10,"ParentId":6,"Title":" Core Packaging","PercentComplete":0.19,"Start":"2021-09-23T01:29:23.4065185Z","End":"2021-09-23T01:55:36.7426484Z"}]

## Answer

**Nadezhda Tacheva** answered on 27 Sep 2021

Hi Gary, This indeed seems like not so easy scenario to cover. I additionally discussed this case with the development team and while providing minutes view is not on our roadmap, we are considering allowing the creation of custom views for the Gantt Timeline. This will allow the developers to create the necessary view to match the application needs. That said, I opened a request for such a feature on your behalf in our public
