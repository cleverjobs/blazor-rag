# Bind to nested indexed properties

## Question

**Cla** asked on 01 Mar 2023

I need to bind a complex object to telerik grid field, i read the article [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bind-navigation-property-complex-object](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bind-navigation-property-complex-object) but it not explain if i can bind an indexed property. For example i need this bind: <GridColumn Field="Property.NestedProperty[0].Value" /> but it seem not working. Can be binded indexed properties? Thanks

## Answer

**Tsvetomir** answered on 03 Mar 2023

Hi Claudio, In addition to the article that you have linked, you can find additional information on columns binding here: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes) Note that if your NestedProperty is a type of IDictionary, List, and Array, you might encounter an error and such a setup is not supported. I hope you find this helpful. Regards, Tsvetomir

### Response

**Claudio** commented on 03 Mar 2023

Thanks, i solved using a column template
