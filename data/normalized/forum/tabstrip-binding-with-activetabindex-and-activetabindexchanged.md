# TabStrip binding with ActiveTabIndex and ActiveTabIndexChanged

## Question

**Cla** asked on 14 Nov 2022

I need to set active tab from code and handle tab changed from user interaction, so i use the ActiveTabIndex property and the ActiveTabIndexChanged event, but this prevent tab to be changed from gui. The issue can be replied with this code: <TelerikTabStrip ActiveTabIndex="ActiveTabIndex" ActiveTabIndexChanged="ActiveTabIndexChanged"> <TabStripTab Title="Tab1"> <Content> 1 </Content> </TabStripTab> <TabStripTab Title="Tab2"> <Content> 2 </Content> </TabStripTab> </TelerikTabStrip> @code { private int ActiveTabIndex {get;set;} private void ActiveTabIndexChanged(int tabIndex) { } } what's wrong? Thanks

## Answer

**Dimo** answered on 16 Nov 2022

Execute ActiveTabIndex=tabIndex in the handler, otherwise the user action is ignored. This applies to all [Parameter] Changed handlers.
