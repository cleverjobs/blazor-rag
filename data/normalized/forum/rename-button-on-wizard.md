# Rename Button on Wizard

## Question

**TimTim** asked on 31 Mar 2025

I see a similar question asked and answered at the link below but couldn't find anything similar in the Blazor forums. I would like to rename the last button from Done to Submit. Rad wizard next button text in UI for ASP.NET AJAX | Telerik Forums

## Answer

**Anislav** answered on 01 Apr 2025

Hi Tim, You can rename the last button from Done to Submit by using custom Wizard buttons as documented here: Custom Buttons Documentation. In this case, it is also a good idea to explicitly call the Wizard lifecycle events like OnFinish to maintain the desired functionality. This approach ensures your Wizard completes as expected even when using custom buttons. Refer to the relevant documentation here: Call OnChange and OnFinish From Button OnClick. Regards, Anislav Atanasov

### Response

**Hristian Stefanov** commented on 01 Apr 2025

Hi Anislav, Thank you for explaining this perfectly and helping the community. Your effort and time are appreciated. Kind Regards, Hris

### Response

**Tim** commented on 01 Apr 2025

Anislav - understood, thanks for the feedback. I was hopeful there would be an easier way since using the WizardButtons section seems to effectively stop the defined WizardStep OnChange events from firing. So, it's a good amount of extra code and complexity just to rename one button. I have implemented it, and the changes seem to be working properly. My approach was to add the following section to the Wizard (from the docs) as well as the code below. In the NextClick function, I'm manually calling the functions formerly triggered by the WizardStep's OnChange events: <WizardButtons> @{
var currentStepIndex=context;

if (currentStepIndex> 0)
{ <TelerikButton OnClick="@( ()=> PreviousClick(currentStepIndex) )"> Back </TelerikButton> }
if (currentStepIndex <=2)
{ <TelerikButton ThemeColor="primary" OnClick="@( ()=> NextClick(currentStepIndex) )"> Next </TelerikButton> }
else
{ <TelerikButton ThemeColor="primary" OnClick="@SubmitClick"> Submit </TelerikButton> }
} </WizardButtons> ... @code { ... private async Task NextClick(int currentStepIndex) { var args=new WizardStepChangeEventArgs() { IsCancelled=false, TargetIndex=currentStepIndex + 1 }; if (args.TargetIndex==1) OnUserStepChange(args); else if (args.TargetIndex==2) OnAddrStepChange(args); else if (args.TargetIndex==3) OnCardStepChange(args); if (!args.IsCancelled) { wizardStep=currentStepIndex + 1; } } private async Task PreviousClick(int newStepIndex) { wizardStep=newStepIndex - 1; } private async Task SubmitClick() { await OnFinishHandler(); } ... } Regards, Tim

### Response

**Anislav** commented on 01 Apr 2025

I agree, it's definitely overkill to go through all that just to rename a button. In the link you provided, the same result is achieved using JavaScript. While you can apply a similar approach in Blazor, it's not a particularly clean solution for changing labels with JavaScript either. Regards, Anislav Atanasov

### Response

**Dimo** answered on 02 Apr 2025

Hi Tim, You can simulate localization without resource files for specific labels in the Telerik components. The linked example is exactly for the Wizard. Regards, Dimo
