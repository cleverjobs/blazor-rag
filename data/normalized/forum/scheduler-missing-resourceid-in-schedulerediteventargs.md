# Scheduler, missing ResourceId in SchedulerEditEventArgs

## Question

**Hel** asked on 06 Jan 2022

Hello, I'm trying to implement my own dialog for creating appointments in a grouped scheduler. I use the OnEdit event for this. The event is called and the start and end are correctly specified in SchedulerEditEventArgs. Unfortunately I miss any reference to the resource of the clicked line. Regards Helmut

## Answer

**Nadezhda Tacheva** answered on 11 Jan 2022

Hi Helmut, It will indeed be useful to expose the resource values in the event arguments of the OnEdit. The following feature request in our
