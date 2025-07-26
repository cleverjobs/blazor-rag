# Button Tooltip (title)?

## Question

**Jef** asked on 22 Jun 2021

I'm sure I'm just being stupid.. but.. I can't figure out how to add a title/tooltip to a button.... a <GridCommandButton> to be specific. +6

## Answer

**Hristian Stefanov** answered on 22 Jun 2021

Hi Jeffrey, Such questions are important for us because they indicate where to improve our documentation. The easiest way to achieve the desired result is to set the Title parameter of the GridCommandButton, and then pass it to the TargetSelector of your Tooltip. The described approach is showcased in the attached sample project. I hope this helps. If you have any other questions, don't hesitate to contact us again. Regards, Hristian Stefanov Progress Telerik

### Response

**Jeffrey** commented on 22 Jun 2021

Thanks Hristian... I guess I could have just tried the obvious but when I started to type "Title" it didn't show up as an option in the intellisense menu so I just assumed it wasn't a valid parameter.
