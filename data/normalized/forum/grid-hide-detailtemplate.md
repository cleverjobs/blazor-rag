# Grid: Hide DetailTemplate

## Question

**Hen** asked on 14 May 2023

I just discovered the DetailTemplate and it is great. But I build myself a genereric Grid-Control with the Tererik-Grid and I pass a RenderFragement from my Parent-Component to this Control. This works perfectly. But even if the RenderFragemt is Null, the "+" and "-" Buttons to expand and collaps the DetailTemplate are always shown. How can I hide them ? Unfortunately this is not working: @if (ChildContent !=null) <DetailTemplate> {
@ChildContent
} </DetailTemplate> }

## Answer

**Nadezhda Tacheva** answered on 17 May 2023

Hi Hendrik, You can handle the OnRowRender event of the Grid to evaluate whether the current row has children. Based on that, you can then apply a conditional CSS class to hide the expand icon for the specific row. You can find some more details and an example in this article: Conditionally Hide Hierarchical Grid Expand Button. I hope you will find that useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Hendrik** commented on 17 May 2023

Hello Nadeszhda, thank you very much for your time and effort. In your solution is just the icon conditionally hidden but the whole column still exists. I need to either show or hide the "Details"-Column. But I think, the way is not too far anymore....

### Response

**Nadezhda Tacheva** commented on 19 May 2023

Hi Hendrik, Indeed, the solution I shared is focused on hiding the expand icons for the Grid records that do not have children. Based on your additional description, I understand that you need to hide the whole column that contains these icons (I suppose this is for the generic purposes of the component). If so, you may check this article for more details and an example: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-toolbar-detail-template.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-toolbar-detail-template.) Testing the snippet from it on my end, it looks like both the Detail Template and the Details Column are successfully hidden. Take your time to revise and test the approach on your end and please let me know if you are still experiencing any issues. If so, please send an isolated runnable sample reproducing the behavior you are getting, so I can debug it and suggest how to move forward. Thank you in advance!

### Response

**Hendrik** commented on 19 May 2023

Hello Nadeszhda, thank you so much. That works perfectly and I learned some new tricks generally !
