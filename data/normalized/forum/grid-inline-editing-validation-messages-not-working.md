# Grid inline editing validation messages not working

## Question

**Gre** asked on 23 May 2022

I have a grid that does CRUD and it works correctly. Editing mode is Inline. The required value validation rules (defined on the data model) are working, but all that happens visually in the grid is a red border on the required fields. The validation messages I expect as tooltips never display. The column in question are Activity and ActivityDate. (All latest versions of Telerik products as of 5/23/22) This is the entity definition: public class BoxActivity
{
public BoxActivity()
{
// Provide these default values so these required columns that will be auto-set do not cause validation to fail.
ActivityDate=DateTime.Now;
LastUpdatedDate=DateTime.Now;
LastUpdatedBy="default";
}

[Required]
[Dapper.Contrib.Extensions.Key]
public int BoxActivityId { get; set; }

[Required]
public int BoxId { get; set; }

[Required(ErrorMessage="Enter an activity")]
[StringLength(30)]
public string Activity { get; set; }

[Required(ErrorMessage="Enter an activity date")]
public DateTime ActivityDate { get; set; }

[StringLength(50)]
public string RequestedBy { get; set; }

public int? FacilityId { get; set; }

[StringLength(4000)]
public string Notes { get; set; }

[Required]
public DateTime LastUpdatedDate { get; set; }

[Required]
[StringLength(50)]
public string LastUpdatedBy { get; set; }
} This is the grid definition: <TelerikGrid Data="@boxActivity" EditMode="@GridEditMode.Inline" Height="auto" Pageable="false" Sortable="false" Groupable="false" FilterMode="Telerik.Blazor.GridFilterMode.None" Resizable="false" Reorderable="false" ConfirmDelete="true" OnUpdate="@BoxActivityUpdateHandler" OnEdit="@BoxActivityEditHandler" OnDelete="@BoxActivityDeleteHandler" OnCreate="@BoxActivityCreateHandler" OnCancel="@BoxActivityCancelHandler"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add Activity </GridCommandButton> </GridToolBar> <GridSettings> <GridValidationSettings Enabled="true" /> </GridSettings> <GridColumns> <GridColumn Field="@(nameof(BoxActivity.ActivityDate))" Title="Activity Date" Editable="true"> <HeaderTemplate> <label class="efc-grid-col-hdr"> Activity Date </label> </HeaderTemplate> <Template> <div style="text-align: center;"> @((context as BoxActivity).ActivityDate.ToString("MM/dd/yyyy")) </div> </Template> <EditorTemplate> <TelerikDatePicker @bind-Value="@((context as BoxActivity).ActivityDate)" Id="ActivityDate" Width="120px"> </TelerikDatePicker> </EditorTemplate> </GridColumn> <GridColumn Field="@(nameof(BoxActivity.Activity))" Title="Activity"> <HeaderTemplate> <label class="efc-grid-col-hdr"> Activity </label> </HeaderTemplate> <Template> <div style="text-align: center;"> @((context as BoxActivity).Activity) </div> </Template> <EditorTemplate> <TelerikDropDownList @bind-Value="@((context as BoxActivity).Activity)" DefaultText="Choose an Activity" Data="@activities" Id="Activity"> </TelerikDropDownList> </EditorTemplate> </GridColumn> <GridColumn Field="@(nameof(BoxActivity.RequestedBy))" Title="Requested By"> <HeaderTemplate> <label class="efc-grid-col-hdr"> Requested By </label> </HeaderTemplate> <Template> <div style="text-align: center;"> @((context as BoxActivity).RequestedBy) </div> </Template> <EditorTemplate> <TelerikDropDownList @bind-Value="@((context as BoxActivity).RequestedBy)" DefaultText="Choose a Requestor" Data="@requestors" Width="180px" Id="RequestedBy"> </TelerikDropDownList> </EditorTemplate> </GridColumn> <GridColumn Field="@(nameof(BoxActivity.FacilityId))" Title="Facility"> <HeaderTemplate> <label class="efc-grid-col-hdr"> Facility </label> </HeaderTemplate> <Template> <TelerikDropDownList @bind-Value="@((context as BoxActivity).FacilityId)" Data="@facilities" Enabled="false" TextField="FacilityName" ValueField="FacilityId" Width="180px" Id="FacilityId"> </TelerikDropDownList> </Template> <EditorTemplate> <TelerikDropDownList @bind-Value="@((context as BoxActivity).FacilityId)" DefaultText="Choose a Facility" Data="@facilities" TextField="FacilityName" ValueField="FacilityId" Width="180px" Id="FacilityId"> </TelerikDropDownList> </EditorTemplate> </GridColumn> <GridColumn Field="@(nameof(BoxActivity.Notes))" Title="Notes"> <HeaderTemplate> <label class="efc-grid-col-hdr"> Notes </label> </HeaderTemplate> <EditorTemplate> <TelerikTextArea @bind-Value="@((context as BoxActivity).Notes)" AutoSize="true" Id="Contents"> </TelerikTextArea> </EditorTemplate> </GridColumn> <GridCommandColumn Context="NewNameToNotCollideBoxActivityContext"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="delete"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

### Response

**Drewanz** commented on 23 May 2022

Hi, I'm also experiencing problems since the last 3.30 upgrade - could you check the F12 on your browser and see if there are errors? On mine there is an error regards one of the components missing a property.

### Response

**Greg** commented on 25 May 2022

I don't see any errors in the F12 Console. I have a support ticket open on another problem that's probably related to linked css, js, or the order in which they are linked. If that cures this problem as well, I'll mention that. Otherwise I'll open another ticket for this validation issue.

### Response

**Drewanz** commented on 25 May 2022

Just found the reason, 3.30 has a different setup for properties, just adjusted the component to reflect the changes and the error went away.

### Response

**Greg** commented on 25 May 2022

@Drewanz: Can you provide more details on the solution you found? Thanks.

## Answer

**Nadezhda Tacheva** answered on 26 May 2022

Hi all, The behavior Greg is referring to is not related to an issue, it is rather expected. Based on the shared Grid definition, I see that EditorTemplates are declared for all columns. In general, when the EditorTemplate of the Grid is used, the built-in ability to provide validation messages is disabled. In order to display validation messages in Tooltip, you may use the TelerikValidationTooltip. Here is a sample that demonstrates the described approach: [https://blazorrepl.telerik.com/mcEpvxPf47EIFRY244.](https://blazorrepl.telerik.com/mcEpvxPf47EIFRY244.) Start editing of a record and delete the WorkHours value to see the Tooltip. I hope you will find this information useful. Please let us know if any further questions are raised. Regards, Nadezhda Tacheva

### Response

**Greg** commented on 26 May 2022

Thanks. Tooltip s are working in both grids and forms now.
