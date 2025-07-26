# Tab Strip - Tab wrapping

## Question

**Dou** asked on 01 Dec 2020

Is there a way to force tabs to wrap when there are more tabs than there is space in a horizontal viewport? I am running into an issue where too many tabs get generated and they end up rendering outside the viewport causing the user to have to scroll. The idea is to render something like this. [Tab 1] [Tab 2] [Tab 3] [Tab 4] [Tab 5] [Tab 6] [Tab 7] [Tab 8] [Tab 9] [Tab 10]

## Answer

**Marin Bratanov** answered on 02 Dec 2020

Hello Doug, You could do it with a relatively simple CSS rule (example below), but the nice appearance where the active tab flows into the content will only work for the bottommost row of tabs and the other rows may look a tad strange. So, I'd suggest enabling scrolling for the tabs as explained here. I've added your Vote for a built-in feature for this that would make it look better than a scrollbar, though. <style>.tabs-container-we-want-to-wrap-tabs { width: 500px; border: 1px solid red;
}.tabs-container-we-want-to-wrap-tabs.k-tabstrip-items { flex-wrap: wrap; /*
Once this gets implemented, you would be able to set the Class directly on the tabstrip instead of cascading through a parent
[https://feedback.telerik.com/blazor/1450831-css-class-for-the-tab-header-and-for-the-entire-tab-strip](https://feedback.telerik.com/blazor/1450831-css-class-for-the-tab-header-and-for-the-entire-tab-strip)
*/ } </style> <div class="tabs-container-we-want-to-wrap-tabs"> <TelerikTabStrip> @{
foreach (var item in Enumerable.Range(1, 20))
{ <TabStripTab Title="@( $" Item { item }" )"> Content for tab @item </TabStripTab> }
} </TelerikTabStrip> </div> Regards, Marin Bratanov

### Response

**Mark** commented on 06 Dec 2021

I've used the above CSS strategy to make the tabstrip appear properly and it worked great but I upgrade recently to the latest version 2.29 and now I notice that the CSS workaround doesn't work. If you paste your code above into a razor component you can see what I mean. Mark

### Response

**Dimo** commented on 06 Dec 2021

@Mark - I added one more answer with the required CSS code for 2.29.

### Response

**Dimo** answered on 06 Dec 2021

Hello Mark and everybody, Here is how to wrap TabStrip tab titles with UI for Blazor 2.29+ <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTabIndex" Class="narrow-tabs"> <TabStripTab Title="Tab 1 Tab 1 Tab 1 Tab 1 Tab 1 Tab 1 Tab 1"> Content </TabStripTab> <TabStripTab Title="Tab 2 Tab 2 Tab 2 Tab 2 Tab 2 "> Content </TabStripTab> <TabStripTab Title="Tab 3 Tab 3"> Content </TabStripTab> </TelerikTabStrip> <style>.narrow-tabs { width: 400px;
}.narrow-tabs.k-tabstrip-items { width: 100%;
}.narrow-tabs.k-tabstrip-items.k-item { flex-shrink: unset;
} </style> @code {
public int ActiveTabIndex { get; set; }=1;
} Regards, Dimo

### Response

**Mark** commented on 06 Dec 2021

It looks like that makes the tabstrip scrollable but the previous css had allowed it to wrap since scrolling on a small screen like a phone isn't a great user experience. Cheers Mark

### Response

**Dimo** commented on 07 Dec 2021

@Mark - the new example should make the tabs wrap. What scrolling are you referring to?
