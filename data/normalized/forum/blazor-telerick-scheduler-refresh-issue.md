# Blazor Telerick Scheduler refresh issue

## Question

**Cyr** asked on 11 Jul 2025

Hello, I'm having a problem refreshing a Scheduler component. I've set up a page where a drop-down list allows you to select a schedule. Once the schedule is selected, the appointments are loaded and the component is updated. However, I notice that the appointments are not refreshed and that I need to set the focus on the component. I've tried several solutions with Rebind and/or Refresh without success. Does anyone have a template that works? Thks,

### Response

**Ivan Danchev** commented on 14 Jul 2025

Hello Cyrille, I've tested the scenario and at my end the Scheduler is refreshed as expected after changing the data and calling its.Rebind() method. Here's an example: [https://blazorrepl.telerik.com/QzYBboFf458w6geH13](https://blazorrepl.telerik.com/QzYBboFf458w6geH13) A DropDownList is declared above the Schedule. When the user selects an option, a set of events is loaded in the Scheduler by changing the data the Scheduler is bound to: Data="@Appointments" This occurs in the DropDownList's OnVariantChanged event handler and after the new data is loaded, the .Rebind() method is called: SchedulerRef?.Rebind(); If you are experiencing a different behavior than the one in the linked example, please modify it accordingly so that it demonstrates the issue and link it back for further review.

### Response

**Cyrille** commented on 17 Jul 2025

Dear Ivan, Thank you for your response. I have tested your sample and it seems working fine in my context. However, I notice that if we use asynchron method for filling data, problem come back. Maybe pb comme from that. Thks,

### Response

**Ivan Danchev** commented on 18 Jul 2025

Hi Cyrille, The problem likely is elsewhere, because I tested the scenario with asynchronous loading of the data, both initially: async Task GetSchedulerData ( ) {
Appointments=await MyService.Read(SelectedVariant);
} protected override async Task OnInitializedAsync ( ) { await GetSchedulerData();
} and on DropDownList item selection: private async Task OnVariantChangedAsync ( object value ) {
Appointments=await MyService.Read(SelectedVariant);
SchedulerRef?.Rebind();
} And the Scheduler is refreshed as expected. See the following example, which demonstrates this: [https://blazorrepl.telerik.com/cTkBbMlR53hVExdy30](https://blazorrepl.telerik.com/cTkBbMlR53hVExdy30)
