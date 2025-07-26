# Gantt Timeline Rendering

## Question

**Eno** asked on 25 Jan 2022

Hello, right now, I am getting the "Object reference not set to an instance of an object." error for rendering the Gantt Timeline. I'm not sure how to send the data from the Gantt Tree to the timeline or setting the timeline to the correct model. The tree renders just fine. Help with understanding Data Binding with the parameters (IdField, ParentIdField, ItemsField, HasChildrenField) will be great as well. Razor Page: <TelerikGantt Data="@SchedulesList" @bind-View="@SelectedView" IdField="Id" ParentIdField="" Width="100%" Height="600px" Sortable="true" SortMode="@SortMode.Multiple" FilterMode="@GanttFilterMode.FilterMenu" FilterMenuType="@FilterMenuType.Menu"> <GanttViews> <GanttDayView> </GanttDayView> <GanttWeekView> </GanttWeekView> <GanttMonthView> </GanttMonthView> <GanttYearView> </GanttYearView> </GanttViews> <GanttColumns> <GanttColumn Field="Sequence" Title="Sequence"> </GanttColumn> <GanttColumn Field="ScheduledStart" Title="Scheduled Start"> </GanttColumn> <GanttColumn Field="ScheduledEnd" Title="Scheduled End"> </GanttColumn> <GanttColumn Field="ScheduledDuration" Title="Scheduled Duration"> </GanttColumn> <GanttColumn Field="Activity.Name" Title="Activity Name"> </GanttColumn> <GanttColumn Field="Resource.Name" Title="Resource Name"> </GanttColumn> </GanttColumns> </TelerikGantt> @code {
private List <VentureBlazor.Models.ActivityResource> SchedulesList { get; set; }
private List <VentureBlazor.Models.Activity> ActivitiesList { get; set; }
private List <VentureBlazor.Models.Resource> ResourcesList { get; set; }
private ActivityScheduleRepository repo;
public GanttView SelectedView { get; set; }=GanttView.Year;

protected override async Task OnInitializedAsync()
{
repo=new ActivityScheduleRepository(ContextFactory.CreateDbContext());
await LoadSchedules();

base.OnInitialized();

}

public async Task LoadSchedules()
{
ActivitiesList=await repo.GetAllActivitiesAsync();
ResourcesList=await repo.GetAllResourcesAsync();
SchedulesList=await repo.GetAllActivityResourceSchedulesAsync();

}

public void Dispose()
{
repo.Dispose();
}
} Model:

public class ActivityResource
{
[Key]
public int Id { get; set; }
public int ActivityId { get; set; }

public int ResourceId { get; set; }

public double Sequence { get; set; }

public DateTime ScheduledStart { get; set; }

public DateTime ScheduledEnd { get; set; }

public double ScheduledDuration { get; set; }

public Activity Activity { get; set; }

public Resource Resource { get; set; }
}

public class Resource
{
public int Id { get; set; }
public string Name { get; set; }="New Resource";
public string Description { get; set; }

public int ResourceTypeId { get; set; }
public virtual ResourceType ResourceType { get; set; }

public ICollection <Activity> Activities { get; set; }
public ICollection <Project> Projects { get; set; }

public List <ActivityResource> ActivityResources { get; set; }
public List <ProjectActivity> ProjectActivities { get; set; }

}

## Answer

**Nadezhda Tacheva** answered on 28 Jan 2022

Hello Enoch, Although the Gantt contains two child components ( Gantt Tree and Gantt Timeline), it essentially works as a whole and once you provide the data source to the Gantt component, both of its parts have access to it but render it in a different manner - the Tree displays the data in a tree-like structure including the declared columns and the Timeline provides visual representation of the Gantt records in a timeline view. Having this in mind, you do not need to additionally send the data to the Timeline as it already can access it. However, you should provide the data and the necessary fields in the correct way, so both the Tree and the Timeline render it properly. In terms of correct data binding, it is important to first define what kind of data you will pass to the Gantt (flat or hierarchical), as the data binding approach will defer based on the type. So, I suggest you first take a look at the two types of data structures: Flat data - in this case the entire collection of Gantt items is available at one level and the parent-child relationships are created through internal data in the model using the Id and ParentId fields which should be provided to the Gantt. Hierarchical Data - in this case the collection of child items is provided in a field of its parent's model. You should provide this child items field to the Items parameter of the Gantt. Based on the given snippets, it looks like the Gannt data ( SchedulesList ) is a collection of flat data model ( ActivityResource ). When dealing with flat data, you should provide IdField and ParentIdField to the Gannt, so it can organize the parent-child relationships. If the corresponding fields in your model are matching the default names (Id and ParentId), it is not necessary to set IdField and ParentIdField explicitly as the Gantt will read them automatically form the data. However, if these fields in your model are named differently, you should point them to the Gantt's IdField and ParentIdField. Apart from that, I also see that the ActivityResource model is a complex one, so for handling this I suggest you take a look at the Bind to nested (navigation) properties in complex objects knowledge base article. Although it lists examples using Grid, the data binding approach is the same. For the data binding of the nested properties, you should use a nested model name different than the model itself. For example, instead of public class ActivityResource {
... public Activity Activity { get; set; }

...
} use something like this public class ActivityResource {
... public Activity CurrResourceActivity { get; set; }

...
} And then for the field binding use this name: ... <GanttColumn Field="CurrResourceActivity.Name" Title="Activity Name"> </GanttColumn>... I hope you will find the above information and resources useful to move forward with your application. Please let us know if any further questions appear. Regards, Nadezhda Tacheva
