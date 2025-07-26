# Disable Edit option for Gantt tasks?

## Question

**Grz** asked on 25 Jul 2022

Hey, Is there any option to disable it, so view is in readonly mode?

## Answer

**Hristian Stefanov** answered on 28 Jul 2022

Hi Grzesiek, You can disable editing in the Gantt Timeline by canceling the OnEdit event. Here is how: async Task OnEdit ( GanttEditEventArgs args ) {
args.IsCancelled=true;
} Let me know if we can assist further. Regards, Hristian Stefanov

### Response

**Grzesiek** commented on 18 Nov 2022

Thank you Hristian, it works :)
