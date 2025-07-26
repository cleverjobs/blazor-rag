# Month Change Event on Date Picker

## Question

**Ric** asked on 13 Jan 2023

We color code each day of the week based on a service call. Is there a way to know when the month is changing so that we can fire our service call event and populated disabled dates and colors for the calendar cells? One idea I had was when rendering the cells, check to see if the first is being rendered then fire the service call event. Doesn't seem like the best option as that would cause the rendering to pause while the call was being executed.

## Answer

**Nadezhda Tacheva** answered on 18 Jan 2023

Hi Ricky, At this stage, such an event is not available, however, we've already received a request for exposing it: Event for when the month has been changed (DateChanged) I added our vote to increase the popularity of the feature. We track the gathered community votes to evaluate the demand for the requested enhancements which helps us to prioritize them. You may additionally follow the item to get status updates. For the time being, you may try the workaround suggested in the public post - using the Calendar component which currently exposes DateChanged event. Regards, Nadezhda Tacheva
