# TabStripTab templates or possiblity for content

## Question

**Mor** asked on 01 May 2020

I want to put an icon on the tab, example a google font icon I tried something like this (so you hopefully can see where I'm going): <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTabIndex"> <TabStripTab Title="Sofia"> </TabStripTab> <TabStripTab Title="London"> </TabStripTab> <div class="material-icons project tab-item"> security <TabStripTab Title="Azure RBAC"> </TabStripTab> </div> </TelerikTabStrip>

## Answer

**Marin Bratanov** answered on 01 May 2020

Hi Morten, You can Follow the implementation of such capabilities in this page: [https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.](https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.) I've added your Vote for it on your behalf and I posted a modified hack that shows how you could step on some of the built-in classes and markup structure to get something similar to a template. Regards, Marin Bratanov

### Response

**Morten** answered on 01 May 2020

Ok thanks. I'll try it out and/or wait :)
