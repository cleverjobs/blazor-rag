# Add a "please wait" notification

## Question

**BobBob** asked on 19 Apr 2021

My tabs are taking a little of bit time to change when clicked on making it look like nothing is happening when they click on tab. I need a way to some kind of Please Wait when a tab is clicked on and then goes away once the new tab is rendered. I am thinking something like the three pulsing dots in the tab title while it is working. Is there any way I can achieve this?

## Answer

**Marin Bratanov** answered on 19 Apr 2021

Hello Bob, We have the Loader and LoaderContainer components so you can show indication to your users that something is happening. You can show them when navigation is about to happen, and hide them after the new component is rendered. Regards, Marin Bratanov

### Response

**Bob** answered on 19 Apr 2021

I know about those controls, but how would I use them when changing tabs? The tabs don't navigation anywhere, they just show different data? I tried adding a please wait to the ActiveTabIndexChanged but it didn't work. That event fires when the tab is changed but it's like I would need a before changing and after changing event to show and hide the loader.

### Response

**Marin Bratanov** answered on 19 Apr 2021

Hello Bob, If you are referring only to tab change in a TabStrip and not navigating between pages, you can simply put the loading containers in the components the tab strip renders. They can be visibl by default and getting the necessary data (or the AfterRender event) can hide them. Regards, Marin Bratanov
