# Long list of tabs

## Question

**Tam** asked on 29 Apr 2020

Is there a way to handle the case of long list of tabs? When the window is too narrow and the tabs don't fit, the last tabs get cut off. <TelerikTabStrip> @foreach (var item in new[] {"First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"}) { <TabStripTab Title="@item"> @item tab content. </TabStripTab> } </TelerikTabStrip>

## Answer

**Svetoslav Dimitrov** answered on 04 May 2020

Hello Tamas, On our Feedback Portal there is an open Feature Request for Scrollable tabs in the Tabstrip. This is mainly for cases, like yours, where you can a lot of tabs and you don't want them to stretch the UI or get cut off the screen. In the thread there is an example on how to make one with CSS. You can see the Feature Request from this link: [https://feedback.telerik.com/blazor/1456564-scrollable-tabs.](https://feedback.telerik.com/blazor/1456564-scrollable-tabs.) You can Vote for it, to raise its popularity, and Follow to receive email notifications on status updates. If this Feature Request does not work for you, you can use media queries and set some rules for different browser widths. If you want to target the currently active tab you can use the.k-item.k-state-active CSS classes, otherwise the.k-item.k-state-default. Below I have made some sample CSS to style the tabs. <style> @@media only screen and ( min-width: 992px ) {.k-item.k-state-default { width: 70px; font-size: 14px; color: #656565;
}.k-item.k-state-active { font-weight: bold; width: 90px; font-size: 16px;
}
}

@@media only screen and ( min-width: 576px ) and ( max-width: 992px ) {.k-item.k-state-default { width: 50px; font-size: 10px; color: #656565;
}.k-item.k-state-active { font-weight: bold; width: 70px; font-size: 12px;
}
}

@@media only screen and ( min-width: 300px ) and ( max-width: 576px ) {.k-item.k-state-default { width: 30px; font-size: 8px; color: #656565;
}.k-item.k-state-active { font-weight: bold; width: 40px; font-size: 10px;
}
} </style> <TelerikTabStrip> @foreach (var item in new[] { "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth" })
{ <TabStripTab Title="@item"> @item tab content. </TabStripTab> } </TelerikTabStrip> Regards, Svetoslav Dimitrov
