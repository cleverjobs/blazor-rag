# Separate Wizard or stepper into separate Blazor components?

## Question

**hfbhfb** asked on 13 Nov 2023

I want to separate Wizard or Stepper into separate Blazor components. Someone that can guide me how to separate the Wizard steps into different components? I struggle to make validation work and the step logic work with parameter or cascading value. I cannot just follow Wizard Form Integration because I need more steps and my own UI in each step so my file will be too big. I can only show the wizard right now with sending it from ""parent" to "child" but validation and step logic doesnt work. Should i looking at Stepper instead of Wizard? or have someone an example? TelerikWizard @bind-Value="@Value" OnFinish="@OnFinishHandler"> <WizardSteps> <PersonalInformationTwo applicationModel="@applicationModel" personalInformationForm="@personalInformationForm" />

## Answer

**Nadezhda Tacheva** answered on 15 Nov 2023

Hi hfb, I already responded to your private ticket sending a sample that shows a possible implementation. I am also posting the example here in case any other community member is struggling with such a use case: [https://blazorrepl.telerik.com/QHvbFeFq25Q0IuqZ09.](https://blazorrepl.telerik.com/QHvbFeFq25Q0IuqZ09.) Regards, Nadezhda Tacheva Progress Telerik
