# TabStrip content scrolling

## Question

**Pau** asked on 22 Feb 2022

I am trying to set overflow:auto on the TabStripTab so that the scrollbar will be contained within each tab (I have some content as a header above the tabs so I do not want the scrollbars to be on the whole page). I am having a lot of difficulty getting this to work. Are there any suggestions for getting this to work?

## Answer

**Dimo** answered on 25 Feb 2022

Hi Paul, To make the TabStrip content scrollable, you need to set height to the TabStrip. Do it with via the Class parameter and a CSS height style. The tricky part is how to define the TabStrip height as " expand to 100%, but minus the header height ". There are two ways to do that: Use a 100% high vertical Splitter with two panes - one with a fixed height and one with no height. Then use a 100% high TabStrip inside the bottom pane. Use generic HTML elements and set the TabStrip height with calc(). Keep in mind that elements with percentage heights require their parents to have an explicit height. <div class="body"> <!-- height: 100% --> <div class="page-header"> <!-- height: 60px --> This text does not scroll. </div> <TelerikTabStrip Class="tabstrip" /> <!-- height: calc(100% - 60px) --> </div> Regards, Dimo Progress Telerik

### Response

**Paul** commented on 25 Feb 2022

My problem is that I don't always know the height of the header. I was trying to use a flexbox or grid to allow the tab contents to grow 100% and have the header be auto height.

### Response

**Paul** commented on 25 Feb 2022

I also tried your example, and the whole page scrolls, not the tab's content. app.css: html, body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; height:100%; } .body { height: 100%; } .tabstrip { height: calc(100% - 60px); } .page-header { height: 60px; } index.razor: <div class="body"> <!-- height: 100% --> <div class="page-header"> <!-- height: 60px --> This text does not scroll. </div> <TelerikTabStrip Class="tabstrip"> <!-- height: calc(100% - 60px) --> <TabStripTab Title="Test"> <div style="height:2000px"></div> </TabStripTab> <TabStripTab Title="Test 2"></TabStripTab> </TelerikTabStrip> </div>

### Response

**Dimo** commented on 25 Feb 2022

In a Blazop app there is (at least) one more element that needs a 100% height style in such a layout - the <app> or <div id="app"> element. Check the page HTML output with the DOM inspector. The other problem is more tricky, if fixed dimensions cannot be set. I made some experiments, but wasn't able to achieve the desired layout with flexbox without an appropriate correct height for the TabStrip.

### Response

**Paul** commented on 10 Mar 2022

Thanks for the help.
