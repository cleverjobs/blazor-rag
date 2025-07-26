# Virtual Scrolling performance issue

## Question

**BenBen** asked on 04 Nov 2019

Hi I'm currently running a trial of Blazor UI, taking a look at the Grid and Virtual Scrolling. I've noticed a fairly heavy performance issue on chromium based browsers, bad enough that I wouldn't be able to release to production in it's current state. My project is Server Side Blazor and the performance issues seem related to mouse over/move, my grid currently only has a single item in it so no actual scrolling happening. I've tried with asp core 3.0 and 3.1 preview. Firefox and MS Edge 44 runs the page just fine. CPU usage for the Tab is very high during mouse movement and when taking a look at the browser tools Performance profiler a very long amount of time is spent Recalculating Styles and Updating the Layer Tree as attached. Anyone had experience with similar issues or know of a fix? Regards Ben

## Answer

**Marin Bratanov** answered on 04 Nov 2019

Hi Ben, Does providing enough data so that there is scrolling help? It is a requirement for virtual scrolling to work (see here ), relevant quote from the docs: Provide for a PageSize of the Grid that is large enough, so that the loaded table rows do not fit in the scrollable data area For example, does our demo have suitable performance for you? You can also run it locally in case your latency to our server is large. Regards, Marin Bratanov

### Response

**Ben** answered on 10 Nov 2019

Hi Mark I'll give this a go early next week, there is a noticeable performance difference between Firefox and Chromium on the demo page as well so I'm not sure it's related to the amount of data. It might be that the grid is doing something that highlights an area where chromium performance is lacking but I wouldn't a clue on how to prove or confirm that. Regards Ben

### Response

**Marin Bratanov** answered on 11 Nov 2019

Hi Ben, There is something I just noticed - in the original trace the origin of those events seems to be either jQuery, or bootstrap.js - neither of which are dependencies of ours. This leads me to believe that some code outside of our grid is attaching handlers that might be causing this. If trimming the problematic code (or testing our demo ) does not help you resolve this, I will need you to send us a small runnable example that showcases the problem in a proper configuration (that is, with enough data) and a proper stack trace that showcases the issue, so we can investigate in more detail. It would be best if you can reproduce this in our demo or with the code from the demo, because this will provide is with a shared codebase for testing. If our demo does not have this problem for you, it probably comes from something in the actual project you have and you should be able to start removing bits and pieces to see which is the offending code. Regards, Marin Bratanov
