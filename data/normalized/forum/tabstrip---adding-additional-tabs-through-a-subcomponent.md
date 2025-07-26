# TabStrip - adding additional tabs through a subcomponent

## Question

**Stu** asked on 09 Oct 2024

I am trying to convert implement the TelerikTabStrip and was largly successful however I have a component that contains conditional logic that adds between 0 and 2 additional tabs to the parent components tabStrip. Unfortuately these tabs are not rendering correctly. I was able to replicate a minimum reproducable example in the blazor REPL environment using the following code. Are you able to advise how I can add tabs to a parents tabstrip, my two rendering issues are: When PersistTabContent is true (works as expected when false) the tabs don't render any content (I need the tabs to persist so turning it off isn't a good fix); and Regardless of if the tabs are persistant or not the subComponent tabs are still shown as "Active" and show the tabs as selected causing the appearence of multiple selected tabs Main.razor <TelerikTabStrip PersistTabContent="true"> <TabStripTab Title="tab1"> <p> tab1 content </p> </TabStripTab> <TabStripTab Title="tab2"> <p> tab2 content </p> </TabStripTab> <TabStripTab Title="tab3"> <p> tab3 content </p> </TabStripTab> <SubComponent /> </TelerikTabStrip> SubComponent.razor <TabStripTab Title="tab4"> <p> tab4 content </p> </TabStripTab> <TabStripTab Title="tab5"> <p> tab5 content </p> </TabStripTab> Screenshots: initial render: Clicking on tab 1, 2 or 3 works as expected: clicking on 4 or 5 shows no content: Then clicking back to 1, 2 or 3 shows 4 and/or 5 as still selected:

## Answer

**Yanislav** answered on 11 Oct 2024

Hi Stuart, The issue seems to stem from Blazor's lifecycle events, and while I couldn’t find official documentation explaining it, I've gathered some insights through experimentation. Basically, the TabStrip is designed to be declarative, and it expects TabStripTabs to be declared as direct children within its ChildContent fragment. Deviating from this design, such as placing tabs inside a third component, alters the lifecycle and rendering order, leading to inconsistencies. As I mentioned, this seems to be a Blazor-specific issue since this behavior changes if a reference type is passed as a parameter to the third component (in your case, the SubComponent ). See: [https://blazorrepl.telerik.com/GelkbbkM28fvm0IE32](https://blazorrepl.telerik.com/GelkbbkM28fvm0IE32) While this might seem as a solution, I want to emphasize that, this is not the intended usage of the component. For reliable functionality, I recommend defining only TabStripTabs as direct children of the TabStrip to ensure the component behaves as expected. I will ensure we address this specific in our documentation. Could you let me know if there’s a specific reason for declaring the tabs inside a separate component? Regards, Yanislav Progress Telerik

### Response

**Stuart** commented on 14 Oct 2024

Hi Yanislav, Thank you for looking into the issue for me, adding the @ref has cause it to render correctly which I suspect is because when the tabstrips lifecycle changes it forces the children associated to it to refresh. The reason I was using a sub component was it was orignally its own tab strip but the design pivoted to add it to an existing tab strip instead which worked fine in blazorise. I have reviewed if there was any reason not to pull it out into the parent component and didn't see any reason not to, so I will move them out of the sub component as recommended. Thank you for your assistance.
