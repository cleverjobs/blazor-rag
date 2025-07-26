# Mobile Gestures?

## Question

**JJ** asked on 11 Jul 2021

Does Blazor UI natively support mobile gestures? I've not been able to find anything in the Docs so I assume not. idk Has anyone had any success incorporating any other frameworks into Blazor UI to add that support? At present, I'm looking at the list control and swiping in left and right to reveal additional menu options (for example like iPhone's Mail app). But I could also see this helpful in the Grid.

## Answer

**Svetoslav Dimitrov** answered on 14 Jul 2021

Hello Jonathan, Mobile gestures are a vast topic and currently, we are hesitant to dive into them and incorporate them into our components. A resource I can offer is the How to create a swipe gesture in Blazor video by one of our developer advocates Ed Charbeneau. In the video, Ed explains in detail how to create a swipe gesture. Another good source of information would be the MobileBlazorBindings repository by Microsoft and the Gestures article from their documentation. Once you have created the swipe gesture you can use the RowTemplate for the Grid together with the AnimationContainer to achieve the desired layout. Regards, Svetoslav Dimitrov Progress Telerik
