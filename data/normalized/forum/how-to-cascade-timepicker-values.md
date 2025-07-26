# How to cascade timepicker values

## Question

**Kev** asked on 12 Apr 2023

I am trying to create a break time control using the Telerik Grid and Timepicker controls. I set the break start values Min is the schedule series start time. and Max is the schedule series end time. So setting the break start timepicker Min and Max properties correlate to this schedule time frame to keep the break time within the bounds of the schedule. When I set break end I want the range in the timepicker to reflect break start to schedule end. For example: I have a schedule that starts at 0600 and ends at 1430. My first break I choose the start time 0800 from the range of 0600 to 1430. I want to set the break end time to be chosen from a range of 0800 to 0900. In the image the Break End shows the time range of 0600 to 1430... So basically I want to have the break end range be from the break start time set. in short When adding a new Break, the START time should pre-populate with the Scheduled Events actual starting time. Example: First Shift is from 7:00 AM to 2:30 PM. When adding a new Break, the start time should pre-populate as 7:00 AM. When you add a new Break and change the START time, it should automatically adjust the END time to at least the same START time + 15 or 30 or xxx minutes. I have tried using the events for the Timepicker to help with this, but I can never get it to update. Is there a way to achieve this? Razor code: <TelerikGrid Data="@Appointment.Breaks" EditMode="GridEditMode.Inline" OnCreate="@CreateHandler" OnDelete="@DeleteHandler" OnUpdate="@UpdateHandler"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field="Description" Title="Description" FieldType="@typeof(string)" Width="50%" /> <GridColumn Field="BreakStart" Title="Break Start" FieldType="@typeof(DateTime)" DisplayFormat="{0:hh:mm:ss tt}" Width="150px"> <EditorTemplate> @{
var BreakToEdit=context as Break; <TelerikTimePicker Format="hh:mm:ss tt" @bind-Value="@BreakToEdit.BreakStart" Id="timepickerstart" DebounceDelay="@DebounceDelay" Min="@Min" Max="@Max"> <TimePickerSteps Minute="5" /> </TelerikTimePicker> } </EditorTemplate> </GridColumn> <GridColumn Field="BreakEnd" Title="Break End" FieldType="@typeof(DateTime)" DisplayFormat="{0:hh:mm:ss tt}" Width="150px"> <EditorTemplate> @{
var BreakToEdit=context as Break; <TelerikTimePicker Format="hh:mm:ss tt" @bind-Value="@BreakToEdit.BreakEnd" Id="timepickerend" DebounceDelay="@DebounceDelay" Min="@Min" Max="@Max"> <TimePickerSteps Minute="5" /> </TelerikTimePicker> } </EditorTemplate> </GridColumn> <GridCommandColumn Width="100px"> <GridCommandButton Command="Edit" Icon="edit"> </GridCommandButton> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> </GridCommandButton> <GridCommandButton Command="Delete" Icon="delete"> </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

### Response

**Kevin** commented on 19 Apr 2023

-comment deleted-

## Answer

**Tsvetomir** answered on 17 Apr 2023

Hi Kevin, Thank you for sharing the details about the scenario you are working on. Indeed, to achieve a min value for the second value, you should handle the Value, ValueChanged, and ValueExpression for the pickers. Save the min value and apply it to the second picker: [https://blazorrepl.telerik.com/cdOIFLaW10KU8Zmz14](https://blazorrepl.telerik.com/cdOIFLaW10KU8Zmz14) The REPL example above shows how to setup the editors and lacks the functionality for the actual save that is not directly correlated to the case. Let me know if additional information is needed. Regards, Tsvetomir Progress Telerik

### Response

**Kevin** commented on 19 Apr 2023

Is there a way when validating inside the grid create handler, to keep the row open for editing instead of closing it?

### Response

**Tsvetomir** commented on 20 Apr 2023

The OnCreate event of the grid is cancellable. Canceling the event will cause the row to remain open. Find more information in the Grid CUD Events article.
