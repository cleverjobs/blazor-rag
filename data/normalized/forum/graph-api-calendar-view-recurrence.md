# Graph API Calendar View Recurrence

## Question

**Chr** asked on 20 Aug 2024

Hello. I call the graph api for outlook, getting users' calendar events. I use the calendar view, which get events based on a start and end date range and then that is used to populate the data for Telerik Scheduler. However, when doing it this way, it will retrieve only the occurrences and not the master event(The symbol for recurring series does not even show up for Scheduler). So when I try to double click on an occurrence from a series, it will not ask if it's for the single occurrence or the series, it will automatically go straight for the edit of the single occurrence. Is there a work around to edit the series without a custom form when getting events by the calendar view call from graph api? Also, when reading the events from calendar view api call, there is no recurrence rule on the occurrences, but there is a series master id they share.

## Answer

**Nadezhda Tacheva** answered on 23 Aug 2024

Hi Christopher, As a start, I want to list a key point for the recurring appointments. A recurring appointment is presented by a single record in the Scheduler data that includes the desired recurrence rule. The Scheduler uses that rule to make clonings of this item that will be visualized as its occurrences in the corresponding periods. The actual data, however, is not changed, it still contains only one record for the recurring appointment representing the whole series. Based on your description, I understand that the retrieved data contains the occurrences as separate events. For the Scheduler, however, they will not be treated as part of the whole series due to the details I listed above. The Scheduler data should not contain the occurrences, the Scheduler creates them based on the original (main) event and the RecurrenceRule it has. That said, to ensure the Scheduler will create a series, you must include the main event in the component data and set the needed RecurrenceRule. You can reshape the retrieved data before passing it to the Scheduler to follow these requirements. Otherwise, you would need to simulate reccurring events and create a custom edit form. Regards, Nadezhda Tacheva
