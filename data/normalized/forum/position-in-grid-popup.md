# Position in Grid Popup

## Question

**Kev** asked on 26 Nov 2020

Hi, Im having problem when using Datetimepicker on Grid popup it sometimes go below the visible area and and couldn't be scrolled. If I put a datepicker at the same place it will be able to work out if it should pop up below or above the input but datetimepicker doesn't seem to do this. Any solution or walk around for this? Thanks! Kevin

## Answer

**Marin Bratanov** answered on 27 Nov 2020

Hello Kevin, You can Follow the improvement on the component for such scenarios here: [https://feedback.telerik.com/blazor/1459721-make-the-time-picker-popup-always-fit-in-the-screen-mostly-for-mobile.](https://feedback.telerik.com/blazor/1459721-make-the-time-picker-popup-always-fit-in-the-screen-mostly-for-mobile.) I see that you have added your Vote for it yesterday, and the best way to know when an update is available is to click the Follow button on that page - this will send you email notifications when something happens (say, we know its release). Generally, if there is enough room in either direction for the popup, it will detect the edge of the viewport and expand down or up, depending on where there is room. When there is not enough room in either direction is the real problem. So, perhaps moving this column earlier in the grid will put that editor higher up in the list, so there will be room below it. If that's feasible for your project, you could give that workaround a try. Regards, Marin Bratanov
