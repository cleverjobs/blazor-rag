# Addaptive ToolBar and ToolBarSpacer

## Question

**Con** asked on 03 May 2022

I was trying to create a toolbar that had some buttons alligned on the end (right side) of the toolbar and also using the new Adaptive flag (to also have overflow items) and it seems that the spacer element does not take into account the size of the overflow button at the end. I had to enter an empty label element at the end of the toolbar content elements to get enough empty space for the overflow button not to overlap with the last toolbar button <ToolBarTemplateItem> <label style="width:30px;"> </label> </ToolBarTemplateItem> Is there a better solution or is this a bug that will be addressed in a future release?

## Answer

**Joana** answered on 06 May 2022

Hi Constantinos, I confirm that this is a known issue in our toolbar component. The fix will be included in our themes, and that is why the version in the feedback portal item does not match a Blazor release version. You can track the progress in the following link: [https://feedback.telerik.com/blazor/1564093](https://feedback.telerik.com/blazor/1564093) Regards, Joana Progress Telerik
