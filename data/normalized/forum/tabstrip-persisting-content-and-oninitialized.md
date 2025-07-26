# TabStrip, persisting content and OnInitialized

## Question

**Ram** asked on 14 Mar 2022

Hello, I ran into a small quirk when using the Blazor TabStrip component. If I have a list of models for the tabs to be initialized from and I don't set PersistTabContent to be true, only the first tab will call a components OnInitializedAsync method. If I do set PersistTabContent to true then the components get their OnInitializedAsync called, but only once as is to be expected. On the other hand, if I have "hardcoded" the TabStripTabs, then the OnInitializedAsync is called. Is this a bug or am I doing something weirdly? A small demo can be seen at [https://blazorrepl.telerik.com/cmadPIvY25vWwvTi23](https://blazorrepl.telerik.com/cmadPIvY25vWwvTi23) where if you open the browser devtools and goto the console tab, you can see that when you change the active tab on the upper Strip, OnInitializedAsync is not called if PersistTabContent is false. Regards, Rami

## Answer

**Marin Bratanov** answered on 15 Mar 2022

Hi Rami, I don't see a difference in the behavior of both tab strips, and in the default case, each tab will initialize only when activated. What perhaps is important to note is that you may want to use the @key directive to properly instruct the framework when to initialize the child component. Take a look here for more details and examples: [https://docs.telerik.com/blazor-ui/components/tabstrip/tabs-collection](https://docs.telerik.com/blazor-ui/components/tabstrip/tabs-collection) Regards, Marin Bratanov

### Response

**Rami** commented on 16 Mar 2022

Thank you Marin! The @key was what was missing, I apparently didn't read the docs properly. Now the OnInitialized is called for all tabs on both strips. So for anyone stumbling into the same thing, adding the @key to the below snippet fixes this issue like Marins link says. <TabStripTab Title="@t.ToString()"> <SpecialComponent ID="@t" @key="@t" /> </TabStripTab>

### Response

**Remzy** commented on 06 Apr 2023

I watned to do the same thing and it is not working for me. since all the components in the tabs register events, I wanted to initialize all of them. only the component in the first tab is initialized and receive events. I added different @key attribute to all of them and still not working. Also, Rami's code does not initialize all the components in all tabs as he said in his last reply with @key added. any help?

### Response

**Yanislav** commented on 11 Apr 2023

Hello Remzy, Please feel free to let me know if I have misunderstood anything, but based on the information provided, it appears that the issue you are addressing differs somewhat from the one previously discussed in this thread. If I understand correctly your goal is to load all tabs' content initially. Is that correct? For performance reasons, the tabs are not initially rendered and only become visible when activated or selected. This is because DOM operations are generally slow, and rendering all tabs at once could negatively impact the performance of not just the TabStrip, but also the entire page. That being said my recommendation is to avoid trying to load all the content at once. In case you have any other questions or if further assistance is needed, please do not hesitate to contact us.
