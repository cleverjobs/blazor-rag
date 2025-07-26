# Grid Popup form footer. What is the best/right way to remove it?

## Question

**Joh** asked on 20 Aug 2024

I have a Grid Popup Edit Form that contains another component. The popup has a line across the bottom that seems to be a footer of some sort. I would like to remove that line but am not able to find a setting to do so. My fall back would be to use CSS but I was wondering if there is a setting or other way to remove it?

## Answer

**Justin** answered on 22 Aug 2024

Hi John, Thank you for the further information. The Popup Form Template is the right place for the form. It may help to keep in mind that the generated popup is a Window with a Title, Content and Action section. Any content in the Form Template will be included in the window content section. Any content in the Buttons Template would be included the action section. There is no setting to exclude the action section of the window. Given that you are using a reusable form component in the Form Template and likely don't want to separate the buttons and include them in a Buttons Template, I suggest hiding the action section with CSS. Regards, Justin

### Response

**Justin** answered on 20 Aug 2024

Hi John, I am under the impression that you are using the Popup Form Template. Is that correct? If so, the line is meant to separate the buttons into a footer as seen in the grids built-in Popup Editing dialog. To recreate the default look, include the Popup Buttons Template and move the buttons to this template. This may look like this: <GridPopupEditFormSettings Context="FormContext"> <FormTemplate> @{
EditItem=FormContext.Item as Person; <TelerikForm Model="@EditItem" ColumnSpacing="20px" Columns="2" ButtonsLayout="@FormButtonsLayout.Stretch" OnValidSubmit="@OnValidSubmit"> <FormItems> <FormItem Field="EmployeeId" Enabled="false"> </FormItem> <FormItem Field="Name"> </FormItem> <FormItem Field="HireDate" LabelText="Custom Hire Date Label"> </FormItem> <FormItem> <Template> <label for="position"> Custom Position Label </label> <TelerikDropDownList Data="@PositionsData" @bind-Value="@EditItem.Position" Id="position"> </TelerikDropDownList> </Template> </FormItem> </FormItems> <FormButtons> @*remove the buttons*@</FormButtons> </TelerikForm> } </FormTemplate> @*add them in a ButtonsTemplate*@<ButtonsTemplate> <TelerikButton Icon="@nameof(SvgIcon.Save)"> Save </TelerikButton> <TelerikButton Icon="@nameof(SvgIcon.Cancel)" ButtonType="@ButtonType.Button" OnClick="@OnCancel"> Cancel </TelerikButton> </ButtonsTemplate> </GridPopupEditFormSettings> I can confirm there is no setting to remove the line, however as you mentioned you can remove it though CSS by overriding the theme styles. Regards, Justin

### Response

**John** commented on 20 Aug 2024

<GridPopupEditFormSettings Columns="3" ColumnSpacing="10px" Context="FormContext"> <FormTemplate> @{
editedAgent=(AgentVM)FormContext.Item; <AgentEditor agentVM="editedAgent" IsEditable="true" OnClick="ExitEditAsync" /> } </FormTemplate> What I've done is take the edit form and the submit buttons and put it into a control. so that I can reuse it in various places within the app. This then moves the submit code to the code behind of the control rather than the grid page. Then I put the control into the FormTemplate section of the GridPopupEditingFormSettings. Is there a better way or place to put that control in the grid?
