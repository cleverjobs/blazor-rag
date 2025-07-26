# Day of Month slightly cut off in Month View with Bootstrap Theme

## Question

**Mik** asked on 20 Feb 2025

When using the Bootstrap theme with the scheduler, appointments are cutting off the bottoms of the Day Number in the cell. Is there an easy way to add a margin to the first appointment in each day cell so that all of the appointments in the cell shift down and don't overlap the number? Here's a repl of what it currently looks like: [https://blazorrepl.telerik.com/mJkQmEvU03c6KHyg35](https://blazorrepl.telerik.com/mJkQmEvU03c6KHyg35) Thanks, Mike

## Answer

**Tsvetomir** answered on 25 Feb 2025

Hello Mike, Thank you for the provided REPL. I assume the described issue is related to the Month View of the Scheduler. To shift down the appointments with a small margin, use the following CSS: .k-event { margin-top: 2 px;
} This will ensure that there is enough space between the number and the appointment. I hope this serves you well in continuing with your project. Regards, Tsvetomir
