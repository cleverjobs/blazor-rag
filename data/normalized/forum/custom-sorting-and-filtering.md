# Custom Sorting and Filtering

## Question

**Mar** asked on 05 Feb 2020

I Display without issues complex types in the grid control, the ToString method is used to display the row value for that column and it's fine. However I can't figure out how to customize sorting and filtering, is there a way to provide a method to compare, sort, and filter columns with complex types?

## Answer

**Marin Bratanov** answered on 05 Feb 2020

Hello Marco, You can use the OnRead event to get the grid state, loop through it and implement the operations: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations) You can also Follow this page on getting built-in support for nested models: [https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models](https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models) Regards, Marin Bratanov
