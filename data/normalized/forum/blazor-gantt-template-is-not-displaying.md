# Blazor Gantt template is not displaying

## Question

**Mor** asked on 27 Sep 2022

Hi! In the blazor gantt demo I can see that it should be possible to costumize the template for mouse over in the gantt-chart, but it does not seem to work. It flickers and does not display any information. Could you please update the example page with a working example? Demopage for template found here: [https://demos.telerik.com/blazor-ui/gantt/templates](https://demos.telerik.com/blazor-ui/gantt/templates) Example page for template not working here: [https://blazorrepl.telerik.com/QwOxHlca49EQ1rgY03?_ga=2.157260347.1214485172.1664189804-2039078829.1642166789&_gac=1.225176296.1661766526.CjwKCAjwx7GYBhB7EiwA0d8oe0Y9E6IZoONYcLxga7yZXoV9ivTM2XM7_bSIJqDDTHjJLd6GLJaQ5RoCJPkQAvD_BwE](https://blazorrepl.telerik.com/QwOxHlca49EQ1rgY03?_ga=2.157260347.1214485172.1664189804-2039078829.1642166789&_gac=1.225176296.1661766526.CjwKCAjwx7GYBhB7EiwA0d8oe0Y9E6IZoONYcLxga7yZXoV9ivTM2XM7_bSIJqDDTHjJLd6GLJaQ5RoCJPkQAvD_BwE) (also linked from the demo page) Thanks in advance Morten Poulsen

### Response

**Nadezhda Tacheva** commented on 30 Sep 2022

Hi Morten, I've tested the Gantt component with a Tooltip template in our demo and locally using the latest UI for Blazor (3.6.1). It looks like the template is rendered correctly - it does not flicker and its content is accordingly displayed. However, I did manage to reproduce the issue in a REPL page. This tells me the problem is related to the REPL tool itself rather than the Tooltip Template of the Gantt. That said, can you please test using the template locally with the latest UI for Blazor and let me know the behavior you are experiencing? If the issue persists, please send us a sample runnable app that reproduces it, so we can debug it. Thank you in advance! In the meantime, I will reach out to our development team to see what might be causing this behavior in REPL. I will get back to you on this once I have more details.

### Response

**Morten** commented on 30 Sep 2022

Hi Nadezhda, Thanks for getting back to me :) I am using the latest version, and I am experiencing the same issue as in the REPL demo, so I am really interested in what causes that behavior so I can undo it. The mouse-over default template is displaying correctly without flickering. Thanks Morten Poulsen

### Response

**Nadezhda Tacheva** commented on 05 Oct 2022

Hi Morten, After further testing, it appears that the issue is only reproducible in a WASM application. The same code tested in a server-side application behaves as expected. At this stage, it is not clear what is causing this behavior. I've logged a bug report on your behalf, so we can further revise it. You may follow the status of the item here: Gantt Tooltip Template does not display its content in WASM application

### Response

**Morten** commented on 05 Oct 2022

Hej Nadezhda! Thank you for submitting the bug. We are currently developing a WASM application, and that explains why I am seeing this problem. Looking forward to work with upcomming releases of Kendo :) Thanks for your help with this issue Morten Poulsen
