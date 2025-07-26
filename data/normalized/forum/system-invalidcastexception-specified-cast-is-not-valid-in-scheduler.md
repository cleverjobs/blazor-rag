# System.InvalidCastException: Specified cast is not valid. in Scheduler

## Question

**Maa** asked on 05 May 2023

Copied a demo TelerikScheduler: <TelerikScheduler Data="@RFCactions" @bind-Date="@StartDate" Height="600px" @bind-View="@CurrView" AllowCreate="false" AllowDelete="false" AllowUpdate="false" ConfirmDelete="true" IdField="@(nameof(RequestForChangeActionSched.Id))" StartField="@(nameof(RequestForChangeActionSched.StartingDate))" EndField="@(nameof(RequestForChangeActionSched.EndingDate))" IsAllDayField="@(nameof(RequestForChangeActionSched.IsAllDay))" TitleField="@(nameof(RequestForChangeActionSched.RequestForChangeId).ToString())" DescriptionField="@(nameof(RequestForChangeActionSched.Activity))"> <SchedulerViews> <SchedulerDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerWeekView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerMultiDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" NumberOfDays="31" SlotDivisions="4"> <DateHeaderTemplate> <div> @context.ToString("ddd dd") </div> </DateHeaderTemplate> </SchedulerMultiDayView> <SchedulerMonthView></SchedulerMonthView> <SchedulerTimelineView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> </SchedulerViews> </TelerikScheduler> @code { List<RequestForChangeActionSched> RFCactions=new List<RequestForChangeActionSched>(); ....etc Made sure all required fields are in my model, with the same datatypes But the (any) view won't show because of an InvalidCastException Updated from V2023.1.313.33 to V2023.1.426.51 but still got the cast error at blazor.webassembly.js:1 System.InvalidCastException: Specified cast is not valid. at Telerik.Blazor.Components.TelerikScheduler`1[[MISFrontEnd.Shared.Domain.RequestForChangeActionSched, MISFrontEnd.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].UpdateAppointment(RequestForChangeActionSched dataItem, IAppointment appointmentForUpdate) at Telerik.Blazor.Components.TelerikScheduler`1[[MISFrontEnd.Shared.Domain.RequestForChangeActionSched, MISFrontEnd.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].CreateAppointment(RequestForChangeActionSched dataItem) at Telerik.Blazor.Components.TelerikScheduler`1[[MISFrontEnd.Shared.Domain.RequestForChangeActionSched, MISFrontEnd.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].ExpandAppointments()

### Response

**Hristian Stefanov** commented on 09 May 2023

Hi Maarten, I have carefully reviewed the provided code. It seems that the configuration is OK. To investigate the issue further, I attempted to replicate the problem by referring to your Scheduler structure, substituting the actual data with dummy data. On my end, the component appeared to be functioning properly - without any errors. I'm sharing the sample via this REPL link for your reference, so you can compare it with the actual project to determine if anything is missing or if there are other factors that may be causing the issue. If the problem persists, modify the REPL sample to demonstrate the problematic behavior in a self-contained, runnable manner. This will enable me to conduct a more thorough investigation of the scenario with a configuration that closely resembles the actual environment. I eagerly anticipate hearing an update from you. Kind Regards, Hristian

### Response

**Maarten** commented on 09 May 2023

Hi Hristian, Thanks a lot for your reply. Your code on REPL looks very much as the example that I used for my scheduler code. My source (Data) however is a MSSQL table. I can't get that into REPL(?). protected async Task<List<RequestForChangeActionSched>> ReadActionItems()
{
DateTime sd=new DateTime(StartDate.Year, StartDate.Month, 1 ); var startDatum=sd.ToString( "s" ).Substring( 0, 10 ); var eindDatum=sd.AddMonths( 1 ).AddDays( -1 ).ToString( "s" ).Substring( 0, 10 ); int handledBy=163; var requestString=$"RequestForChangeAction/Raw?pageNumber=1&pageSize=200&Handledby={handledBy} &orderby=startingDate&ascending=false&ActionIsOpen=true&FromStartDate={startDatum} &TillStartDate={eindDatum} "; var rfcActions=new List<RequestForChangeActionSched>(); try { var result=await Http.GetFromJsonAsync<PageResultEnvelope<RequestForChangeActionSched>>(requestString);
rfcActions=result.CurrentPageData;
} catch (Exception e)
{
Notifier.NotifyError( "Error from Server" );
Notifier.NotifyError(e.Message);
} return rfcActions;
} In Fiddler I see a resultset of 150 records coming back. Microsoft Edge shows a empty scheduler page. When I open de DevTools, I see the Exception in the console, the moment a cell can be loaded (switch to dayview on a day w/o appontments and there will be no exception) so it happens on rendering of the data (obviously on a cast error) Here's my model: public class RequestForChangeActionSched: PageResult { public int? Modifiedby { get; set; } public int RequestForChangeId { get; set; } public int? RfcactivityNo { get; set; } public int? CreatedBy { get; set; } public string? ForDepartment { get; set; } public int? ForTeam { get; set; } public bool? NoProjectReport { get; set; } public bool? IsInSprint { get; set; } public bool? MakeWorkItem { get; set; } public string? WorkItemId { get; set; } public int? Handledby { get; set; } public ActivityStatus? ActivityStatus { get; set; } public DateTime StartingDate { get; set; } public bool? IsAppointment { get; set; } public DateTime EndingDate { get; set; } public bool? MakeRide { get; set; } public bool? SendFlowers { get; set; } public bool? SendNotice { get; set; } public DateTime? Deadline { get; set; } public int? ForecastMins { get; set; } public int? RealForecast { get; set; } public string Activity { get; set; } public string? Memo { get; set; } public int? DependantOnActionId { get; set; } public DateTime? ActionFinishedDate { get; set; } public int? ProcessingTimeMins { get; set; } public int? FinishedBy { get; set; } public int? MdlidChargedYn { get; set; } public string? NotifyDepartment { get; set; } public string? WorkInstruction { get; set; } public string? Document { get; set; } public bool? IsAfterwork { get; set; } public string? MondayBoardId { get; set; } public string? MondayItemId { get; set; } public bool? IsSubItem { get; set; } // Telerik Scheduler properties public bool IsAllDay { get; set; }=false; public string? RecurrenceRule { get; set; }=string.Empty; public List<DateTime>? RecurrenceExceptions { get; set; }=new (); public int? RecurrenceId { get; set; }
} Hopefully you can see what I am missing TIA Regards, Maarten

### Response

**Maarten** commented on 09 May 2023

Ok, just tried it with this model: public class RequestForChangeActionSched { public int? Id { get; set; } public int RequestForChangeId { get; set; } public DateTime StartingDate { get; set; } public bool? IsAppointment { get; set; } public DateTime EndingDate { get; set; } public string Activity { get; set; } // Telerik Scheduler properties public bool IsAllDay
{ get { if (IsDateTimeNullorEmpty(StartingDate))
{ return true;
} else { return false;
}
}
} public string? RecurrenceRule { get; } public List<DateTime>? RecurrenceExceptions { get; } public int? RecurrenceId { get; } public static bool IsDateTimeNullorEmpty ( DateTime? date ) { return!date.HasValue ? true: false;
}
} Still got the "Unhandled exception rendering component: Specified cast is not valid." Shoot me Regards, Maarten

### Response

**Hristian Stefanov** commented on 12 May 2023

Hi Maarten, Thank you for getting back to me with more information. After using the "RequestForChangeActionSched" model, I was able to reproduce the issue. Now let me shed some light below on the reason for the problem and the possible fix. The issue arises from the TitleField parameter, requiring it to be mapped to a string property of the model. Consequently, direct casting is not allowed in this parameter declaration. However, there are two possible approaches to rectify the error and ensure the smooth functioning of the "RequestForChangeActionSched" model: Incorporate a new string property into the model. Subsequently, within its getter, perform a cast on the "RequestForChangeId" value and assign the TitleField to the newly introduced string property. To provide further clarity, I have prepared an illustrative example for your convenience (refer to the highlighted sections): <TelerikScheduler Data="@Appointments" @bind-Date="@StartDate" Height="600px" AllowCreate="false" AllowDelete="false" AllowUpdate="false" ConfirmDelete="true" IdField="@(nameof(RequestForChangeActionSched.Id))" StartField="@(nameof(RequestForChangeActionSched.StartingDate))" EndField="@(nameof(RequestForChangeActionSched.EndingDate))" IsAllDayField="@(nameof(RequestForChangeActionSched.IsAllDay))" TitleField="@(nameof(RequestForChangeActionSched.RequestForChangeIdText))" DescriptionField="@(nameof(RequestForChangeActionSched.Activity))"> <SchedulerViews> <SchedulerDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerWeekView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerMultiDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" NumberOfDays="31" SlotDivisions="4"> <DateHeaderTemplate> <div> @context.ToString("ddd dd") </div> </DateHeaderTemplate> </SchedulerMultiDayView> <SchedulerMonthView> </SchedulerMonthView> <SchedulerTimelineView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> </SchedulerViews> </TelerikScheduler> @code {
public DateTime StartDate { get; set; }=new DateTime(2019, 12, 2);
//the time portions are important
public DateTime DayStart { get; set; }=new DateTime(2000, 1, 1, 8, 0, 0);
public DateTime DayEnd { get; set; }=new DateTime(2000, 1, 1, 20, 0, 0);
public DateTime WorkDayStart { get; set; }=new DateTime(2000, 1, 1, 9, 0, 0);
public DateTime WorkDayEnd { get; set; }=new DateTime(2000, 1, 1, 17, 0, 0);
List <RequestForChangeActionSched> Appointments=new List <RequestForChangeActionSched> ()
{
new RequestForChangeActionSched
{
Id=0,
RequestForChangeId=10,
Activity="Q4 is coming to a close, review the details.",
StartingDate=new DateTime(2019, 12, 5, 10, 00, 0),
EndingDate=new DateTime(2019, 12, 5, 11, 30, 0)
},

new RequestForChangeActionSched
{
Id=1,
RequestForChangeId=11,
Activity="The cat needs vaccinations and her teeth checked.",
StartingDate=new DateTime(2019, 12, 2, 11, 30, 0),
EndingDate=new DateTime(2019, 12, 2, 12, 0, 0)
},

new RequestForChangeActionSched
{
Id=2,
RequestForChangeId=12,
Activity="Kick off the new project.",
StartingDate=new DateTime(2019, 12, 6, 9, 30, 0),
EndingDate=new DateTime(2019, 12, 6, 12, 45, 0)
},

new RequestForChangeActionSched
{
Id=3,
RequestForChangeId=13,
Activity="An unforgettable holiday!",
StartingDate=new DateTime(2019, 11, 27),
EndingDate=new DateTime(2019, 12, 05)
}
};

protected override void OnInitialized()
{

base.OnInitialized();
}

public class RequestForChangeActionSched
{
public int? Id { get; set; }
public int RequestForChangeId { get; set; } public string RequestForChangeIdText { get { return this.RequestForChangeId.ToString(); } } public DateTime StartingDate { get; set; }
public bool? IsAppointment { get; set; }
public DateTime EndingDate { get; set; }
public string Activity { get; set; }

// Telerik Scheduler properties
public bool IsAllDay
{
get
{
if (IsDateTimeNullorEmpty(StartingDate))
{
return true;
}
else
{
return false;
}
}
}
public string? RecurrenceRule { get; }
public List <DateTime>? RecurrenceExceptions { get; }
public int? RecurrenceId { get; }

public static bool IsDateTimeNullorEmpty(DateTime? date)
{
return !date.HasValue ? true : false;
}
}
} Create a DTO model based on the "RequestForChangeActionSched" model and ensure that all properties are appropriately mapped. Within the DTO, modify the "RequestForChangeId" property to accommodate a string type. During the mapping process, you can perform a cast operation to convert the original integer value. Below I have prepared an illustrative example showcasing this approach as well: <TelerikScheduler Data="@AppointmentsDTO" @bind-Date="@StartDate" Height="600px" AllowCreate="false" AllowDelete="false" AllowUpdate="false" ConfirmDelete="true" IdField="@(nameof(RequestForChangeActionSchedDTO.Id))" StartField="@(nameof(RequestForChangeActionSchedDTO.StartingDate))" EndField="@(nameof(RequestForChangeActionSchedDTO.EndingDate))" IsAllDayField="@(nameof(RequestForChangeActionSchedDTO.IsAllDay))" TitleField="@(nameof(RequestForChangeActionSchedDTO.RequestForChangeId))" DescriptionField="@(nameof(RequestForChangeActionSchedDTO.Activity))"> <SchedulerViews> <SchedulerDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerWeekView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> <SchedulerMultiDayView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" NumberOfDays="31" SlotDivisions="4"> <DateHeaderTemplate> <div> @context.ToString("ddd dd") </div> </DateHeaderTemplate> </SchedulerMultiDayView> <SchedulerMonthView> </SchedulerMonthView> <SchedulerTimelineView StartTime="@DayStart" EndTime="@DayEnd" WorkDayStart="@WorkDayStart" WorkDayEnd="@WorkDayEnd" /> </SchedulerViews> </TelerikScheduler> @code {
public DateTime StartDate { get; set; }=new DateTime(2019, 12, 2);
//the time portions are important
public DateTime DayStart { get; set; }=new DateTime(2000, 1, 1, 8, 0, 0);
public DateTime DayEnd { get; set; }=new DateTime(2000, 1, 1, 20, 0, 0);
public DateTime WorkDayStart { get; set; }=new DateTime(2000, 1, 1, 9, 0, 0);
public DateTime WorkDayEnd { get; set; }=new DateTime(2000, 1, 1, 17, 0, 0); List <RequestForChangeActionSchedDTO> AppointmentsDTO=new List <RequestForChangeActionSchedDTO> (); List <RequestForChangeActionSched> Appointments=new List <RequestForChangeActionSched> ()
{
new RequestForChangeActionSched
{
Id=0,
RequestForChangeId=10,
Activity="Q4 is coming to a close, review the details.",
StartingDate=new DateTime(2019, 12, 5, 10, 00, 0),
EndingDate=new DateTime(2019, 12, 5, 11, 30, 0)
},

new RequestForChangeActionSched
{
Id=1,
RequestForChangeId=11,
Activity="The cat needs vaccinations and her teeth checked.",
StartingDate=new DateTime(2019, 12, 2, 11, 30, 0),
EndingDate=new DateTime(2019, 12, 2, 12, 0, 0)
},

new RequestForChangeActionSched
{
Id=2,
RequestForChangeId=12,
Activity="Kick off the new project.",
StartingDate=new DateTime(2019, 12, 6, 9, 30, 0),
EndingDate=new DateTime(2019, 12, 6, 12, 45, 0)
},

new RequestForChangeActionSched
{
Id=3,
RequestForChangeId=13,
Activity="An unforgettable holiday!",
StartingDate=new DateTime(2019, 11, 27),
EndingDate=new DateTime(2019, 12, 05)
}
};

protected override void OnInitialized()
{ AppointmentsDTO=Appointments.Select(x=> new RequestForChangeActionSchedDTO
{
Id=x.Id,
RequestForChangeId=x.RequestForChangeId.ToString(),
Activity=x.Activity,
StartingDate=x.StartingDate,
EndingDate=x.EndingDate
}).ToList(); base.OnInitialized();
} public class RequestForChangeActionSchedDTO
{
public int? Id { get; set; }
public string RequestForChangeId { get; set; }
public DateTime StartingDate { get; set; }
public bool? IsAppointment { get; set; }
public DateTime EndingDate { get; set; }
public string Activity { get; set; }

// Telerik Scheduler properties
public bool IsAllDay
{
get
{
if (IsDateTimeNullorEmpty(StartingDate))
{
return true;
}
else
{
return false;
}
}
}
public string? RecurrenceRule { get; }
public List <DateTime>? RecurrenceExceptions { get; }
public int? RecurrenceId { get; }

public static bool IsDateTimeNullorEmpty(DateTime? date)
{
return !date.HasValue ? true : false;
}
} public class RequestForChangeActionSched
{
public int? Id { get; set; }
public int RequestForChangeId { get; set; }
public DateTime StartingDate { get; set; }
public bool? IsAppointment { get; set; }
public DateTime EndingDate { get; set; }
public string Activity { get; set; }

// Telerik Scheduler properties
public bool IsAllDay
{
get
{
if (IsDateTimeNullorEmpty(StartingDate))
{
return true;
}
else
{
return false;
}
}
}
public string? RecurrenceRule { get; }
public List <DateTime>? RecurrenceExceptions { get; }
public int? RecurrenceId { get; }

public static bool IsDateTimeNullorEmpty(DateTime? date)
{
return !date.HasValue ? true : false;
}
}
} I remain at your disposal if the issue still appears. Kind Regards, Hristian

### Response

**Maarten** commented on 12 May 2023

Hi Hristian, Thank you so much for finding this error. I realised TitleField needs to be a string but my approche caused the exception. Your solution works like a charm: You're a true lifesaver. Tnx! Maarten

## Answer

**Maarten** answered on 12 May 2023

Hristian came with the correct solution Regards, Maarten
