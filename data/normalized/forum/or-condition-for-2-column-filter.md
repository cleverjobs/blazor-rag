# OR condition for 2 column filter

## Question

**Kev** asked on 19 Nov 2020

Can you apply an OR condition on 2 column filters, or programmatically set the filter value for the GridSearchBox ?

## Answer

**Nadezhda Tacheva** answered on 24 Nov 2020

Hello Kevin, Please see the comments on your questions as follows: Applying "OR" condition on 2 or more columns The default behavior of column filters must be AND because this is what people expect. You can, hovewer, customize that by using the OnRead event the grid exposes - it provides you with all the filter descriptors and that lets you implement the actual filtering in your real data source in any way you prefer - either through custom application code, or you could loop the filters and create one composite filter with all of them that has the OR logical operator, instead of having a series of separate filters that our logic will apply the AND operator to. The following article explains how the OnRead event works and offers some examples that you can use as base to review the functionality and build what you need: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) Generally, this is the event where you can customize any of the grid read operations and implement your own logic. Programmatically set the filter value for the GridSearchBox We already have an enhancement request concerning the ability to get and set the Searchbox value programmatically. With that, you would be able to save the user input from it, and apply it after loading the grid. In case you find it interesting and something that you might want to go for, you can Follow it here - [https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically](https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically) - and I've already added your Vote to it to raise its priority. Regards, Nadezhda
