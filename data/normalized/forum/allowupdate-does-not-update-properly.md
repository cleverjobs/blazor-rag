# AllowUpdate does not update properly?

## Question

**And** asked on 29 Jul 2020

I have the Scheduler's AllowUpdate property bound to a boolean property Timesheet.IsEditable. Expected behavior: When Timesheet.IsEditable is changed to "false," a user cannot drag and drop an entry. Observed behavior: When Timesheet.IsEditable is changed to "false," a user CAN drag and drop an entry. The workaround I'm using currently is private async Task UpdateEntry(SchedulerUpdateEventArgs args) { if (!Timesheet.IsEditable) return; // do actual business logic here } but this seems cludgy, and results in bad UX - the scheduler still looks as they it will allow the user to drag and drop and entry. I also have AllowCreate and AllowDelete bound to this same property, and they both behave as expected when Timesheet.IsEditable is toggled. Is this a bug? Or is there something I'm overlooking? Thanks, Andrew

## Answer

**Marin Bratanov** answered on 30 Jul 2020

Hi Andrew, You can Follow the progress of this bug here, and also find a workaround: [https://feedback.telerik.com/blazor/1463350-toggling-allowupdate-at-runtime-does-not-update-the-scheduler-behavior-until-you-toggle-a-view](https://feedback.telerik.com/blazor/1463350-toggling-allowupdate-at-runtime-does-not-update-the-scheduler-behavior-until-you-toggle-a-view) Regards, Marin Bratanov
