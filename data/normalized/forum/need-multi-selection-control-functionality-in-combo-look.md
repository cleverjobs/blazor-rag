# Need Multi selection control functionality in combo look

## Question

**Him** asked on 17 May 2023

Need Multi selection control functionality in combo look means i need to put arrow icon with multi select telerik control and on click of that icon will appear the list box for selection as like in combo/dropdown control

## Answer

**Nadezhda Tacheva** answered on 18 May 2023

Hi Himani, You can programmatically open the popup of the MultiSelect when needed by invoking its Open() method. If you want to use just an icon for opening the popup, you should consider the proper place to add it. By design, when at least one item is selected, the MultiSelect renders an "X" icon at the end of its input. Having this in mind, you may consider using a Button and handling its OnClick to open the popup (similar to the ComboBox look). You may also add some CSS adjustments to style the components in the desired way. By design of the MultiSelect, when the selected items do not fit in one line, the component will expand to show them all. In this scenario, you need to either increase the height of the button as well or use the summary tag mode when available. I would recommend the second approach for this scenario. For the time being, a possible workaround is to restrict the MultiSelect height with CSS. Note: I noticed that currently, the MultiSelect appears a bit taller than the button. I will inform the team about that to address it in the next possible release. In the meantime, you can also handle that with some CSS. I've prepared a runnable sample to showcase the approach: [https://blazorrepl.telerik.com/cxkTlsYW37sqBdPV41.](https://blazorrepl.telerik.com/cxkTlsYW37sqBdPV41.) I hope you will find the above information and sample useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Himani** commented on 30 May 2023

How to check the suggestion list is already open or not, which helps to close the suggestion list only if it is open

### Response

**Nadezhda Tacheva** commented on 02 Jun 2023

Hi Himani, You may handle the OnOpen and OnClose events which fire when the popup is about to open or close. You may manage a flag in the handlers of these events based on which to execute your desired log. I hope this helps.
