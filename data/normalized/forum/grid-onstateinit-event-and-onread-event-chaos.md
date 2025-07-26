# Grid OnStateInit Event and OnRead Event Chaos

## Question

**Bry** asked on 20 Dec 2023

Here is the problem: When the page first loads, the grid attempts to load the layout defined on the page. This causes a OnRead event to occur as is expected. However, the OnStateInit does NOT fire before this OnRead event. Actually, this is not entirely correct. The initial OnRead is running independent of the OnStateInit, it simply fires and it returns when it feels like it. At some point the OnStateInit fires. I load a saved GridState layout in the OnStateInit event which causes the OnRead to fire again. This causes a couple problems. The grid will load, and then reload as the args.GridState is set in OnStateInit. This causes ugly page flashing, and two data requests when only one is required. Even worse since both requests are async, you are not sure which layout you will get, since the last one to come back is the one you get, which can and does occur randomly. I can return no data for the initial request in OnRead, and this does work, however I can find no reliable way inside of the OnRead event to determine which is the initial load I don't want and which is the OnRead fired from the args.GridState set in OnStateInit which I do want. My question is, how do I prevent the initial grid data request and load? Bryan

## Answer

**Radko** answered on 25 Dec 2023

Hi Bryan, The way the Grid is implemented is that within its OnParametersSet lifecycle event, it would first set its initial state, if applicable, and then invokes the OnRead event. In general, the order should be consistent, meaning the OnStateInit should always be called first. However, you are correct, that setting the Grid's state does trigger a new data fetch, which is also expected, as modifying the state will more often than not need a new data set as well. As for the issue you are experiencing - perhaps the best way to go around this would be to introduce a flag, indicating whether the initial state has been in fact been set. This way, we can avoid executing any logic within our OnRead handler unless the statement is in fact true. Here is a quick example of this: [https://blazorrepl.telerik.com/GHbGQJbE18MohaGm14](https://blazorrepl.telerik.com/GHbGQJbE18MohaGm14) I hope the above helps. Regards, Radko Progress Telerik

### Response

**Bryan** commented on 02 Jan 2024

Thanks for the reply. Earlier, I did try using a flag as you suggested but it also does not work, If we set _initStateSet to true in the OnGridInit event, sometimes the second OnRead request would happen BEFORE the initial request, the _initStateSet would be true and the data would not be loaded. This would happen randomly, about 30% of the time. Yes, this is async hell. The only way to solve this was to determine where the request came from in OnGridRead event using the GridReadEventArgs. I hacked this by using the value args.Request.Skip and setting it to -1 if it comes from the OnGridInit and checking this value in OnGridRead. Since we are not using virtual scrolling, it does work. It might be wise in the future to add another property in the GridReadEventArgs that would indicate where this request comes from so it could determine to load the data or skip it. Bryan

### Response

**Hristian Stefanov** commented on 05 Jan 2024

Hi Bryan, I'm stepping into the discussion on behalf of my colleague, Radko. We are glad to learn that you've resolved this matter and have a solution that works for your case. I've also shared your valuable feedback with our development team. If, after evaluation, there's a consensus on the necessity of adding another property in the GridReadEventsArgs to indicate the source of the request, we'll initiate a feature request on our Public Feedback Portal (Grid section). Kind Regards, Hristian
