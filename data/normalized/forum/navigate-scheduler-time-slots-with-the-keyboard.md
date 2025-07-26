# Navigate Scheduler time slots with the keyboard

## Question

**Mik** asked on 19 Feb 2025

Is there a way to navigate the time slots of the scheduler using only the keyboard? The scheduler in the UI for Asp.NET Ajax had this ability. Without this, how does a keyboard only user navigate the scheduler to add new appointments? Thanks, Mike

## Answer

**Hristian Stefanov** answered on 20 Feb 2025

Hi Mike, The Scheduler in UI for ASP.NET Ajax has a slot selection feature that is currently not available in the Blazor Scheduler component. A feature request for this functionality has already been submitted on our public feedback portal: Drag over the slots to create an appointment in them. I’ve voted for this request on your behalf and increased its priority. You can also subscribe to the item to receive email updates on its progress. On a side note, I don't see a strong need for navigating between time slots manually, as the recommended shortcut for creating an appointment is " c ", which lets you specify the time slot directly without having to cycle through any empty slots until you find the right one. Regards, Hristian Stefanov Progress Telerik
