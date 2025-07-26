# TabStrip: Expand Element inside as Tab to the size of the Tab

## Question

**Hen** asked on 28 Jun 2024

What is the best way to resize a div within a TabStripPage to the size of the tab ? I am still struggeling with css...

## Answer

**Dimo** answered on 02 Jul 2024

Hello Hendrik, Normally, you only need a height for the TabStrip and a 100% height for the <div> inside the TabStrip, as in the snippet below. If you want the TabStrip to also expand, then you may need more styles on the TabStrip ancestors. If your scenario is more complex, please provide a demo. <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTab" Height="600px"> <TabStripTab Title="Tab 1"> <div style="height:100%;background:#ffc;"> This DIV will expand to fill the TabStrip </div> </TabStripTab> <TabStripTab Title="Tab 2"> Content 2 </TabStripTab> <TabStripTab Title="Tab 3"> Content 3 </TabStripTab> </TelerikTabStrip>

@code {
private int ActiveTab { get; set; }
} Regards, Dimo Progress Telerik
