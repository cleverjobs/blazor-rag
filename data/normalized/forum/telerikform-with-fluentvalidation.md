# TelerikForm with FluentValidation

## Question

**Gui** asked on 16 Nov 2022

Good Morning, I vave this code. I try to create a FluentValdation in TelerikForm, code builts good. When i submit empty form, validations are good(), but the form doesn't show the errors. <TelerikForm Model="@TriggerDetail" Columns="1" ColumnSpacing="25px" OnValidSubmit="@HandleValidSubmit" EditContext="@EditContext"> <FormValidation> <FluentValidationValidator Validator="@Validator"> </FluentValidationValidator> </FormValidation> <FormItems> <FormGroup LabelText="General Information" Columns="2" ColumnSpacing="15px"> <FormItem Field="@nameof(TriggerDetailModel.Name)" LabelText="@Localizer[" JobTrigger_Name "]" Enabled="@Enabled"> </FormItem> <ValidationMessage For="@(()=> TriggerDetail.Name)" /> <FormItem Field="@nameof(TriggerDetailModel.Group)" LabelText="@Localizer[" JobTrigger_Group "]" Enabled="@Enabled"> <Template> <label class="k-label k-form-label"> @Localizer["JobTrigger_Group"] </label> <TelerikAutoComplete Data="@ExistingTriggerGroups" @bind-Value="@TriggerDetail.Group" ClearButton="true" Enabled="@Enabled" /> </Template> </FormItem> <ValidationMessage For="@(()=> TriggerDetail.Group)" /> </FormGroup> </FormItems> <FormButtons> <TelerikButton Icon="caret-alt-to-left" OnClick="@BackStep" ThemeColor="@(ThemeConstants.Button.ThemeColor.Error)"> @Localizer["Back"] </TelerikButton> <TelerikButton ButtonType="ButtonType.Submit" Icon="caret-alt-to-right" ThemeColor="@(ThemeConstants.Button.ThemeColor.Info)"> @Localizer["Next"] </TelerikButton> </FormButtons> </TelerikForm> @code{
public TriggerDetailModel TriggerDetail { get; set; }=null!;
public TriggerDetailValidator Validator { get; set; }=new();

private void HandleValidSubmit()
{
var validationResult=Validator.Validate(TriggerDetail);
if (validationResult.IsValid)
{
NextStep();
}
else
{
//Errores
}
}
}

public class TriggerDetailValidator : AbstractValidator <TriggerDetailModel> {
public TriggerDetailValidator()
{
RuleFor(t=> t.Name).NotEmpty();
RuleFor(t=> t.Group).NotEmpty();
}
} Where is the problem? Thanks

## Answer

**Svetoslav Dimitrov** answered on 18 Nov 2022

Hello Guillermo, I can see that you have taken the correct path of adding the FormValidation tag to the TelerikForm. You can add the ValidationSummary inside that tag to show a list of validation messages. Alternatively, if you want to show a validation message below each editor in the Form, you can go for the ValidationMessage component. For each form editor, you must place a validation message component. You can see examples and more information on both from the hyperlinks above. Let me know if this helps you move forward with your application. Regards, Svetoslav Dimitrov
