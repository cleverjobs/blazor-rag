# Grid Scrollbar auto change to default Browser scrollbar but change back to Telerik scrollbar when press F12 to Debug

## Question

**ACV** asked on 06 Apr 2023

Hi, Like Subject above, when I Debug code, my scrollbar change to default browser scrollbar (Image Scrollbar1.jpg) When i press F12 to go to Developer mode, it changes to normal - Telerik scrollbars. Its shadow and it is hard to look little bit (Image Scrollbar2.jpg). I dont know why its happen. And it happended a couple days ago. Browsers that I used to check: Edge, Firefox and Chrome and had same issue. Thank you for your help.

### Response

**Dimo** commented on 07 Apr 2023

Hello Tai, We do not style the scrollbars in any way. The problem must be caused by a combination of application logic, custom CSS and a timing problem (race condition).
