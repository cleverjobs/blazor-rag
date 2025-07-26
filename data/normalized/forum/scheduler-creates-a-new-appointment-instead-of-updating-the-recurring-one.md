# Scheduler creates a new appointment instead of updating the recurring one.

## Question

**And** asked on 05 Jan 2022

Hi, When I edit a specific recurring appointment (not a series), it updates the appointment properly if I use drag-n-drop, but when I use the edit dialog it creates a new appointment in addition to the recurring one instead of directly updating the recurring appointment as in the drag-n-drop scenario. Is this normal? Thanks, --Andre

## Answer

**Marin Bratanov** answered on 08 Jan 2022

Hi Andre, Recurring appointments are a bit special - they are one item in the data source that the scheduler shows as many according to the recurrence rule. When you edit a single appointment, what you will first get is a Create event for the exception of the rule, then an Update event for the recurrence so you can add that exception date to it. Then, when you edit an exception, you will only get the Update event. You can read more about how this works and see examples of handling it in the following pages: [https://docs.telerik.com/blazor-ui/components/scheduler/edit-appointments](https://docs.telerik.com/blazor-ui/components/scheduler/edit-appointments) [https://docs.telerik.com/blazor-ui/components/scheduler/data-bind](https://docs.telerik.com/blazor-ui/components/scheduler/data-bind) Whether you drag the appointment instance or double click it should make no difference - in both cases you should be prompted to edit an exception or the entire series, and if you choose to make an exception you should first get Create, then Update event calls. If you see something else, double check that you have the correct static assets included and that you are using the latest version. Regards, Marin Bratanov

### Response

**Andrey** commented on 09 Jan 2022

Hi Marin, Thank you for the reply. Maybe I wasn't clear in my original question, but I'm still a bit confused: I went to Telerik demo page for the Scheduler (link below), and it behaves exactly as I described. Below are steps I take to illustrate the issue: [https://demos.telerik.com/blazor-ui/scheduler/overview](https://demos.telerik.com/blazor-ui/scheduler/overview) 1. I start dragging a recurring appointment to a new time slot. 2. Right before I drop the appointment, it asks if I want to edit only current occurrence or the series; I click 'Edit current occurrence' button. 3. At this point the current occurrence is displayed correctly as a recurrence exception and no original appointment from the series is displayed alongside of it. 4. I then refresh the page to reset the scheduler data. 5. This time I double-click the recurring appointment and it again asks if I want to edit only current occurrence or the series; I click 'Edit current occurrence' button. 6. The edit dialog opens, and I change the time for the occurrence. 7. I click Update, and at this point current occurrence is displayed correctly as a recurrence exception, but this time the original appointment from the series is also displayed alongside the exception. So there are two appointments displayed when I use the edit dialog . Could you please verify that and tell if I'm doing something wrong or misunderstanding things completely. Thanks in advance! -- Andre

### Response

**Nadezhda Tacheva** answered on 12 Jan 2022

Hi Andrey, Thank you for the additional details and steps to reproduce the behavior you are experiencing! I managed to reproduce it on my side as well. After discussing it with our development team I can confirm that you have encountered a valid bug - both approaches for editing appointments should behave the same way. Generally speaking, when editing an occurrence, a new appointment is indeed created first, as my colleague Marin mentioned in his previous post, however, the series should be updated afterwards to reflect that change in the corresponding occurrence. When you are editing an occurrence though the edit form, it looks like the series is not updated accordingly and keeps the initial occurrence. To cover that scenario, I have opened a bug report on your behalf. You can find it in our public
