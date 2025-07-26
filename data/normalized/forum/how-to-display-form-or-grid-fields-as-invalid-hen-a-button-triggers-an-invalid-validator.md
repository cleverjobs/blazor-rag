# How to display Form or Grid fields as invalid hen a button triggers an invalid Validator?

## Question

**Arn** asked on 01 Dec 2023

Hi, This is my second Validation struggle this week. I have a TelerikGrid displaying my Dtos. This grid uses a FluentValidator. I want to trigger the Validator for a specific DTO when the user clicks on a button on the row displaying the DTO. The Validator rules are rather complex, let's say that if it is invalid when the user clicks the button, several grid columns from the row would need to turn red My method bound to the button does trigger the validator correctly and I can see when it fails (the ValidationResult contains errors). But none of the invalid controls are then displayed as having errors (red with errors). Do I have to implement the logic manually? I have to say that I do not have the slightest idea in which direction I should head. My minimal current code looks like this: <TelerikGrid @ref="@_gridRef" TItem="MyDto" OnRead="@ReadItems"> <GridSettings> <GridValidationSettings> <ValidatorTemplate> <FluentValidationValidator Validator=@Validator /> </ValidatorTemplate> </GridValidationSettings> </GridSettings> <GridToolBarTemplate> [...] </GridToolBarTemplate> <DetailTemplate Context="ctx"> [...] /* We will talk about how to flag this DetailTemplate's fields as arror later*/ </DetailTemplate> <GridColumns> <GridColumn Field="@(nameof(MyDto.MyProp))" Title="..." /> <GridColumn Field="@(nameof(MyDto.MyProp2))" Title="..." /> <GridColumn Field="@(nameof(MyDto.MyProp3))" Title="..." /> <GridColumn Title="Action" <Template> <TelerikButton OnClick="@(()=> Update(context as MyDto))" Title="Title" /> </Template> </GridColumn> [...] </GridColumns> </TelerikGrid> In this case I would like let's say GridColumn 2 and 3 to be displayed as invalid. My button Method code is as follows: private async Task Update(MyDto myDto)
{
ValidationResult result=Validator.Validate(myDto);
if (!result.Errors.Any())
{
await myService.Update(myDto);

await RefreshTable();
}
//else
//{
// await Task.Delay(50);
// StateHasChanged();
//}
} Thx in advance foy your assistance.

## Answer

**Svetoslav Dimitrov** answered on 06 Dec 2023

Hello Arnaud, What is the EditMode of the Grid you are using? Depending on the EditMode there might be different ways to achieve the desired behavior. If you go for the Inline you can take advantage of the built-in validation of the Grid. You can add the GridCommandColumn and the respective GridCommandButton tags. It will trigger the validation for the entire row (think of it as a horizontal form). Based on your description I believe that this edit mode will best match your needs. If you want to implement a custom Batch editing and trigger the validation on click of the Save/Update button, I am sorry to report that this is not possible. In Blazor the validation triggers when editors are rendered and the user inputs incorrect value. If there are no editors there is no way to trigger the validation. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Arnaud** answered on 06 Dec 2023

Hi Svetoslav, At this stage, there was no EditMode set in the TelerikGrid. I was handling the update logic manually from the button in the last column. The DB logic works fine but the validation process has indeed no visual effect. Switching to EditMode=Inline would be an option for us I suppose. I've just given it a try but I do not see any improvement. I set my handler this way for testing purpose: <TelerikGrid @ref="@_gridRef" TItem="MyDto" OnRead="@ReadItems" EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandler" OnDelete="@UpdateHandler"> [...similar as previous post...] <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Delete" Icon="@SvgIcon.Trash"> Delete </GridCommandButton> </GridCommandColumn> C# code:
async Task UpdateHandler(GridCommandEventArgs args)
{
MyDto myDto=args.Item as MyDto; // myDto is in INVALID state
ValidationResult result=Validator.Validate(myDto);

await Task.CompletedTask;
} Same as before, I can see that the ValidatorResults contains errors, but the associated fields in the line do not turn red. My assumption is that this line: Validator.Validate(myDto) does return the errors but it not meant to display them. Similarily as when using a TelerikForm, we do not display the errors with Validator.Validate(myDto) but with myForm.IsValid() However, for TelerikGrid, there are no myGrid.IsValid() command or similar. What did I miss? :) Have a good day. A

### Response

**Svetoslav Dimitrov** commented on 11 Dec 2023

Hello Arnaud, The Telerik Form validates one model. The Telerik Grid represents a collection of models, you can think of as an equivalent of multiple forms. That is the reason why the Telerik Grid does not have, and most probably will not have a myGrid.isValid() or a similar method - there is no built-in validation for a collection of models. Regards, Svetoslav Dimitrov
