# Blazor Scheduler - Show Month-view in a vertical grid

## Question

**Maa** asked on 12 May 2023

Hi All, I schedule a Month at the time but using the MultiDay view because I need 09:00-17:00 in .25 hours a day. Is it possible to use the Month view in a grid of days x hours like the Multiday view. As alternative I would also be happy if I could use the Month-view date-picker TIA Regards, Maarten

## Answer

**Dimo** answered on 16 May 2023

Hi Maarten, The Scheduler's month view displays only days, so it can't be used as a Grid of days and hours. It will be possible to change the label, which opens the DatePicker in the Scheduler toolbar when we implement a Scheduler toolbar template. Please consider voting and following the linked item to receive status updates. I am sorry if the Scheduler does not fully meet your requirements. Regards, Dimo Progress Telerik

### Response

**Maarten** commented on 16 May 2023

Hi Dimo, Thanks for your reply. I voted for the Scheduler Toolbar. Can I have it tomorrow? Regards, Maarten

### Response

**Dimo** commented on 16 May 2023

Maarten - we plan features weeks or months in advance. In theory, the fastest possible option for us is to plan a feature at the beginning of a release cycle for the same release. This means a month and a half from planning to delivery. That's why I suggested following the public feature request, so that you know when we change its status. In the meantime, I have a few alternative options: Hide the built-in DatePicker and use another one outside the Scheduler. You can even position it with CSS, so that it appears to be inside the Scheduler. Use the Telerik Professional Services, which include custom development and the so-called feature acceleration. This is a separate paid offering of ours. Feature acceleration allows you to "escalate" a feature or a bug fix, so that we implement it sooner and it becomes part of the official product. Custom development means that our partners implement a more elaborate workaround of a non-supported behavior. The above REPL example is a very simpler version of that.

### Response

**Maarten** commented on 16 May 2023

Hi Dimo, I was kind of joking (but there aro no emoticons in this editor). Every one who needs a (new) feature wants it yesterday. But it's understandable that this will take time (we know, we're all developers).> Hide the built-in DatePicker and use another one outside the Scheduler How do I hide the datepicker? It is not in the view parameters. TIA, Regards, Maarten

### Response

**Dimo** commented on 16 May 2023

The linked REPL example shows how to hide the built-in DatePicker and label.

### Response

**Maarten** commented on 16 May 2023

Hi Dimo, Tnx! I missed that one, sorry. Regards, Maarten
