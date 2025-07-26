# TelerikGrid DetailTemplate not rendering when it has GridAggregates with InteractiveServer rendermode

## Question

**Mic** asked on 31 May 2024

(.Net 8, Telerik Blazor 6.0.0) Adding GridAggregates to a detail template when running in InteractiveServer mode appears to cause it not to render the detail grid, although the rows are "there". The attached example has grouping activated on the detail grid. Grouping by a column, the rows appear. I tested this on Telerik.UI.for.Blazor.Trial 5.1.1 and it works fine (rows always render), so it seems to be a problem on 6.0.0. We have quite a few DetailTemplates with GridAggregates so would appreciate feedback on this. Attaching an example taken from Telerik examples. Many thanks, Michael.

### Response

**Al** commented on 01 Jun 2024

I have also run into this. Reverting to 5.1.1 restores correct behavior.

## Answer

**Tsvetomir** answered on 03 Jun 2024

Hello Michael and Al, Thank you for the provided information related to the issue you are encountering. I can confirm that for the described behavior there is an already reported bug in our feedback portal: [Regression] Grid with aggregates never loads if data comes asynchronously. The item is already in development and we are planning to release a Patch version in a few days, which will include the fix for it. I hope the provided information serves you well in addressing your situation. Regards, Tsvetomir Progress Telerik

### Response

**Michael** commented on 03 Jun 2024

Hi Tsvetomir, Thanks for the reply. In the meantime, can you please tell me where I can download a non trial version of 5.11, so that I don't have the limitations of the trial version? Many thanks, Michael.
