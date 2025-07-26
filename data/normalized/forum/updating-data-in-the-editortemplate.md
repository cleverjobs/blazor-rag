# Updating data in the EditorTemplate.

## Question

**Eno** asked on 06 Jan 2022

Hello, I can retrieve the correct data in the TelerikDropDownList but, when I try to update the column, I get a "Value cannot be null. (Parameter 'key')" error. The update functionality works for the other properties in the ActivityResource model. It gives me the error above when I try to update anything from the child models (Activity and Resource). Thanks for the help in advance! Models: public class ActivityResource { public int ActivityId { get; set; } public int ResourceId { get; set; } public double Sequence { get; set; } public DateTime ScheduledStart { get; set; } public DateTime ScheduledEnd { get; set; } public double ScheduledDuration { get; set; } public Activity Activity { get; set; } public Resource Resource { get; set; }
} public class Activity { public int Id { get; set; } public int Number { get; set; } public string Name { get; set; }="New Activity"; public string Description { get; set; } public ICollection<Resource> Resources { get; set; } public List<ActivityResource> ActivityResources { get; set; }

} public class Resource { public int Id { get; set; } public string Name { get; set; }="New Resource"; public string Description { get; set; } public int ResourceTypeId { get; set; } public virtual ResourceType ResourceType { get; set; } public ICollection<Activity> Activities { get; set; } public List<ActivityResource> ActivityResources { get; set; }
}

Controller: public async Task UpdateActivityResourceScheduleAsync ( ActivityResource schedule ) { // Getting the Schedule that is in the database. var targetedSchedule=_ctx.ActivityResources.FirstOrDefault(r=> r.ActivityId==schedule.ActivityId && r.ResourceId==schedule.ResourceId); bool resquence=false; if (targetedSchedule !=null )
{ if (targetedSchedule.Sequence !=schedule.Sequence)
{
resquence=true;
} // Assigning the properties. targetedSchedule.Sequence=schedule.Sequence;
targetedSchedule.ScheduledStart=schedule.ScheduledStart;
targetedSchedule.ScheduledEnd=schedule.ScheduledEnd;
targetedSchedule.ScheduledDuration=schedule.ScheduledDuration;
targetedSchedule.Activity=schedule.Activity;
targetedSchedule.Resource=schedule.Resource;
targetedSchedule.ActivityId=schedule.ActivityId;
targetedSchedule.ResourceId=schedule.ResourceId;
targetedSchedule.Activity=_ctx.Activities.FirstOrDefault(aId=> aId.Id==schedule.ActivityId);
targetedSchedule.Resource=_ctx.Resources.FirstOrDefault(rId=> rId.Id==schedule.ResourceId);



} // Updating the properties. _ctx.ActivityResources.Update(targetedSchedule); await _ctx.SaveChangesAsync();
}

Razor Page:
<TelerikGrid Data="@SchedulesList" Height="550px" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" Pageable="true" PageSize="20" Resizable="true" Reorderable="true" RowDraggable="true" OnStateInit="@((GridStateEventArgs<VentureBlazor.Models.ActivityResource> args)=> OnStateInit(args))" OnRowDrop="@((GridRowDropEventArgs<VentureBlazor.Models.ActivityResource> args)=> OnRowDropHandler(args))" EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandler" OnDelete="@DeleteHandler">
<DetailTemplate>
@{ var schedule=context as VentureBlazor.Models.ActivityResource;
<TelerikGrid Data="@schedule.Activity.Resources" Pageable="true" PageSize="5">
<GridColumns>
<GridColumn Field="Name"></GridColumn>
<GridColumn Field="Description"></GridColumn>
</GridColumns>
</TelerikGrid>

}
</DetailTemplate>
<GridToolBar>
@* <GridCommandButton Command="Add" Icon="plus" Primary="true">Add Schedule</GridCommandButton>
*@</GridToolBar>
<GridColumns>
@* <GridColumn Field="@(nameof(VentureBlazor.Models.ActivityResourceSchedule.Id))" Editable="false" />
*@<GridColumn Title="Activity Id" Field="Activity.Id" Editable="false" />
<GridColumn Title="Resource Id" Field="Resource.Id" Editable="false" />
<GridColumn Field="@(nameof(VentureBlazor.Models.ActivityResource.Sequence))" />
<GridColumn Field="@(nameof(VentureBlazor.Models.ActivityResource.ScheduledStart))" />
<GridColumn Field="@(nameof(VentureBlazor.Models.ActivityResource.ScheduledEnd))" />
<GridColumn Field="@(nameof(VentureBlazor.Models.ActivityResource.ScheduledDuration))" />
<GridColumn Title="Activity Name" Field="@(nameof(VentureBlazor.Models.ActivityResource.ActivityId))">
<EditorTemplate>
@{
CurrentlyEditedSchedule=context as VentureBlazor.Models.ActivityResource;
<TelerikDropDownList Data="@ActivitiesList" @bind-Value="@CurrentlyEditedSchedule.ActivityId" TextField="@nameof(Activity.Name)" ValueField="@nameof(Activity.Id)">

</TelerikDropDownList>
}
</EditorTemplate>
<Template>
@{ int aId=(context as VentureBlazor.Models.ActivityResource).ActivityId;
Activity matchingPos=ActivitiesList.FirstOrDefault(a=> a.Id==aId); string textToRender=matchingPos !=null? matchingPos.Name : "Unknown";
<text>@textToRender</text>
}
</Template>
</GridColumn>
<GridColumn Title="Resource Name" Field="@(nameof(VentureBlazor.Models.ActivityResource.ResourceId))">
<EditorTemplate>
@{
CurrentlyEditedSchedule=context as VentureBlazor.Models.ActivityResource;
<TelerikDropDownList Data="@ResourcesList" @bind-Value="@CurrentlyEditedSchedule.ResourceId" TextField="@nameof(VentureBlazor.Models.Resource.Name)" ValueField="@nameof(VentureBlazor.Models.Resource.Id)">

</TelerikDropDownList>
}
</EditorTemplate>
<Template>
@{ int rId=(context as VentureBlazor.Models.ActivityResource).ResourceId;
VentureBlazor.Models.Resource matchingPos=ResourcesList.FirstOrDefault(r=> r.Id==rId); string textToRender=matchingPos !=null? matchingPos.Name : "Unknown";
<text>@textToRender</text>
}
</Template>
</GridColumn>
<GridCommandColumn Width="200px" Resizable="false">
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit" Primary="true">Edit</GridCommandButton>
<GridCommandButton Command="Delete" Icon="delete">Delete</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { private List<VentureBlazor.Models.ActivityResource> SchedulesList { get; set; } private List<VentureBlazor.Models.Activity> ActivitiesList { get; set; } private List<VentureBlazor.Models.Resource> ResourcesList { get; set; } private VentureBlazor.Models.ActivityResource CurrentlyEditedSchedule { get; set; } private VentureBlazor.Models.Activity NewActivity=new VentureBlazor.Models.Activity(); private VentureBlazor.Models.Resource NewResource=new VentureBlazor.Models.Resource(); private ActivityScheduleRepository repo; int selectedValue { get; set; } protected override async Task OnInitializedAsync ( ) {
repo=new ActivityScheduleRepository(ContextFactory.CreateDbContext()); await LoadSchedules();
} public async Task LoadSchedules ( ) {
SchedulesList=await repo.GetAllActivityResourceSchedulesAsync();
ActivitiesList=await repo.GetAllActivitiesAsync();
ResourcesList=await repo.GetAllResourcesAsync();
} public async Task UpdateHandler ( GridCommandEventArgs args ) { await repo.UpdateActivityResourceScheduleAsync((VentureBlazor.Models.ActivityResource)args.Item); await LoadSchedules();
}

}

### Response

**Marin Bratanov** commented on 08 Jan 2022

Sounds like a null reference where a null check is missing before accessing a collection member. This might be somewhere in the models or the context, but does not look like an issue with the UI. You should probably review the stack trace of the error to see where it comes from so you can add appropriate defensive checks.
