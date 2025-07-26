# On page with a Tab Strip how to make form data persist when switching to a different tab and then back to tab with form?

## Question

**Jst** asked on 28 Aug 2021

I have a page with a TabStrip on it. One of the Tabs has a form on it. The user wants to be able to access a tab but then be able to go to the Tab with a form and fill in part of it, go to another tab and then back to the form and fill in some more of the form and then submit the form. Are there any examples of being able to switch between tabs while persisting the data in the form until it is submitted? Each of the tabs consists of a separate component.

## Answer

**Marin Bratanov** answered on 28 Aug 2021

Hi, The Wizard component can let you have such an interface easily: [https://demos.telerik.com/blazor-ui/wizard/overview](https://demos.telerik.com/blazor-ui/wizard/overview) When the following enhancement is implemented, you would be able to have the tabs remain in-memory so their data and state are not lost: [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) If you are interested in that, click the Vote and Follow buttons. For the time being, the solution with the TabStrip (without the Wizard) is to keep the state of the component in an application state above the tabstrip so that that stays in memory. Regards, Marin Bratanov

### Response

**Michael** commented on 02 Dec 2021

I had the same problem with tabs, so as per this post - switched to the wizard. The net effect is the same. When you move between steps, they initialise like new - each time. Just like the tabs do. The only way around this is to put ALL your code in the wizard unit its-self. Kills the idea of of components? My current setup has 5 wizard steps. I have built components for 2 of the steps to test, and switching between the steps re-initialises each time. How to prevent this (without moving component code to the wizard host)?

### Response

**Marin Bratanov** commented on 05 Dec 2021

The ability in the tab strip to hide the tabs with CSS only (so they are all initialized at the same time, all the time) will be available in our next release - 2.30.0. I'd suggest waiting for that. The idea of the wizard was to get you more events and UI more suitable to sequential tasks (things like Prev/Next buttons), sorry for not being clear about that.
