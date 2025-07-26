# Wizard Stepper Colors

## Question

**Dus** asked on 20 Sep 2022

Hey! Is there a way for me to change the colors of the Wizard Stepper? I figured out that I can write css in my component that will override the css on the buttons, but I cannot figure out how to change the colors on the stepper. I'm terrible at css and am actually begining to work with Tailwind. Used this to override the button:.k-button-solid-primary { background-color: rgb(8 145 178); color: white; border-color: rgb(8 145 178); } .k-button-solid-primary:hover { background-color: rgb(165 243 252); color: white; border-color: rgb(165 243 252); }

## Answer

**Hristian Stefanov** answered on 23 Sep 2022

Hi Dustin, You are on the right path - overriding the CSS is the easiest way to customize the Wizard. Inspecting the HTML elements with your browser dev tools allows you to apply the desired styles to the correct elements (the Wizard steps). Here is an example I have prepared for you: <style>.my-wizard.k-stepper.k-step-indicator { background-color: rgb ( 165 243 252 ); color: white; border-color: rgb ( 165 243 252 );
} /*This changes the color on mouse hover.*/.my-wizard.k-stepper.k-step-indicator:hover { background-color: lawngreen; color: white; border-color: lawngreen;
} </style> <div style="text-align:center"> <TelerikWizard Class="my-wizard" Width="600px" Height="300px"> <WizardSettings> <WizardStepperSettings Linear="false"> </WizardStepperSettings> </WizardSettings> <WizardSteps> <WizardStep Label="Cart" Icon="cart"> <Content> <h2> Content for Wizard Step 1 </h2> </Content> </WizardStep> <WizardStep Label="Delivery address" Icon="marker-pin-target"> <Content> <h2> Content for Wizard Step 2 </h2> </Content> </WizardStep> <WizardStep Label="Payment method" Icon="dollar"> <Content> <h2> Content for Wizard Step 3 </h2> </Content> </WizardStep> </WizardSteps> </TelerikWizard> </div> Additionally, see these articles that will help you understand better the CSS customizations: How to override theme styles Blazor theme customization options I hope you will find the above information helpful to move forward. Let me know if you face any difficulties on the go. Regards, Hristian Stefanov Progress Telerik

### Response

**Dustin** commented on 23 Sep 2022

Perfect, thank you!

### Response

**Dustin** commented on 23 Sep 2022

I have been able to change all of the colors that I need except for the line in between the steps. I can't for the life of me figure out what is controlling that color. Can you help me out once again?

### Response

**Hristian Stefanov** commented on 28 Sep 2022

Hi Dustin, I'm glad to see that you've managed to change all the other colors. Here is an additional example that shows how to change the color of the line between the steps: <style>.my-wizard.k-stepper.k-step-indicator { background-color: rgb ( 165 243 252 ); color: white; border-color: rgb ( 165 243 252 );
} /*This changes the color on mouse hover.*/.my-wizard.k-stepper.k-step-indicator:hover { background-color: lawngreen; color: white; border-color: lawngreen;
}.my-wizard.k-progressbar.k-selected { background-color: lawngreen; color: white; border-color: lawngreen;
} </style> <div style="text-align:center"> <TelerikWizard Class="my-wizard" Width="600px" Height="300px"> <WizardSettings> <WizardStepperSettings Linear="false"> </WizardStepperSettings> </WizardSettings> <WizardSteps> <WizardStep Label="Cart" Icon="cart"> <Content> <h2> Content for Wizard Step 1 </h2> </Content> </WizardStep> <WizardStep Label="Delivery address" Icon="marker-pin-target"> <Content> <h2> Content for Wizard Step 2 </h2> </Content> </WizardStep> <WizardStep Label="Payment method" Icon="dollar"> <Content> <h2> Content for Wizard Step 3 </h2> </Content> </WizardStep> </WizardSteps> </TelerikWizard> </div> Kind Regards, Hristian
