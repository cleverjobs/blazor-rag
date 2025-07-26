# TelerkGridLayout not rendering

## Question

**JaiJai** asked on 24 Aug 2023

I had a problem with the TelerikGridLayout, in conjunction with a MediaQuery where on First render it was not rendering any of the objects. After a lot of investigation I found an article that used an IEnumerable to bind to the grid and not a list. After using an IEnumerable, my objects rendered perfectly and were responsive. Anyone having problems with the TelerikGridLayout, make sure to use an IEnumerable and not a List to bind to the grid.

## Answer

**Svetoslav Dimitrov** answered on 29 Aug 2023

Hello Jai, Can you send us a runnable reproducible of the issue you are facing? I am asking because the TelerikGridLayout is not a data-bound component and it must not be affected by the type of a data collection. If you actually meant the TelerikGrid (Data Grid) it must work with List as well as IEnumerable. I will highly appreaciate your assistance. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Jai** commented on 29 Aug 2023

Hi there If you look at support ticket 1621013 you will see the code that I had. It was using a List. As I mentioned in this post, once I changed to an IEnumerable, it started working perfectly, that's why I created this post. The problem was weird. It wouldn't render on first render, but when you resized, it would render.
