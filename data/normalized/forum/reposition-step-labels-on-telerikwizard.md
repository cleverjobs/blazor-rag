# Reposition step labels on TelerikWizard

## Question

**EdoEdo** asked on 14 Sep 2023

Hello, We are using a TelerikWizard with WizardStepperSettings Linear="false" and would like to move the labels inline with the step indicators. See this example picture: Is dat possible? Regards, -Edo

## Answer

**Hristian Stefanov** answered on 18 Sep 2023

Hi Edo, You can change the labels position in the desired way by using the following CSS: @using Telerik.FontIcons <style>.k-step-list-horizontal.k-step-link { flex-direction: row;
}.k-stepper.k-step-label { background-color: white;
} </style> <TelerikWizard @bind-Value="@WizardValue"> <WizardSettings> <WizardStepperSettings Linear="false" /> </WizardSettings> <WizardSteps> <WizardStep Label="Start" Icon="@FontIcon.Gear"> <Content> <p> Welcome to the Wizard! </p> </Content> </WizardStep> <WizardStep Label="Survey" Icon="@FontIcon.Pencil"> <Content> <p> The user is performing some actions... </p> </Content> </WizardStep> <WizardStep Label="Finish"> <Content> <p> Thank you! </p> </Content> </WizardStep> </WizardSteps> </TelerikWizard> <p> <strong> Wizard Value: @WizardValue </strong> </p> @code {
int WizardValue { get; set; }
} Please run and test it to see the result. Regards, Hristian Stefanov Progress Telerik
