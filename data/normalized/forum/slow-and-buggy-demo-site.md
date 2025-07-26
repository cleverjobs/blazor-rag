# Slow and buggy demo site

## Question

**Tin** asked on 30 Sep 2019

Hello, why the demo site is so slow and full of bugs ( duplicated menu, none drop down not working on Firefox , strange side menu behavior on drop down, grid filter menu icon no hand on mouse over... ) . Can we expect the same in implementation? Tino.

## Answer

**Marin Bratanov** answered on 30 Sep 2019

Hello Tino, This is the first time we receive such feedback, and we are not aware of such bugs in the demo site. Could you send me a video or screenshots of what you see? As for the slowness and whether you can expect such a problem in your implementation - this does not come from our components, but from the framework. Our demos are a server-side Blazor project, which is mostly suitable for intranet apps where users are close to the server, bandwidth is high, latency is low, and the number of users are limited. Ideally, our demos should be a client-side project, but this is not possible at the moment, because the wasm flavor of Blazor is not production-ready. So, we will have to stick with the server-side project which may cause slowness due to both network latency, and server loads (server-side blazor apps don't scale well for the server either). What I can suggest you do is download the msi or zip packages we provide and run our demos locally to get a better idea of how things work. Regards, Marin Bratanov

### Response

**Tino** answered on 30 Sep 2019

Hello, as for the slowness, in others it is not so visible ( DevExpess, Syncfusion ). Drop downs ( date picker, date time picker, drop down list ) are so slow that they are not usable ,cca. 1 sec to open close Bugs : - sometimes on drop down open/close, the side menu opens/close. - menus , has already been discussed at forum Sry, can't send videos. Too big files.

### Response

**Marin Bratanov** answered on 30 Sep 2019

Hello Tino, On my end, the DevExpress demos behave just like ours (Telerik) demos in terms of speed, latency and responsiveness. Considering you see different behavior, my best bet is that the network conditions in which we operate are quite different with regard to the demo servers. I am attaching below two traces of what I get to the servers - the latency is similar. Of course, this is only for a ping, which is a lower level request than an actual connection, so those symptoms may not appear in a simple ping test, but you can still give it a go to see what you get. On your end, I expect that there will be significant differences, and the connection to our servers will be slower. Unfortunately, there is nothing anyone can do about this. The problem with a large latency in server-side blazor apps is that it can wreak havoc with the order of events that happen on the client and what the server gets (and responds with). The DOM diff the server will return will become out of sync with the browser because the different SignalR packets will arrive in different (unexpected, wrong) order, and you may get unexpected results because the server can't know better. So, I would suggest that you give our offline demos a try to see how the components actually work. On Syncfusion - their demos are a client-side Blazor app and it takes over 20 seconds to load up on my end, so I would not call that a significant improvement. Moreover, their Blazor components are wrappers over jQuery widgets and not native components. You can read more about our take on native-vs-wrappers in the following article: [https://www.telerik.com/blogs/comparing-native-blazor-components-to-wrapped-javascript-components.](https://www.telerik.com/blogs/comparing-native-blazor-components-to-wrapped-javascript-components.) Of course, after the initial load, a client app does not fire requests to the server to change the DOM (it wouldn't even if their components were native). On the menus - we are aware of a problem where more than one can open at a time, which is, again, a latency problem, and we are working on resolving it. You can track its status here: [https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.](https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.) ------ With all that said, if you continue to experience issues with our components when you run the demos locally, let me know and I will create a ticket for you where you can attach larger files as well, so we can investigate the situation. We are not aware of such severe bugs as you encounter and if they are not caused by network latency, I will need to be able to reproduce the issues in order to investigate, and offer a more concrete answer. Regards, Marin Bratanov
