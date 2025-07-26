# Standard Navigation bar stopped working after 2.26 update

## Question

**alm** asked on 23 Aug 2021

I have a project that is based on the standard "sever side blazor" project template in Visual Studio. It's been working more or less fine over the past year and has had the Telerik package there from the beginning. The project makes extensive use of Telerik' blazor controls. When I updated to 2.26, my nav bar suddenly disappeared. I can step through the code but nothing displays. I am pretty sure there is some kind of CSS conflict going on, but I'm just not savvy enough here to diagnose the issue.

## Answer

**Svetoslav Dimitrov** answered on 26 Aug 2021

Hello Eric, The best way to determine which part of the CSS conflicts is to chunk delete/comment out parts of the CSS file. For example, you can comment out the first 50 lines of CSS and run the application and if it still does not behaves as expected you can comment out the next section. It might be a bit handful, but there is no good way to debug CSS files. I hope this helps you move forward with your application. Regards, Svetoslav Dimitrov
