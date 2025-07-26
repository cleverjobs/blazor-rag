# Grid: show Loading component on filter or page size changes

## Question

**Eri** asked on 12 Oct 2023

I am working with a grid that uses paging. One of the options I expose to the user is to allow for a page size of "all" to show all records. When selected, it can take the grid 10-20 seconds to display all those records, but there is no indication to the user that there is processing going on. I saw another ticket that mentioned using the PageSizeChanged & onRead event to display a loading image, but that loading image is still delayed. Is there another way to achieve the goal of showing a loading spinner when the grid is doing larger operations. Paging, filtering, etc... Thanks in advance

## Answer

**Dimo** answered on 13 Oct 2023

Hello Eric, If the LoaderContainer displays with a delay, this can be due to a blocked UI thread. Is this what you want to achieve - Grid with LoaderContainer and PageSizeChanged Regards, Dimo Progress Telerik
