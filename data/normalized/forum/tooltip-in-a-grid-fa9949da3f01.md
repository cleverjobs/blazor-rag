# Tooltip in a grid?

## Question

**Dou** asked on 28 Mar 2020

Does anyone have an example of how to use a tooltip in a grid? I would like to put a tooltip on a GridCommandButton but I can't seem to figure out how to do that.

## Answer

**Marin Bratanov** answered on 28 Mar 2020

Hello Doug, The following example shows how you can add tooltips to grid elements and even do load on demand for their rich content: [https://github.com/telerik/blazor-ui/tree/master/tooltip/in-grid.](https://github.com/telerik/blazor-ui/tree/master/tooltip/in-grid.) As for a simple title attribute on the command button - you can Follow its implementation here: [https://feedback.telerik.com/blazor/1457593-title-parameter-for-gridcommandbutton](https://feedback.telerik.com/blazor/1457593-title-parameter-for-gridcommandbutton) (I have added your Vote for it to raise its priority). If tooltips are highly important to your case, you could use your own buttons that have titles in a "regular" column and invoke editing through the grid state: [https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.](https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.) Regards, Marin Bratanov
