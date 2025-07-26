# TelerikMediaQuery - Add support for container queries

## Question

**Ric** asked on 08 Nov 2023

I find myself using css container queries a lot in conjunction with the TelerikDrawer. I would really like to be able to use the MediaQuery control to set parameters based on the container size instead of the screen size.

## Answer

**Dimo** answered on 10 Nov 2023

Hi Rick, This has been requested before ( Feature request for CSS Container Queries ), but currently there is not enough browser API to implement it. Regards, Dimo Progress Telerik

### Response

**Rick** commented on 10 Nov 2023

In the original question you were referenced the MediaQueryList. In the case of individual elements, why not try looking at the ResizeObserver.

### Response

**Dimo** commented on 15 Nov 2023

Hi Rick, Media query events fire once during resizing, when the CSS expression value toggles from true to false or vice-versa. On the other hand, the ResizeObserver fires events continuously during element resizing. This is very inefficient to handle in Blazor and requires throttling. As a result, a Blazor wrapper around ResizeObserver can never work smoothly like the "textbook" example on MDN. So in other words, a potential Blazor component will: Introduce a problem rather than solve one. Duplicate existing browser functionality that one can use already. Not provide any added value, except concealing a few lines of JavaScript code. You may argue that bullets 2 and 3 may also apply to our MediaQuery component, but nevertheless we have it. The reasoning is: Media-query-based responsive designs and algorithms are a lot more common. The step-based MediaQuery behavior allows it to integrate more easily with other components and changes in their configuration. We were reluctant about the MediaQuery component too, and we still are, to some extent.
