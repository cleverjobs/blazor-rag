# EditForm inside a Dialog. How to handle not duplicating the buttons?

## Question

**Dan** asked on 10 Feb 2023

I have an EditForm with some simple attributes that I would like to edit. The TelerikButtons, Abort and Save, are directly implemented and call the necessary business logic. But now I would also like to implement the EditForm as a TelerikDialog popup to quickly record data. Sadly, the buttons are duplicated. How should I go about not duplicating the functionality? Can I somehow move them or redirect the dialogbuttons to call them? <TelerikDialog Visible="@IsAssetCreationVisible" ButtonsLayout="@DialogButtonsLayout.End" Width="30%"> <DialogContent> <GameAssetCreatePage AssetType="AssetType.Text"> </GameAssetCreatePage> </DialogContent> <DialogButtons> <TelerikButton> Abort </TelerikButton> <TelerikButton Id="@GameAssetCreatePage.EditFormId" ButtonType="ButtonType.Submit" ThemeColor="@ThemeColor.Primary"> Save and Close </TelerikButton> </DialogButtons> </TelerikDialog>

## Answer

**Hristian Stefanov** answered on 15 Feb 2023

Hi Daniel, As far as I understand, the desired result here is to keep either the EditForm buttons or the Dialog buttons. The easiest approach for this case seems to remove the <DialogButtons> tag from the Dialog implementation. That way, only the EditForms buttons will stay. I have prepared an example for you: @using System.ComponentModel.DataAnnotations <TelerikDialog @bind-Visible="@Visible" Title="Test"> <DialogContent> <TelerikForm EditContext="@MyEditContext" OnSubmit="OnSubmitHandler"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> <FormButtons> <TelerikButton ButtonType="ButtonType.Button" OnClick="@AbortButton"> Abort </TelerikButton> <TelerikButton ButtonType="@ButtonType.Submit" ThemeColor="primary"> Save and Close </TelerikButton> </FormButtons> </TelerikForm> </DialogContent> </TelerikDialog> <br /> <TelerikButton OnClick="@(()=> { Visible=!Visible; })"> Open Dialog </TelerikButton> @code {
private bool Visible { get; set; }
public EditContext MyEditContext { get; set; }

public Person person=new Person();

protected override void OnInitialized()
{
MyEditContext=new EditContext(person);
}

private void OnSubmitHandler(EditContext editContext)
{
bool isFormValid=editContext.Validate();

if (isFormValid)
{
//apply some custom logic when the form is valud
}
else
{
//apply some custom logic when the form is not valid
}

Visible=!Visible;
}

private void AbortButton()
{
//abort action
}

public class Person
{
[Editable(false)]
public int Id { get; set; }

[Required]
[MaxLength(20, ErrorMessage="The first name should be maximum 20 characters long")]
[Display(Name="First Name")]
public string FirstName { get; set; }

[Required]
[MaxLength(25, ErrorMessage="The last name should be maximum 25 characters long")]
[Display(Name="Last Name")]
public string LastName { get; set; }

[Required]
[Display(Name="Date of Birth")]
public DateTime? DOB { get; set; }
}
} Please run and test it to see the result. Let me know if I'm missing something from the scenario. Regards, Hristian Stefanov

### Response

**Daniel** commented on 16 Feb 2023

That doesn't quite solve my problem. I have a EditForm as a normal page. Then I create a dialogue where the content happens to be that page. My question now is what do I do with the original buttons from the form? Because the dialogue would add its own buttons. <GameAssetCreatePage @ref="GameAssetCreatePage" ButtonsVisible="false" "/> </DialogContent> <DialogButtons> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> GameAssetCreatePage?.OnAbort())"> Abort </TelerikButton> <TelerikButton Id="@GameAssetCreatePage.EditFormId" OnClick="@(()=> GameAssetCreatePage?.OnSubmit())" ButtonType="ButtonType.Submit" ThemeColor="@ThemeColor.Primary"> Save and Close </TelerikButton> I have solved it like this: to hide the buttons on the EditForm like you suggested and then to use a reference to the EditForm page and call the existing methods. Please let me know if this is an intended solution to embed forms inside a dialogue.

### Response

**Hristian Stefanov** commented on 21 Feb 2023

Hi Daniel, As far as I understand, you've found a solution for the case. I'm glad to see this. I also confirm that the described approach seems completely OK for the current scenario. If a better alternative appears, I will write to you again here. Let me know if we can help with anything else.
