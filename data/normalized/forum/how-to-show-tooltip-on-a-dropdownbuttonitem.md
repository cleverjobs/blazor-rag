# How to show Tooltip on a DropDownButtonItem

## Question

**NiV** asked on 31 Aug 2023

Hello. I would like to show a tooltip on a DropDownButtonItem, I tried but without success. This is the Repl link. May you kindly help me? Thank you.

## Answer

**Hristian Stefanov** answered on 05 Sep 2023

Hi Fabio, Thank you for providing me with a runnable sample. I carefully reviewed it, and I'm ready to help you achieve your goal. The DropDownButtonItems options are rendered inside a popup. Consequently, the problem stems from the way the Blazor framework renders popups. Therefore, to ensure the tooltip functions as intended for these options, it's essential to relocate the HTML span element within the " DropDownButtonItem " tag. I modified the sample on your behalf, and I'm sending it back: @using Telerik.SvgIcons; <!-- A tooltip should appear in the DropDownItem2, but doesn't appear. --> <TelerikTooltip TargetSelector=".test[title] " /> <TelerikDropDownButton> <DropDownButtonContent> DropDownButtonContent </DropDownButtonContent> <DropDownButtonItems> <DropDownButtonItem Icon="@SvgIcon.ChartAreaClustered"> DropDownButtonItem1 </DropDownButtonItem> <DropDownButtonItem Icon="@SvgIcon.ChartAreaRange"> <span class="test" title="This is the tooltip for DropDownButtonItem2"> DropDownButtonItem2 on which should appear the tooltip </span> </DropDownButtonItem> </DropDownButtonItems> </TelerikDropDownButton> Please run and test it to see the new outcome. Regards, Hristian Stefanov Progress Telerik
