# Scrolling issue when opening a context menu in a grid with many rows

## Question

**tuo** asked on 06 Aug 2021

When there are so many rows that the browser has a scroll bar, the context menu that opens automatically moves the scroll bar to the lowest position. Pictures attached showing the problem. Also example code attached.

## Answer

**Marin Bratanov** answered on 06 Aug 2021

Terve Tuomas, This issue stems from the scrollable element in the app (which our components can't control), the fact that the popup of the context menu renders at the level of the TelerikRootComponent, and that it has default focus - this makes the browser attempt to scroll the focused element into view, but it tends to fail to do that for absolutely positioned elements, and this is the result. The following article describes this in more detail and links a sample project that shows how you can control the scrollable element so you don't get this behavior: [https://docs.telerik.com/blazor-ui/knowledge-base/common-popup-causes-scroll-on-show.](https://docs.telerik.com/blazor-ui/knowledge-base/common-popup-causes-scroll-on-show.) On another note, you may also want to set a Height to the grid so that you can control better the layout of the app and so that the users can easily see the pager of the grid. This can also alleviate this issue by eliminating the page scrollbar, but the true fix is still controlling what element scrolls. Regards, Marin Bratanov Progress Telerik

### Response

**tuomas** commented on 09 Aug 2021

That helped me a lot. Thank you!
