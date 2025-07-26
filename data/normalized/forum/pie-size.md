# Pie size

## Question

**Emi** asked on 09 Jan 2023

Hello, Is there a way to change to size of the pie chart. It seems there is a lot of whitespace available for the chart in the svg that is drawn, compared to other chart types.

## Answer

**Svetoslav Dimitrov** answered on 12 Jan 2023

Hello Emil, These whitespaces are expected by design, let me provide some information: The Pie Chart offers labels for each distinct segment. One way to render these labels is by drawing lines from the Chart outside and the respective value: The space that these labels might take must be taken under consideration when rendering the pie chart. So why don't we render the chart with tight space around it and just add the necessary space when/if the labels are rendered? The reasoning behind that is that adding new space will cause the UI of the application to change and possibly be broken. Another aspect of the Pie Chart that must be accounted for is the Title that is rendered above the Chart. The reasoning is very similar like for the labels from the above paragraph. I hope this makes sense, let me know if you have any further questions. Regards, Svetoslav Dimitrov
