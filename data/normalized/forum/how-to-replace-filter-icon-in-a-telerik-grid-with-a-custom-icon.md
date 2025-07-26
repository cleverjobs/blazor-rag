# How to replace Filter Icon in a Telerik Grid with a custom Icon

## Question

**Pra** asked on 11 Jul 2024

Hi team, We are currently using Telerik grids for our data, with fluent theme. We were able to change most of the css for that grid, as per our requirement. However, we were unable to replace the filter-icon.svg with ours. I looked into other posts in this forum, and in one post from 2020 they suggested changing the css or going through the template. But we were unable to replicate the work. Is there any direct implementation now, to replace these icons or any other workaround ?

### Response

**Mark** commented on 12 Jul 2024

I also can't replace the filter-icon.svg in Telerik's Fluent theme. Any help here?

## Answer

**Nadezhda Tacheva** answered on 15 Jul 2024

Hello Mark, The Grid currently does not provide an option to change the built-in filter icon. We are considering adding such an option for the whole suite in future. You may vote for the item here and follow it to get status updates: Ability to change the built-in icons. For the time being, I can suggest two options: Use CSS You can target the filter icon and use custom CSS to change the path of the SVG element similar to the example here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-expand-collapse-icons.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-expand-collapse-icons.) Create custom filter button Hide the built-in filter button and use a template to add your custom button, so you can specify the desired icon to use in it. The configuration will vary depending on the filter mode: For FilterRow - set ShowFilterCellButtons to false to hide the default buttons and use Filter Row Template to add the desired input and custom filter button. For FilterMenu - the default filter menu can be triggered just by the default filter button so you may choose a different approach here. Disable the default filtering and implement an approach for filtering from code through the state. In the Header Template you may add a custom button for toggling a custom filter menu. For the menu itself you may use the Popup component. You may also create a reusable dropdown for the filter operators as shown here: Use FilterOperator Drop-Down in Filter Template. Regards, Nadezhda Tacheva Progress Telerik
