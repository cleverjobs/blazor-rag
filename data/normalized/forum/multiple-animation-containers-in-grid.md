# Multiple Animation Containers in Grid

## Question

**Geo** asked on 03 Dec 2020

I have a grid and I want to pop up an animation container with content specific to a row when a button is clicked in that row. How do I reference the correct animation container? No matter which button I click, it always loads the last animation container. I've set @ref="notesPopup" for the animation container in the grid template In code: TelerikAnimationContainer notesPopup; async Task ToggleNotes() { await notesPopup.ToggleAsync(); } I think the question is how do I dynamically set the @ref and reference it in code? Thank you

## Answer

**Nadezhda Tacheva** answered on 08 Dec 2020

Hello George, There is a couple of approaches to achieve the desired results in your case. I have attached an example using AnimationContainer component outside of the Grid to display content specific to a row when a button is clicked in that row (see AnimationContainer.zip) The Notification component is a relatively new component that you also might try in this case. I have attached an example of its implementation to represent its behavior when it comes to generating specific content in different notifications (see Notification.zip) Another option is to go for the Tooltip component - is has a ShowOn parameter that you can easily modify and choose between click on a button or a hover. You may also find useful this sample on adding tooltips to grid rows and loading their data on demand: Tooltips for grid columns with load-on-demand Last but not least, the Window component could also be useful in your scenario. Its benefit is that it can be modal, so the user is unable to interact with the rest of the page until it closes (in case that is behavior that you might want to go for). As for the issue with the component references - this is a problem you'd hit every time you try to use a component reference of components generated in a loop - if you declare that component in the loop, but only one reference field, only the last component will populate that reference. So, you should either use one instance outside the loop (like in my example), or prepare an array of reference fields so you can populate the corresponding component reference in its place. This can easily become difficult to maintain. Regards, Nadezhda
