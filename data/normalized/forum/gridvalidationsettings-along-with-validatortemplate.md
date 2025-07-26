# GridValidationSettings along with ValidatorTemplate

## Question

**Bee** asked on 21 Apr 2022

Hello I am using in the in-build grid edit popup form in the editmode. Each of the grid columns have editortemplate that has an associated TelerikValidationMessage control to show the inline validation messages. I am also using ValidatorTemplate to show the validation messages onces the save action is made and the error comes in the model state. My issue is I only want to show the inline validation message and not the default validation summary that comes with the editform. Is there a way to disable the validation summary on the editform. Below is my code and and image of what it is looks now, and what I am trying to accomplish. //Editor Template for the Grid Column with Validation Message <GridColumn Field="@(nameof(_defectObj.Name))" Title="Name" Width="200px" TextAlign="ColumnTextAlign.Left" FieldType="@(typeof(string))" FilterMenuType="Telerik.Blazor.FilterMenuType.Menu"> <EditorTemplate> @{
_defectEdit=(DefectModel)context; <TelerikTextBox @bind-Value="_defectEdit.Name"> </TelerikTextBox> <TelerikValidationMessage For="@(()=> _defectEdit.Name)"> </TelerikValidationMessage> } </EditorTemplate> </GridColumn> <GridSettings> <GridPopupEditSettings MaxWidth="700px" MaxHeight="600px" Width="500px" Height="600px" MinHeight="200px" MinWidth="300px" Title="@(_isNewGridRow==true? " Add New Defect ": " Edit " + _currentDefectName )"> </GridPopupEditSettings> <GridPopupEditFormSettings Orientation="FormOrientation.Horizontal" ButtonsLayout="FormButtonsLayout.Center" Columns="1" ColumnSpacing="25"> </GridPopupEditFormSettings> <GridValidationSettings Enabled="true"> <ValidatorTemplate> <DataAnnotationsValidator> </DataAnnotationsValidator> <ProblemDetailsValidator @ref="_customValidation"> </ProblemDetailsValidator> </ValidatorTemplate> </GridValidationSettings> </GridSettings> Image shows how both ValidationMessage display and ValidationSummary display. I would only like to show the Validation Message along the input textbox and not the validation summary. How can I accomplish this. Thank you. Beena.

### Response

**Nadezhda Tacheva** commented on 26 Apr 2022

Hi Beena, Thank you for reaching out! We are currently looking into it and will need some more time to revise the case in detail. I will get back to you with an update as soon as possible. Thank you for your patience in advance!

## Answer

**Beena** answered on 26 Apr 2022

Please look at the support in the link. Resolved through css. [https://www.telerik.com/account/support-center/view-ticket/1562385](https://www.telerik.com/account/support-center/view-ticket/1562385) Thank you Beena

### Response

**Nadezhda Tacheva** answered on 26 Apr 2022

Hi Beena, Thank you for the follow up! Indeed, custom CSS is the proper approach to achieve your desired result for the time being. Apart form that, we've had an additional discussion with our development team for an option to allow removing the ValidationSummary out of the box. We want to see what is the community demand on that, so I opened a feature request on your behalf: Ability to remove ValidationSummary from the Popup edit form We are tracking the interest based on the votes gathered for a certain request. Therefore, I added your vote there as this is important metrics in our enhancement prioritization process. In addition, I see you are using an EditorTemplate just for adding the inline validation messages. That said, you might be interested in another enhancement which will allow built-in field validation messages for the Popup edit form. Once available, you will not need to use EditorTemplate for that purpose, you will be able to simply specify your preferred field validation message type (inline or popup). I added your vote there as well and you may follow its progress by subscribing for the item in the portal. Regards, Nadezhda Tacheva Progress Telerik
