# DropDownList not showing in my grid?

## Question

**RobRob** asked on 11 Dec 2024

I was following this example here. <GridColumn Field=@nameof(BookingEquipmentModel.FirstRequestedEquipmentType) Title="1st Requested" Editable="true" Filterable="false" Width="7rem"> <EditorTemplate> @{
_currentBookingEquipmentModel=context as BookingEquipmentModel; <TelerikDropDownList Data="@_equipmentTypeList" @bind-Value="@_currentBookingEquipmentModel.FirstRequestedEquipmentTypeId" TextField="@nameof(EquipmentTypeModel.Code)" ValueField="@nameof(EquipmentTypeModel.EquipmentTypeId)" DefaultText="Select Type"> <DropDownListSettings> <DropDownListPopupSettings Height="auto" /> </DropDownListSettings> </TelerikDropDownList> } </EditorTemplate> </GridColumn> Grid EditMode set to GridEditMode.Inline and Column is Editable=True. _equipmentTypeList is populated in OnAfterRenderAsync. It's behaving as if it's just a normal read only column? Rob.

### Response

**Dimo** commented on 11 Dec 2024

Hi Rob, The linked EditorTemplate page contains an example with a DropDownList, which works. A non-rendering DropDownList sounds rather strange and there should be no need to change the edit mode. Even if the data is not available yet, the component itself should appear. I suspect a misconfigured Edit command button. If you send a complete runnable example, I will be able to see what's happening.

### Response

**Rob** commented on 11 Dec 2024

Yep, that was the link I used for how to work it ... the only difference is that I do NOT define a Template like you use: <Template>
@{ // a Template is used to show the foreign key data that is user-friendly int roleId=(context as Employee).RoleId;
Role matchingPos=Roles.FirstOrDefault(r=> r.RoleId==roleId); string textToRender=matchingPos !=null? matchingPos.RoleName : "Unknown";
<text>@textToRender</text>
}
</Template> I populate my list (of options _equipmentTypeList) during the OnAfterRenderAsync. I do have a Edit Command Button defined for a column, but no really sure how that is relevant? <AuthorizeView Policy="@TomsClaims.BookingEdit"> <ChildContent Context="authContext2"> <GridCommandColumn Width="6rem" Locked="true"> <GridCommandButton Command="EquipmentEditCommand" OnClick="@EquipmentEditCommandHandler" Class="btn-green" Icon="@FontIcon.Pencil" ShowInEdit="false"> Edit </GridCommandButton> </GridCommandColumn> <GridCommandColumn Width="8rem"> <GridCommandButton Command="CommodityViewCommand" OnClick="@CommoditiesViewCommandHandler" Class="btn-teal" ShowInEdit="false"> Commodities </GridCommandButton> </GridCommandColumn> <GridCommandColumn Width="8rem"> <GridCommandButton Command="CommodityViewCommand" OnClick="@EquipmentDeleteCommandHandler" Class="btn-red" Icon="@FontIcon.Trash" ShowInEdit="false"> Delete </GridCommandButton> </GridCommandColumn> </ChildContent> </AuthorizeView>

### Response

**Dimo** commented on 11 Dec 2024

The Grid column <Template> cannot affect how the <EditorTemplate> works or when / whether its content appears. I don't see a built-in Edit command button, so I assume that you are putting the Grind in edit mode programmatically through EquipmentEditCommandHandler. Please compare your code with the linked KB or send a complete runnable test page for inspection.

### Response

**Rob** commented on 11 Dec 2024

No Edit or Add or Delete command button ... just setting the GridColumn Editable="true" and EditMode="@GridEditMode.Incell" on the grid. I could be confused, but if EditMode for the grid is Incell and the column is set to Editable and I click in the grid cell for that column it should automatically be in "Edit mode"? When I make a change in the cell my UpdateHandler is fired and I follow similar code per your example for Incell. Not sure I can get you a project sample, is there anything specific I need to check? Hints? Rob.

### Response

**Rob** commented on 11 Dec 2024

Somewhat related ... due to poor database design I inherited for this project, I need to be able to bind the TextField value as well as the ValueField. For example something like this (which is not valid as there is no @bind-Text support): <EditorTemplate> @{
_currentBookingEquipmentModel=context as BookingEquipmentModel; <TelerikDropDownList Data="@_equipmentTypeList" @bind-Value="@_currentBookingEquipmentModel.FirstRequestedEquipmentTypeId" @bind-Text="@_currentBookingEquipmentModel.FirstRequestedEquipmentType" TextField="@nameof(EquipmentTypeModel.Code)" ValueField="@nameof(EquipmentTypeModel.EquipmentTypeId)" DefaultText="Select Type"> <DropDownListSettings> <DropDownListPopupSettings Height="auto" /> </DropDownListSettings> </TelerikDropDownList> } </EditorTemplate> I realize I can use a separate event handler for the dropdown to get the data I need for _currentBookingEquipmentModel.FirstRequestedEquipmentType ... but since TextField is available in the dropdown I'd rather just bind to it. Is there an easier way to get the TextField actual value?

### Response

**Dimo** commented on 11 Dec 2024

My previous comment referred to inline editing scenarios. What you say about cell clicks is correct, but applies to incell editing. Inline editing requires an Edit command or programmatic triggering of edit mode. The original problem description is that a DropDownList inside an <EditorTemplate> doesn't appear even though the column is editable and has a Field. This is the example I need. It doesn't matter if it's a single runnable web page (REPL) or an isolated runnable project. On a side note, I see that you have three command buttons in three command columns. If that's not on purpose, I should confirm that one command column can hold multiple command buttons.===If you wish the DropDownList to display custom text as its value, use a <ValueTemplate>. If the goal is different, please open a separate thread with a more detailed description.

### Response

**Rob** commented on 11 Dec 2024

Incell is actually what I want and working as expected. You're correct I was not using Add/Edit command button columns for the purpose of Add/Edit "in grid", they launch dialogs. Yes I was aware command column can hold multiple command buttons, wanted them in separate columns (for now). ValueTemplate is not what I was looking for so will start a separate thread.

## Answer

**Rob** answered on 11 Dec 2024

I was able to solve the issue by changing the EditMode=Incell (it was using Inline per example you folks provided but seems to require Incell to work correctly). <TelerikGrid Data="@_bookingEquipmentList" EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandler" Height="calc(40vh - 10rem)" Size="@ThemeConstants.Grid.Size.Small" Resizable="true" Sortable="true" Reorderable="true" Pageable="true" PageSize="25">
