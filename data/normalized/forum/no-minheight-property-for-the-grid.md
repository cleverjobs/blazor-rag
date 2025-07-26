# No MinHeight property for the grid?

## Question

**RobRob** asked on 26 Nov 2024

I'm having an issue where my users set Desktop scaling to 300% and as a result my grid will collapse and not show any rows of data making users think there is no data. I can Ctrl + Mouse wheel to adjust the browser scaling, but that's not really a good option to convey to users. I've tried using: Height="calc(34vh - 10rem)" Property but not really able to solve the problem no matter how much I adjust the values. What I was hoping to see is a "MinHeight" property for the grid but no such property exists? Am I seeking something isn't possible with the Telerik Grid? Rob.

## Answer

**Dimo** answered on 28 Nov 2024

Hi Rob, Indeed, non-pixel CSS units don't play well with browser zoom and this is a general phenomenon. You can apply a min-height style through a custom CSS class set by the Grid Class parameter. Just be aware of CSS isolation specifics, if you rely on this Blazor feature. Regards, Dimo Progress Telerik
