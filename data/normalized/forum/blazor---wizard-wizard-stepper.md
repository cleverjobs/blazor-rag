# Blazor - Wizard / Wizard Stepper

## Question

**Mat** asked on 09 Dec 2022

I a working on an app that has x number of steps depending user configuration. I need to be able to call a service to load the model that I pass into the step. However, I have not had any success finding an event. I also tried using the OnInitialized within the component inside the step. But that has not worked either. Is there any event which will fire before the parameter is passed to the component within the step. Note: I really want contain it within the step because I have no way of know which steps are available without some complex logic. @if (WizardInfo.ShowIncomeDetails) { <WizardStep Label=@IncomeDetailsText IconClass="fa-regular fa-calendar-day fa-xl" OnChange="@IncomeDetailsOnChangeAsync" Valid="@incomeDetailsIsValid"> <Content> <TelerikForm Model="IncomeDetails" ValidationMessageType="@FormValidationMessageType.Inline"> <FormValidation> <FluentValidationValidator></FluentValidationValidator> <ValidationSummary/> </FormValidation> <FormItems> <IncomeDetails IncomeDetails="@IncomeDetails" @ref="@incomeDetailsComponent" /> </FormItems> <FormButtons></FormButtons> </TelerikForm> </Content> </WizardStep> }

### Response

**Yanislav** commented on 14 Dec 2022

Hello Matt, Generally speaking, the most suitable event for loading form data is when the OnInitialized event of the page/component is triggered. Here is an example: [https://blazorrepl.telerik.com/QQbQPnPx16PgWHyz23](https://blazorrepl.telerik.com/QQbQPnPx16PgWHyz23) If I understand correctly the requirement, since the step is dynamic, you want to load the model data only if the step is actually included in the Wizard. If that's the case, you can try using the same condition as the one, based on which depends if the step is rendered, e.g. protected override void OnInitialized ( ) {
@if (WizardInfo.ShowIncomeDetails){ //load data } In case you want to load the model data only when the user navigates to the specific step, you may try handling the ValueChanged event of the Wizard to perform taht action. As a parameter to the ValueChanged event, you receive the index of the targeted step. If the index matches the index of the respective step, then you can fetch data. I've prepared an example that demonstrates this approach : [https://blazorrepl.telerik.com/cQlQvHPd25XusyhN03](https://blazorrepl.telerik.com/cQlQvHPd25XusyhN03) Whether this approach is suitable depends on the exact scenario and when you are rendering the dynamic step. You may test the sample and consider if this option will be a good fit. Note that this way the event is triggered each time the step is changed, so each time the step is rendered the model will be fetched. Alternatively, if you'd like to handle the OnChange to load the data as per your current configuration, you should handle the event of the previous and/or next step. The OnChange event is triggered when the user tries to exit the current step (clicks on another step). The handler provides information on the targeted step. Based on the configuration of the sample you've shared, the OnChange will be raised only after the user tries to change this step and thus the model data is not loaded when this step initializes. I hope this helps. In case I am missing something or the suggested approaches above do not meet your requirement, may I ask you to share more details on what you are trying to achieve and how the component should behave? If the aim is achievable, I can try to find a possible solution.

### Response

**Matt** commented on 14 Dec 2022

Thank you for the response. I tried the ValueChanged before I posted the quest. The problem is I don't know what the index of the each step should be. For example, assuming there are steps A, B, C, D, E and F possible. Company 1 may configure to use steps A, B and F. While Company 2 may configure to to have steps A, C, D, E, F. OnInitialized might work, I am currently loading the object before I pass it to the component. It might work by loading it in the object in the Oninitialized event then calling StateChanged.

### Response

**Yanislav** commented on 19 Dec 2022

Hello Matt, Based on the additional details that you've shared, handling ValueChanged will indeed not be the most optimal choice. That said, you may proceed with loading the object in OnInitialized. I hope the suggestion and information provided in my previous reply were helpful. Also, thank you for sharing the solution you've come up with. It might be helpful for someone facing the same issue in the future.
