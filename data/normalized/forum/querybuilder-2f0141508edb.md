# QueryBuilder

## Question

**mic** asked on 16 Dec 2020

Do you have or planned to add a QueryBuilder component similar to the one that Syncfusion have? [https://www.syncfusion.com/blazor-components/blazor-query-builder](https://www.syncfusion.com/blazor-components/blazor-query-builder)

## Answer

**Marin Bratanov** answered on 16 Dec 2020

Hello Michael, You can Follow its implementation here: [https://feedback.telerik.com/blazor/1445600-filter-component.](https://feedback.telerik.com/blazor/1445600-filter-component.) I've added your Vote for it to raise its priority. Considering we do native blazor components, this will most likely output C# objects (our DataSourceRequest so you can use its with ToDataSourceResult, see here ) which you could serialize as needed over the wire too, instead of json. Regards, Marin Bratanov
