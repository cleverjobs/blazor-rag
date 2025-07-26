# Is Scheduler first column editable?

## Question

**Had** asked on 02 Aug 2024

Hi there, Is there any way to edit/modify the first column? I mean, I would like to add some button, image, etc to the column. Like i show in the next image. There's any template to recreate this behavior ? Here's some code from that example. Thanks in advance. SchedulerTelerik.razor @page "/schedulerTelerik" <div class="container"> <div class="d-flex justify-content-between gap-4"> <div class="input-group mb-3"> <div class="input-group-prepend"> <span class="input-group-text"> Change start date: </span> </div> <TelerikDateTimePicker @bind-Value="@startDate" Class="form-control" /> </div> <div class="input-group mb-3"> <div class="input-group-prepend"> <span class="input-group-text"> Change end date: </span> </div> <TelerikDateTimePicker @bind-Value="@endDate" Class="form-control" /> </div> <div class="input-group mb-3"> <div class="input-group-prepend"> <span class="input-group-text"> Change slot duration: </span> </div> <TelerikNumericTextBox @bind-Value="@slotDuration" Class="form-control" /> </div> </div> <br /> <TelerikScheduler Data="@appointments" @bind-Date="@startDate" @bind-View="@currentView" Height="800px" AllowCreate="true" AllowDelete="true" AllowUpdate="true"> <SchedulerViews> <SchedulerTimelineView StartTime="@startTime" EndTime="@endTime" SlotDuration="@slotDuration" SlotDivisions="@slotDivision" ColumnWidth="@columnWidth" /> </SchedulerViews> <SchedulerResources> <SchedulerResource Field="Team" Title="Edit team" Data="@schedulerResources"> </SchedulerResource> </SchedulerResources> <SchedulerSettings> <SchedulerGroupSettings Resources="@groupingResources" Orientation="@SchedulerGroupOrientation.Vertical"> </SchedulerGroupSettings> </SchedulerSettings> </TelerikScheduler> </div> SchedulerTelerik.razor.cs using Telerik.Blazor; using Telerik.FontIcons; namespace TelerikComponentsTest.Pages { public partial class SchedulerTelerik { # region Auxiliar classes public class SchedulerAppointment { public Guid Id { get; set; } public string Title { get; set; } public string Description { get; set; } public DateTime Start { get; set; }=DateTime.Now; public DateTime End { get; set; }=DateTime.Now.AddHours( 4 ); public bool IsAllDay { get; set; } public string RecurrenceRule { get; set; } public List<DateTime> RecurrenceExceptions { get; set; } public Guid? RecurrenceId { get; set; } public FontIcon? Icon { get; set; } public SchedulerAppointment () {
Id=Guid.NewGuid();
}
} public class Resource { public string Text { get; set; } public string Value { get; set; } public string Color { get; set; }
} # endregion # region Dependency injection services // the following static classes mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MockupAppointmentService { private static List<SchedulerAppointment> _data { get; set; }=new List<SchedulerAppointment>(); public static async Task CreateAppointmentAsync ( SchedulerAppointment itemToInsert ) {
itemToInsert.Id=Guid.NewGuid();
_data.Insert( 0, itemToInsert);
} public static async Task<List<SchedulerAppointment>> ReadAppointmentAsync()=> await Task.FromResult(_data); public static async Task UpdateAppointmentAsync ( SchedulerAppointment itemToUpdate ) { var index=_data.FindIndex(i=> i.Id==itemToUpdate.Id); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
} public static async Task DeleteAppointmentAsync ( SchedulerAppointment itemToDelete ) { if (itemToDelete.RecurrenceId !=null )
{ // a recurrence exception was deleted, you may want to update // the rest of the data source - find an item where theItem.Id==itemToDelete.RecurrenceId // and remove the current exception date from the list of its RecurrenceExceptions } if (! string.IsNullOrEmpty(itemToDelete.RecurrenceRule) && itemToDelete.RecurrenceExceptions?.Count> 0 )
{ // a recurring appointment was deleted that had exceptions, you may want to // delete or update any exceptions from the data source - look for // items where theItem.RecurrenceId==itemToDelete.Id }

_data.Remove(itemToDelete);
}
} public static class MockupResourcesService { public static List<Resource> _resources { get; set; }=new List<Resource>() { new Resource()
{
Text="Alex",
Value="1",
Color="#99ffcc" }, new Resource()
{
Text="Bob",
Value="2",
Color="#47d147" }, new Resource()
{
Text="Charlie",
Value="3",
Color="#336600" }
}; public static async Task<List<Resource>> GetResourcesAsync()=> await Task.FromResult(_resources);
} # endregion # region Fields private DateTime
startDate=DateTime.Now.Date,
endDate=DateTime.Now.Date.AddDays( 1 ).AddHours( 10 ),

startTime=DateTime.Now.Date,
endTime=DateTime.Now.Date.AddHours( 23 ); private int slotDuration=60,
slotDivision=1,
columnWidth=80; private List<Resource> schedulerResources=new List<Resource>(); private List<SchedulerAppointment> appointments=new (); private List<string> groupingResources=new List<string> { "Team" }; private SchedulerView currentView=SchedulerView.Timeline; # endregion # region private methods private void GetSchedulerData ()=> appointments=new List<SchedulerAppointment>(); private async Task GetResources ()=> schedulerResources=await MockupResourcesService.GetResourcesAsync(); # endregion # region Life time cycle protected override async Task OnInitializedAsync () {
GetSchedulerData(); await GetResources(); await base.OnInitializedAsync();
} # endregion }
}

### Response

**Hadrian** commented on 14 Aug 2024

I am looking at other libraries to see if they have the functionality I need and I have found these for example: Syncfusion scheduler demo DevExpress scheduler demo Is there any way to achieve this functionality or is the functionality planned for the future?
