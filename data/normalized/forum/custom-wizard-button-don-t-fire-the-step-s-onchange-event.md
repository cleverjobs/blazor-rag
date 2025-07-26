# Custom Wizard Button don't fire the step's OnChange event

## Question

**BobBob** asked on 21 Jul 2021

I have a wizard where I have defined OnChange events for the steps and I am also creating my own custom buttons. the event fires when a step is clicked on in the progress bar, but they do not fire when clicking on the buttons in the WizardButtons. I have created my next and previous button just like in your example for custom buttons. if (index> 0)
{ <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> step -=1)"> Previous </TelerikButton> }
if (index <lastStep)
{ <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> step +=1)" Primary="true"> Next </TelerikButton> } How do I make the button clicks fire the OnChange event for the step?

## Answer

**Marin Bratanov** answered on 21 Jul 2021

Hello Bob, Programmatic change of a parameter does not fire the corresponding event. For example, changing the string a Textbox is bound to will not fire its ValueChanged or OnChange event. Doing so can cause endless loops and unnecessary complexity in handling them. When you invoke such changes in your code, you already have an event handler, so you can call the appropriate methods to execute additional logic. For example, refactor the ValueChanged handler of the wizard to execute its logic in a method that takes the step index as an argument, and call that method from both the wizard ValueChanged, and the button OnClick. On the particular question for OnChange - that's a handler that lets the developer know that the end user is about to change the step. Now, since you as the developer are changing the step, the wizard should not fire events further - it assumes that you know what is required and you have confirmed the parameter change. Regards, Marin Bratanov Progress Telerik

### Response

**Bob** commented on 21 Jul 2021

Okay, thanks. I was able to resolve the issue by calling a method that creates the WizardStepChangeEventArgs and called the OnSteChange method. See below I do, however, think you should clearly state in your documentation for the custom buttons that when you override the standard wizard buttons, they will not fire on the OnChange event for the steps (note they are still fired if you click on the steps in the bar at the top). private async Task PerformStepClick(int increment) { int newStep=step + increment; WizardStepChangeEventArgs changeArgs=new() { TargetIndex=newStep }; await OnWizardStepChange(changeArgs); if (!changeArgs.IsCancelled) { step +=increment; } }

### Response

**Nadezhda Tacheva** answered on 26 Jul 2021

Hi Bob, Thank you for your feedback! We will consider adding more details for this scenario in the Custom Buttons section of the Wizard documentation. Regards, Nadezhda Tacheva Progress Telerik
