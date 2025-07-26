# Problems using ContextMenu and DropDownList in a Dialog

## Question

**Hen** asked on 19 Sep 2022

When I try to open a ContextMenu or a DropDownList within a Dialog the x and y coordinates of the dropdown have offsets. It seems to me that they still refer to the main "window". Is there any way to avoid that problem ?

## Answer

**Joana** answered on 22 Sep 2022

Hi Hendrik, The incorrect position of the popups might stem from an additional styling added to the app. We have created a documentation troubleshooting section about possible causes. [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position) Could you please verify that there are styles that interfere the position of the popup? Regards, Joana Progress Telerik
