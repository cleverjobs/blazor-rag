# blazor telerik virtualization of remote data for grid

## Question

**kha** asked on 22 Oct 2019

hi im using TelerikGrid and i wanted this feature to request for a part of data and when client scrolled down to that part of data then do another request to get second part of data i wanted to know if this can be done right now and if not when will this feature be added ?

## Answer

**Marin Bratanov** answered on 22 Oct 2019

Hi, The virtual scrolling feature does that automatically if you have provided the entire data source to the grid at once - it will take only the needed items and render them. If you want to fetch them on demand yourself, you will need to use the OnRead event (you may want to check your other thread for some issues that I saw in the initial implementation that was posted). Make sure to use its Skip parameter to take the offset (see here ). Regards, Marin Bratanov
