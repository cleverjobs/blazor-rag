# Wizard label multiple lines

## Question

**Pau** asked on 03 Aug 2022

Hi <WizardStep Label="Registration of employee" can i have a label over more lines? Like Registration of employee Eric

## Answer

**Dimo** answered on 05 Aug 2022

Eric, here is how to achieve this: <TelerikWizard Class="multiline-stepper" /> <style>.multiline-stepper.k-stepper.k-step-link,.multiline-stepper.k-stepper.k-step-text { white-space: normal;
} </style> Regards, Dimo Progress Telerik

### Response

**Brad** commented on 05 Jun 2023

Thank you for the example. In my case I used white-space: pre-line so that I can force a line wrap with '\n'.
