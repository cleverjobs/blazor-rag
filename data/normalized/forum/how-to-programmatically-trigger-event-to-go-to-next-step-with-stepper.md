# How to programmatically trigger event to go to next step with Stepper?

## Question

**Tej** asked on 08 Feb 2022

[https://docs.telerik.com/blazor-ui/components/stepper/events](https://docs.telerik.com/blazor-ui/components/stepper/events) According to the docs, it says the OnChange event fires before the current step has changed. I'm assuming clicking the Stepper itself triggers this event, but what if I wanted to go to the next step by clicking on a custom button that I've created? This seems like a common use case, is this possible with the stepper? I don't want to use the Wizard component because it doesn't seem possible to customize it to match my requirement: I want to keep all previous steps' content rendered on the page vertically as you progress through the wizard instead of having the each step content replaced by the next step content. The documentation doesn't seem to allow for customization of the step content rendering behaviour but please correct me if I'm wrong ([https://docs.telerik.com/blazor-ui/components/wizard/structure/content).](https://docs.telerik.com/blazor-ui/components/wizard/structure/content).)

## Answer

**Marin Bratanov** answered on 10 Feb 2022

Hello Tejinder, To change what a component has/shows, you would typically change the value and/or reference of the corresponding parameter. Events work in the other direction - they fire when the user does something and let your app react to that. Thus, to change the active step, you should change the Value. The Wizard hides the content of steps not shown at the moment as its goal is to optimize rendering, data retrieval and real estate. If you want to have everything at once - making the desired layout for your app is the right thing to do, and changing the Value of the stepper will let you alter its appearance based on the buttons you have in that custom layout. Regards, Marin Bratanov

### Response

**Dean** commented on 31 May 2022

When I programmatically set the Value of a Wizard I get the warning: "BL0005: Component parameter 'Value' should not be set outside of its component."

### Response

**Dimo** commented on 02 Jun 2022

@Dean - Are you trying to set the Wizard Value via the Wizard component reference (@ref)? This is not the Blazor way. Instead, set the new value to the property, which is set as a component parameter. See [https://stackoverflow.com/questions/59559195/blazor-component-parameter-should-not-be-set-outside-of-its-component](https://stackoverflow.com/questions/59559195/blazor-component-parameter-should-not-be-set-outside-of-its-component) <TelerikButton OnClick="@MoveStep">Move Step</TelerikButton> <TelerikWizard Width="600px" Height="300px" @bind-Value="@WizardStep" /> @code {
int WizardStep=0; async Task MoveStep ( ) { WizardStep=1; }
}
