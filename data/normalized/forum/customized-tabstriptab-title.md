# Customized TabStripTab Title

## Question

**Tam** asked on 05 Mar 2020

I am using TabStrip to display steps of a process. When any of the steps is completed, I would like to mark that tab. Ideally, I would like to put a checkbox in the tab title. Alternatively, placing an icon into the title would suffice. As a last option, if any of the previous ones are not possible, I would like to control the style of individual tabs with CSS. Is any of this possible?

## Answer

**Svetoslav Dimitrov** answered on 06 Mar 2020

Hello Tamas, Yes, you could do it with CSS. You can wrap the entire TabStip with a <div> and append a class to it. After that you can select the TabStrip Tabs and manipulate them. Here is a short code snippet to demonstrate targetting the tabs before the selected one, and those after it: <style>.tab-parent.k-tabstrip-items li { color: yellow;
}.tab-parent.k-tabstrip-items li.k-state-active,.tab-parent.k-tabstrip-items li.k-state-active ~ li { color: cyan;
} </style> <div class="tab-parent"> <TelerikTabStrip> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> <TabStripTab Title="Fourth"> Fourth tab content. </TabStripTab> </TelerikTabStrip> </div> That would be made easier by a Class parameter the tabs could expose, and you can Follow the status of this feature here (I added your Vote on your behalf): [https://feedback.telerik.com/blazor/1450831-css-class-for-the-tab-header-and-for-the-entire-tab-strip.](https://feedback.telerik.com/blazor/1450831-css-class-for-the-tab-header-and-for-the-entire-tab-strip.) On the topic of adding check box or icons - to do that, a template would need to be implemented in the tab strip for the tab titles, and here is an open feature request in our Feedback Portal that you can use to Follow its implementation: [https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.](https://feedback.telerik.com/blazor/1419293-tab-strip-label-template.) I have already given your Vote for it too. Regards, Svetoslav Dimitrov

### Response

**dcadler** answered on 18 Mar 2020

Svetoslav, What is the css style for the Tabstrip tab body? .k-tabstrip-content? I am wrapping the entire tabstrip in a div and adding a class to that dive as you recommended to change the appearance of the tabs themselves but I would like to change the background color of the tabstrip tab body as well.

### Response

**Svetoslav Dimitrov** answered on 19 Mar 2020

Hello David, The CSS selector is.k-tabstrip>.k-content and to it you can change the background color. Regards, Svetoslav Dimitrov
