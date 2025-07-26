# HOw can I get the Scheduler TimeLineView SchedulerSlotTemplateContext Start and End times?

## Question

**Dou** asked on 20 Jul 2023

In the Blazor Scheduler, the TimeLineView SchedulerSlotTemplateContext Start and End times are always 00:00:00. All of the other views have the correct data. I notice the docs mention being sure the SlotTemplate adds class !k-pos-absolute (which mine does) but that didn't seem to help. Can someone please provide some guidance here?

### Response

**Suzanne** commented on 07 Aug 2023

To get the correct Start and End times in the Scheduler TimeLineView's SchedulerSlotTemplateContext in Blazor, you can try using the SchedulerSlotTemplateContext.Slot property to access the underlying time slot information. Here's an example of how you can retrieve the Start and End times: csharp Copy @using Telerik.Blazor.Components.Scheduler <TelerikScheduler TimelineView="TimelineViewSettings" SlotTemplate="CustomSlotTemplate"> </TelerikScheduler> @code { private void CustomSlotTemplate(SchedulerSlotTemplateContext context) { var slot=context.Slot; var startTime=slot.Start; // Start time of the time slot var endTime=slot.End; // End time of the time slot // Use the startTime and endTime as needed } } By accessing the Start and End properties of the slot object within the SchedulerSlotTemplateContext, you should be able to retrieve the correct Start and End times for the TimeLineView. If the Start and End times are still appearing as 00:00:00, it's possible that there may be other factors affecting the behavior. In that case, it would be helpful to review your code and make sure all necessary configurations and data bindings are correctly set up. Additionally, consulting the Telerik Blazor documentation or reaching out to their support team can provide further insights and assistance specific to the issue you're facing.

### Response

**Doug** commented on 08 Aug 2023

@Suzanne What version of the components are you using? I am using 4.4.0 and SchedulerSlotTemplateContext does not contain a definition for 'Slot'

### Response

**Brook** commented on 01 Dec 2023

I am having the same issue. Check the sample code it is doing the same thing. I found a fix. void EditHandler(SchedulerEditEventArgs args) { SchedulerAppointment item=args.Item as SchedulerAppointment; item.Start=args.Start; item.End=args.End; ...

## Answer

**Brook** answered on 01 Dec 2023

This is how I got it to work. void EditHandler(SchedulerEditEventArgs args) { SchedulerAppointment item=args.Item as SchedulerAppointment; item.Start=new DateTime(args.Start.Year, args.Start.Month, args.Start.Day, args.Start.Hour, args.Start.Minute, 0); item.End=new DateTime(args.End.Year, args.End.Month, args.End.Day, args.End.Hour, args.End.Minute, 0); item.IsAllDay=args.IsAllDay; ...
