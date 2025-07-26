# Appointments in the timeline move to the wrong resource

## Question

**Hel** asked on 22 Aug 2023

Hello, we have a strange behavior in the scheduler. When first called up, the appointments in the timeline are displayed correctly in the order of their resource. (The text in the appointment corresponds to the id of the resource.) If you switch the scheduler view to day and then back to timeline, everything is still displayed correctly. However, if you switch to the weekly or monthly view and then back to the timeline, some of the appointments shift down by about 250px and end up in the wrong resource or no resource at all.

### Response

**Dimo** commented on 25 Aug 2023

@Helmut - perhaps this bug report is related? Wrong appointment position of the last resource group in Timeline view Please excuse us for the trouble. A possible workaround is to recreate the Scheduler when the glitch occurs (e.g. use the ViewChanged event and check what is the old and new view). See workaround 1 on this page for an example how to hide and show a component.
