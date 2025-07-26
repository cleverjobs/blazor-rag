# Feature Parity with KendoUI for Angular

## Question

**Mic** asked on 25 Nov 2021

Hello, I'm looking into the question which version of the Telerik UI stack would best fit my requirements and am wondering how much feature parity exists between the Blazor UI controls and Kendo UI for Angular. List of controls? It seems the "standard controls" are available, but I didn't do a deep dive / side by side comparison. I'm just looking for general guidance here. Availability of the testing framework abstraction layer showcased in this blog article: [https://www.telerik.com/blogs/automated-testing-of-kendo-ui-made-easy](https://www.telerik.com/blogs/automated-testing-of-kendo-ui-made-easy) Many thanks, Michael

## Answer

**Marin Bratanov** answered on 25 Nov 2021

Hi Michael, I would suggest you choose the framework based on factors like your team's expertise and experience, your company's needs, goals and plans, integration with other products you intend, and so on. I'd say that the UI stack plays a smaller role than those considerations. What I can say at this point is that the Angular suite will have more features simply because it is significantly older, Blazor as a framework is barely two years old, but already had 90 native components. So, the general UI capabilities are likely to be met by any of our suites. Regards, Marin Bratanov Progress Telerik

### Response

**Michael** commented on 30 Nov 2021

Hi Marin, thank you for your feedback on this. Yes, the points you've mentioned I've summarized as "requirements". It's great to see that Blazor is catching up but your answer also means that I will still need make sure that all features that are needed will be available. I'll have to do this anyway, but when there's multiple choices, I'll have to evaluate each one. Thanks, Michael

### Response

**Marin Bratanov** commented on 01 Dec 2021

Thank you for your understanding, Michael. To be a little blunt - I simply can't make that decision for you, choosing the framework has lots of implications, and the UI component set is not the largest of them. I understand it takes effort, but robust planning can save you from lots of headache down the road.

### Response

**Michael** commented on 09 Dec 2021

Hello Marin, I'm sorry if I wasn't precise on this. I am not looking for someone to make this decision for me. I was only looking for a documented feature matrix for an efficient comparision of the different libraries You know, something like [https://caniuse.com/](https://caniuse.com/) or [https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#browser_compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#browser_compatibility) with which I can quickly identify if a specific Telerik control library exposes a blocking issue (missing feature). Best regards, Michael

### Response

**Marin Bratanov** commented on 11 Dec 2021

Thank you for the clarification, Michael. To be a little blunt, I doubt we would ever do that. All component suites evolve at such a great pace that maintainting such a resource would be a major resource drain. For example, in Blazor we ship new releases roughly every 6 weeks, and all of them contain new features as well as fixes. Other suites also have quick release cadences, and making such a matrix takes a long, long time. Thus, the approach I can suggest you take is to go through the demos and documentation of the component suites you are considering when you choose a framework. After the framework itself has been selected, there would be likely one choice of a component suite targeting that framework anyway, so if you need something you can't find in the documentation, demos and api reference, it is best to reach out and ask the specific question. Perhaps there will be a way to achieve it right now.

### Response

**Michael** commented on 11 Dec 2021

Hello Marin, thank you for the update and info on the release cadence. This also helps. Best regards, Michael
