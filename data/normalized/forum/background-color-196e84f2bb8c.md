# Background Color

## Question

**Kir** asked on 24 Aug 2020

Hi! I'd like to set different background color to specific date ranges behind the appointments on the scheduler. Is it possible to do? Thanks!

## Answer

**Marin Bratanov** answered on 24 Aug 2020

Hello Kirill, You can follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot.](https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot.) I've added your Vote on your behalf to raise its priority, and I would encourage you to post how you would expect that to be exposed for configuration and what options it will provide (say, a CSS Class for the slot, a Template for the slot, both, or something else). This will let you provide your exact scenario so we can take it into account when implementing this, without me retelling my understanding. Regards, Marin Bratanov

### Response

**Kirill kopenko** answered on 24 Aug 2020

Hi, Marin. I've had this implemented using other tools where I had two collections on a schedule control: one with appointments and one with (in my own project terms) "time slots" which only had start date time, duration and CSS class to render, and were rendered on background. Appointments had a little padding, so background would also be visible. So it could either be two different source data collection, or an appointment may have a flag that turns it into a"timeslot" that gets rendered as a background. Hope, it helps.

### Response

**Marin Bratanov** answered on 24 Aug 2020

Hi Kirill, Thank you for getting back to me, it does help. I pasted that information in the Feedback portal thread to ensure all details are present in one place so they are not missed when reviewed later. Regards, Marin Bratanov
