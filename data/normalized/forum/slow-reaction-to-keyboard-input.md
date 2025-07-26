# Slow reaction to keyboard input

## Question

**Ber** asked on 29 Jan 2021

Hi, I use a window to show a popup in a webassembly blazor project. In this window, I have a grid with +/- 2500 items and some text/date input fields. When I type some text in the textboxes or try to change the date in a datetimepicker with the keyboard, there is a lot of delay. It takes a long time before the typed text is showing in the textbox. When I do the same with +/- 10 items in the grid, it works fine. The filtering in the grid works also fine without any noticable delays. I try to use this project offline, so I need to keep all the grid items in local storage. It's not possible to do some server side filtering. Is there a way to improve this behaviour? Thanks

## Answer

**Marin Bratanov** answered on 29 Jan 2021

Hello Bert, I recommend you review the Slow Performance section of the documentation on improving your WASM app performance. Said shortly, just enable the paging in the grid again. It is OK to keep the data in-memory for offline usage, just avoid rendering 1500 rows, render 10 or 20 by using paging. When you pass the entire data collection to the Data parameter of the grid it will do the paging, filtering, sorting and grouping for you. Regards, Marin Bratanov

### Response

**Bert** answered on 29 Jan 2021

Hi Marin, I'm already using paging (100 rows), but he paging is not server side. I solved it by hiding the grid when not in use. I will try again with lower paging size and see what happens. Thanks

### Response

**Marin Bratanov** answered on 29 Jan 2021

Hello Bert, The grid can handle paging that is not on the server-side, the bigger caveat with that is usually how much data you'll need to serialize to the client first. Whether the paging is server-side or not, I recommend using smaller page sizes anyway. If your users prefer to scroll rather than page, consider the virtual scrolling feature. The idea of both is to reduce the amount of components and dom elements Blazor has to handle, in order to improve the performance. Removing components you don't need is also vital to good application performance. Regards, Marin Bratanov
