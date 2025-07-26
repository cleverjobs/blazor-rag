# Scheduler - Control order of appointments top to bottom, regardless of start/stop

## Question

**Cur** asked on 13 Sep 2022

I would like to have the the scheduler show appointments in alphabetical order, regardless of start stop, even if it introduces a "gaps". Is there a way to override the order the control paints in the appointments? It appears that no matter the order of the Data (appointment) list, the appointments get painted the same way. Thanks, Curt

### Response

**Hristian Stefanov** commented on 16 Sep 2022

Hi Curt, Let me try to shed some light on the situation below. The described idea regarding a sorting functionality sounds interesting. At the same time, that does not seem a feasible feature for such a type of component like Scheduler. In the common scenarios, Blazor Scheduler components (including non-Telerik) do not provide a sorting functionality. The main factor that determines the position of the appointments is their start/end time and date. That is how components of type schedulers operate their appointments. Still, if you have seen somewhere else sorting functionality in a Scheduler component, please send us a link, screenshot, or video, so we can use it as a reference. Thank you. Kind regards, Hristian
