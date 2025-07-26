# Wizard - Make the Step Properties available to read

## Question

**Ric** asked on 14 Aug 2024

I have a wizard that on the first page a user can toggle what all pages they want to access. It is meant to narrow down the available options to what they need. When a user turns one of the options off, I disable that page. I don't hide it because the functionality with the add/remove pages tends to put the newly added pages at the bottom of the wizard (which I don't want). The next problem I run into is the functionality of the Previous / Next Buttons. If the next or previous page is disabled, the relative button is also disabled. Which means the user now has to click the actual step instead of clicking next. I attempted to add my own buttons but without access to the individual steps like the default buttons have I can't determine if the steps are disabled or not. My goal is to click the "Next" or "Previous" button and determine what the next available step (if it is non-linear) is instead of forcing the user to figure out they need to click the step in the stepper section. There is a hack to get around this, but the business logic is not ideal, and it is very rigid. I would prefer not to go this route. The work around is checking all the possible combinations of variables that control the disabled option for each page.

## Answer

**Dimo** answered on 15 Aug 2024

Hi Rick, I confirm that the described scenario requires a custom implementation with a WizardButtons template. The app should know what is the state of all steps and navigate to the appropriate one. Depending on the exact scenario, this may be easy to achieve: <label> <TelerikCheckBox @bind-Value="@StepAccessibility[1]" /> Step 2 Disabled </label> <label> <TelerikCheckBox @bind-Value="@StepAccessibility[2]" /> Step 3 Disabled </label> <label> <TelerikCheckBox @bind-Value="@StepAccessibility[3]" /> Step 4 Disabled </label> <TelerikWizard @bind-Value="@WizardStep" Width="600px" Height="300px"> <WizardSettings> <WizardStepperSettings Linear="false" /> </WizardSettings> <WizardSteps> <WizardStep Text="1" Label="Label 1"> <Content> <p> Step 1 content </p> </Content> </WizardStep> <WizardStep Text="2" Label="Label 2" Disabled="@StepAccessibility[1]"> <Content> <p> Step 2 content </p> </Content> </WizardStep> <WizardStep Text="3" Label="Label 3" Disabled="@StepAccessibility[2]"> <Content> <p> Step 3 content </p> </Content> </WizardStep> <WizardStep Text="4" Label="Label 4" Disabled="@StepAccessibility[3]"> <Content> <p> Step 4 content </p> </Content> </WizardStep> <WizardStep Text="5" Label="Label 5"> <Content> <p> Step 5 content </p> </Content> </WizardStep> </WizardSteps> <WizardButtons> @{
var index=context; <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> WizardStep=0)" Enabled="@(index> 0)"> First </TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@OnPreviousStepClick" Enabled="(index> 0)"> Previous </TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@OnNextButtonClick" Enabled="@(index !=4)"> Next </TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> WizardStep=2)" Enabled="@(index !=4)"> Last </TelerikButton> } </WizardButtons> </TelerikWizard> @code {
private Dictionary<int, bool> StepAccessibility { get; set; }=new ();

private int WizardStep { get; set; }

protected override void OnInitialized ( ) { for (int i=0; i <5; i++)
{
StepAccessibility.Add(i, false );
}

base.OnInitialized();
}

private void OnNextButtonClick ( ) { var nextStep=StepAccessibility.FirstOrDefault( x=>!x.Value && x.Key> WizardStep);

WizardStep=nextStep.Key;
}

private void OnPreviousStepClick ( ) { var nextStep=StepAccessibility.LastOrDefault( x=>!x.Value && x.Key <WizardStep);

WizardStep=nextStep.Key;
}
} Regards, Dimo
