# Flag specific schedule entries as uneditable?

## Question

**And** asked on 28 Aug 2020

Is there a way to specify that only certain entries are not editable, as opposed to the entire Scheduler component? I'm currently working around this by immediately returning from the CRUD handlers if they attempt to operate on one of the events. This is unexpected UX, since these entries look like they should respond to CRUD operations like "regular" entries. Alternatively, how can I specify certain dates as outside of work hours? Specifically looking at things like federal holidays; Christmas, for instance, should never have an entry from a user. Thanks, Andrew

## Answer

**Marin Bratanov** answered on 28 Aug 2020

Hi Andrew, The difference between an editable and non-editable schedulre is that the editable one leaves some padding next to the appointments so you can double click to add an overlapping appointment (see more here ). The appointments themselves are not different, and to prevent the user from editing some of them you can use the OnEdit handler and cancel it based on the desired conditions (an example here ). If you want to distinguish such appointments, for the time being you can amend something in their title so it renders in the scheduler. Once appointment templates become available, you will be able to tweak that as well. On marking non-working hours, the general feature is the working day start and end features of a view, you can read more here and see how that gets colored here, for example. For marking some appointments as being in wrong time slots or as holidays - the appointment template would provide flexibilty, and for the time being you could use a resource to color them differently. You could probably use a resource to also mark non-editable appointments too, but only one special coloring can be applied through that. In case you are looking at marking the scheduler slots themselves, this feature would let you do that. I've added your Vote on your behalf for both feature requests to raise their priority, and you can click the Follow button to get email notifications for status updates. Regards, Marin Bratanov
