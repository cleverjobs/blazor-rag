# Grid OnRowExpand blur all other rows, or otherwise focus on the selected row with details

## Question

**Ant** asked on 09 Nov 2021

Having sub-grids of related data is very useful, but the interface can be a bit busy (see attached pic). Perhaps a solution would be if all other rows are blurred or otherwise de-emphasised when the expand icon is clicked, using jQuery and CSS, or using the OnRowExpand event. I'm liking using less jQuery - so the OnRowExpand event is my preferred method; but how would I change the style of all the other rows? Perhaps a better solution is to change the css of the expanded row plus details row below? I don't see how that can be done except using jQuery.

## Answer

**Marin Bratanov** answered on 11 Nov 2021

Hi Antony, Perhaps you can collapse the other rows as shown here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-expand-only-current](https://docs.telerik.com/blazor-ui/knowledge-base/grid-expand-only-current) Another approach would be to show a detail window to have the user see a (modal) popup with the details rather than lots of content inline. A third approach would be to add some CSS rules that provide the desired behavior and appearance. You can cascade through the expanded hierarchy row class to highlight the current one and de-emphasize the others. Perhaps you can cascade this through a Class set on the grid only if there are expanded rows. Regards, Marin Bratanov Progress Telerik
