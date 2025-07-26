# Grid filter - checkboxes

## Question

**Kon** asked on 01 Jul 2021

Hi, I have some questions related to the new filter type in Grid - checkboxes 1. Is it possible to format decimal values in filter window? Attributes related to currency format like Display... do not work here. I have still values like 123.0000000000 in checkboxes filter window 2. Is it possible to format date values in filter window? I have dates in filter window with different format than in Grid. 3. Is it possible to sort values in filter window? I mean default behaviour/sorting (without writing templates for every column). Thanks!

## Answer

**Marin Bratanov** answered on 03 Jul 2021

Hi Kondar, By default, the grid uses the basic string representation of the data, so the formats come from the framework based on the data type. The Custom Data section of the documentation shows how you can put custom data there to control order and appearance: [https://docs.telerik.com/blazor-ui/components/grid/filter/checkboxlist#custom-data.](https://docs.telerik.com/blazor-ui/components/grid/filter/checkboxlist#custom-data.) If that is not sufficient for your needs, I suggest you create a FilterMenuTemplate with the desired behavior: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-menu-template.](https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-menu-template.) Regards, Marin Bratanov Progress Telerik
