# TelerikScheduler OnUpdate not firing

## Question

**nel** asked on 01 Nov 2024

Hello. I'm having an issue with the Scheduler not firing it's OnUpdate event, OnDelete does. Tested with breakpoints, the Update handler is not breaking. Here is my markup: <Telerik.Blazor.Components.TelerikScheduler Height="500px" Data="@InternalTasks" @bind-Date="@StartDate" @bind-View="@CurrView" AllowCreate="false" AllowDelete="false" AllowUpdate="true" TitleField="@(nameof(ProjectTaskDto.DisplayTitle))" DescriptionField="@(nameof(ProjectTaskDto.Title))" TItem="ProjectTaskDto" OnUpdate="SchedulerUpdate"> <SchedulerViews> <Telerik.Blazor.Components.SchedulerDayView> </Telerik.Blazor.Components.SchedulerDayView> <Telerik.Blazor.Components.SchedulerWeekView> </Telerik.Blazor.Components.SchedulerWeekView> <Telerik.Blazor.Components.SchedulerMultiDayView NumberOfDays="10"> </Telerik.Blazor.Components.SchedulerMultiDayView> <Telerik.Blazor.Components.SchedulerMonthView ItemsPerSlot="6"> </Telerik.Blazor.Components.SchedulerMonthView> <Telerik.Blazor.Components.SchedulerTimelineView> </Telerik.Blazor.Components.SchedulerTimelineView> </SchedulerViews> </Telerik.Blazor.Components.TelerikScheduler> And here is my razor.cs code public partial class BasicScheduler {
List<ProjectTaskDto> InternalTasks=new List<ProjectTaskDto>();
DateTime StartDate { get; set; }=new DateTime( 2024, DateTime.Now.Month, 1 );
SchedulerView CurrView { get; set; }=SchedulerView.Month; protected override async Task OnInitializedAsync () {
InternalTasks.Add( new ProjectTaskDto
{
Title="Test",
DisplayTitle="Test",
Type=TaskType.Foundation,
StartDate=new DateTime( 2024, DateTime.Now.Month, 14 ),
EndDate=new DateTime( 2024, DateTime.Now.Month, 18 ),
}); await base.OnInitializedAsync();
} void SchedulerUpdate ( SchedulerUpdateEventArgs args ) {

}
} And the DTO here: public class ProjectTaskDto: FullAuditedEntityDto <Guid>
{ public string Title { get; set; } private string _displayTitle=null; public string DisplayTitle
{ get { return _displayTitle ?? Title;
} set {
_displayTitle=value;
}
} public TaskType Type { get; set; } public decimal? EstimatedPrice { get; set; } public decimal? ActualPrice { get; set; } public DateTime? StartDate { get; set; } public DateTime? EndDate { get; set; } public DateTime? Start
{ get { return StartDate;
} set {
StartDate=value;
}
} public DateTime? End
{ get { return EndDate;
} set {
EndDate=value;
}
} public Entities.TaskStatus Status { get; set; } public bool IsAppointment { get; set; } public Guid ProjectId { get; set; } public bool IsAllDay
{ get { return!IsAppointment;
}
} public string Class { get; set; } public List<BidDto> Bids { get; set; }
} Any help is appreciated.

### Response

**nelsonad** commented on 01 Nov 2024

I got it. It's because my IsAllDay property did not have a setter. I added one that does nothing and now it's firing.

## Answer

**nelsonad** answered on 01 Nov 2024

Properties updated by moving events around need a setter or the OnUpdate event will not fire. It fails silently without exceptions.

### Response

**Hristian Stefanov** commented on 04 Nov 2024

Hi Adam, I'm glad to hear that you have quickly resolved the matter on your own. Indeed, the IsAllDay property needs a setter so the model can be properly updated. Thank you for sharing how things turned out publicly so other developers in the same situation can benefit from this. Kind Regards, Hristian
