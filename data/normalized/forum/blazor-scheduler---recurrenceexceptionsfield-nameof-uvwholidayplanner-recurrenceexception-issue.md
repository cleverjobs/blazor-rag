# Blazor Scheduler - RecurrenceExceptionsField="@(nameof(UvwHolidayPlanner.RecurrenceException)) issue

## Question

**Bla** asked on 14 Jan 2023

Hi, I have set up my model the exact way it is in the demo. My client makes a JSON call to API to populate the scheduler. The post is successful but the get seems to break the scheduler. The error message is below: Error: System.InvalidCastException: Unable to cast object of type 'System.String' to type 'System.Collections.Generic.IEnumerable`1[System.DateTime]'.

at Telerik.Blazor.Components.TelerikScheduler`1.CreateAppointment(TItem dataItem)

at Telerik.Blazor.Components.TelerikScheduler`1.ExpandAppointments()

at Telerik.Blazor.Components.TelerikScheduler`1.ProcessAppointmentsAsync()

at Telerik.Blazor.Components.TelerikScheduler`1.OnParametersSetAsync()

at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)

at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle) unsure why I need to cast as the demo it seems to work fine without casting. Is this an issue within the UI control itself? I'm using version 2.24.0 Thanks
