# Blazor Scheduler Component Recurrence Prompt Question

## Question

**Ste** asked on 14 Jan 2021

I'm in the same situation as the OP in this post: [https://www.telerik.com/forums/how-do-you-always-edit-series-when-editing-a-recurring-appointment](https://www.telerik.com/forums/how-do-you-always-edit-series-when-editing-a-recurring-appointment) In my case, I'm working with with the Blazor Scheduler Component. How can I disable the prompt and automatically select "Edit the series"? Or at least "disable" the "Edit this occurrence" button when updating/deleting an appointment?

## Answer

**Marin Bratanov** answered on 14 Jan 2021

Hello Stefan, I made this feature request on your behalf so you can Follow the implementation of such a feature: [https://feedback.telerik.com/blazor/1502395-ability-to-directly-edit-an-occurence-or-the-series-without-the-prompt-asking-you-to-choose.](https://feedback.telerik.com/blazor/1502395-ability-to-directly-edit-an-occurence-or-the-series-without-the-prompt-asking-you-to-choose.) At the moment, the only idea I can offer is using a custom editor dialog: [https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form](https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form) Regards, Marin Bratanov
