# Is TreeList groupable?

## Question

**Bla** asked on 20 May 2021

Just that. Is there an "out of the box" grouping functionality in TreeList component?? If it is not possible, do you have any suggestions on how I can accomplish this? Regards,

## Answer

**Marin Bratanov** answered on 21 May 2021

Hi, The treelist is already a visualization of hierarchical data. This means that it is effectively grouped: Thus, if the user were able to drag columns to group, there would be quite strange results: grouping would appear very unexpected because there is already groups, nested data and expandable elements you could not have more than one level of grouping - only root nodes could potentially be grouped which is almost the same as filtering the data structure might have to change dramatically (which is unlikely to be possible) if the user tries to group by a field that is not the root field If you are looking to let the users choose how to group the data to see different hierarchies in it I recommend you consider the grid component that can already do that: [https://demos.telerik.com/blazor-ui/grid/grouping.](https://demos.telerik.com/blazor-ui/grid/grouping.) You can even use its state to set grouping from code. Regards, Marin Bratanov Progress Telerik

### Response

**Blazorist** answered on 21 May 2021

I was evaluating the Grid and TreeList components. I'm going to have to use the grid since I need more than one level of grouping. Thank you very much for your answer. Blazorist.
