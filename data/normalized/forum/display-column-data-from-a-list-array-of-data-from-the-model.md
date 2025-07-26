# Display column data from a List/Array of data from the model

## Question

**Mik** asked on 26 Sep 2023

Hello, i was wondering if it is possible to bind and display data in a column from a List/Array of data like this: public record Item
{ public string Name { get; set; } public List<int> CostsAtMonths { get; set; }=new (); public int [] CostsAtMonths { get; set; }
} Then have it displayed in in a TreeList with a column for each month of the year, where each column points to an item of the list/place in an array like this:

## Answer

**Nadezhda Tacheva** answered on 28 Sep 2023

Hi Mikail, I already responded to your private ticket which is a duplicate of the current one. I am pasting my response here as well for visibility. Based on the screenshot, I personally think that a more suitable component for such a data visualization structure is the PivotGrid that we recently released: [https://demos.telerik.com/blazor-ui/pivotgrid/overview.](https://demos.telerik.com/blazor-ui/pivotgrid/overview.) This component is generally used to represent multidimensional data in a cross-tabular format. Plus, it also supports scrolling, sorting and filtering. Can you please revise it and let me know your thoughts? You can find the documentation here: [https://docs.telerik.com/blazor-ui/components/pivotgrid/overview.](https://docs.telerik.com/blazor-ui/components/pivotgrid/overview.) Please let me know if any questions appear while evaluating it. You can post your response in either the private ticket or this forum thread. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Hatef** answered on 29 Aug 2024

Has there been any update on the functionality of the grids? using the PivotGrids seems to be overkill for a simple use case like this

### Response

**Nadezhda Tacheva** commented on 03 Sep 2024

Hi Hatef, The Grid cannot automatically generate columns with such a model structure as it expects a different structure. However, it is still possible to achieve the desired behavior with the Grid by implementing a custom approach for generating the columns. A similar topic has been discussed in this forum thread: Data binding in Grid. You can use the information and the example listed there as a starting point.
