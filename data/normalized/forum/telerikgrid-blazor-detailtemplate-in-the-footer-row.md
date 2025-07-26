# TelerikGrid Blazor DetailTemplate in the footer row

## Question

**Arn** asked on 07 Nov 2023

Hi, I have a Blazor TelerikGrid using the DetailTemplate feature to expand each line. It works fine but I would also need to expand the footer line. Is there a way to do that? Also, is there a way to display the DetailTemplate "+" expand button on the RIGHT rather than on the left? I don't see any properties that would allow this. Thx A

## Answer

**Dimo** answered on 10 Nov 2023

Hello Arnaud, The desired result requires you to: Hide the default hierarchy expand column with custom CSS. Add another column with a template for expanding and collapsing the detail templates from the Grid state. Note that when you expand the footer, there will be no single "detail template", which spans across the whole footer row. Instead, you will have a small "detail template" inside each footer cell in each column. You can start from this REPL example. Regards, Dimo Progress Telerik

### Response

**Arnaud** commented on 01 Dec 2023

Hi Dimo, I agree that your solution would have worked in most cases. It was not an option in my case as what I wanted to display in the expanded row could not be split over several columns. Alternatively, I moved the total data that were meant to be displayed on the footer expanded row. I added it into my items collection so that I don't need a footer for total anymore. Well, quite a poor solution but worked for me...
