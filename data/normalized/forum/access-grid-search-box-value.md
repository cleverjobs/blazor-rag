# Access Grid "Search" box value

## Question

**Chr** asked on 02 Feb 2021

I'm working on a custom export of the grid data (mostly due to date formats.) I can get the filtered data using the code from here: [https://www.telerik.com/forums/export-telerik-ui-blazor-data-to-excel-pdf#gLpHjDCLDUmPjega_RAwPw](https://www.telerik.com/forums/export-telerik-ui-blazor-data-to-excel-pdf#gLpHjDCLDUmPjega_RAwPw) This works great for using the filter menu items. Adding a couple new lines of code, I can easily get the current sort as well. Is there anything exposed to let me get anything typed into the "Search" box which does the Contains on all the fields? It doesn't exist in the current FilterDescriptors and I didn't see another thing that would let me get that values and further filter the existing data with what is in that box. Thanks

## Answer

**Marin Bratanov** answered on 03 Feb 2021

Hi Chris, The following thread shows one way to get all the filter descriptors the grid will generate for you so you can use them later: [https://feedback.telerik.com/blazor/1495832-include-filter-descriptors-from-the-searchbox-in-the-state.](https://feedback.telerik.com/blazor/1495832-include-filter-descriptors-from-the-searchbox-in-the-state.) It also explains why this isn't in the grid state. I have also added your Vote on this feature and you can click the Follow button to get email status updates - it will expose the Value of the searchbox so you could make your own filters if you prefer: [https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically](https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically) Regards, Marin Bratanov

### Response

**Chris** answered on 03 Feb 2021

Great, thanks! I'll look into the link you provided. I solved it by creating my own custom search box so I know what was typed there, and used that to add a combinedfilter to the grid data. It's probably not as quick as the inbuilt one, but I'm only dealing with 3-500 records at a time, so it's fast enough for now. But would love to remove a bunch of custom code I wrote if it was built in!

### Response

**Marin Bratanov** answered on 03 Feb 2021

Hi Chris, You can get all the filter descriptors through the OnRead event and that lets you optimize the data queries too (see more here ). Regards, Marin Bratanov

### Response

**Chris** answered on 03 Feb 2021

I was playing around with the OnRead event, but when using paging/virtual scrolling, I was having all sorts of problems getting all the data for the excel export of all the data(which is the reason I needed this.) Being able to access the search box value would save me tons of code. Thanks

### Response

**Marin Bratanov** answered on 03 Feb 2021

You can Follow that here. While the request is for clearing the input I expect two-way binding to be exposed for it, as it makes full sense. You may also want to Follow this for OnRead with exports: [https://feedback.telerik.com/blazor/1469312-include-all-pages-in-excel-export-should-work-with-onread](https://feedback.telerik.com/blazor/1469312-include-all-pages-in-excel-export-should-work-with-onread) Regards, Marin Bratanov

### Response

**Michal** answered on 20 Jan 2023

Hello, starting with versin 4.0.0 when all filters in OnRead request starting as "CompositeFilterDescriptor", what is the proper way how to get value from grid search box, when GridFilterMode.FilterRow is used together with searchbox? In previous versions there was a little "hint" how to guess the value in OnRead like this: grid-OnRead(GridReadEventArgs args){ var searchboxvalue=SqlClass.GetRawFromSearchBox(args.Request.Filters)
} public static string GetRawFromSearchBox ( IList<IFilterDescriptor> request ) { var filter=request[ 0 ]; if (filter is FilterDescriptor)
{ return (filter as FilterDescriptor)?.Value?.ToString();
} else if (filter is CompositeFilterDescriptor)
{ return ((filter as CompositeFilterDescriptor).FilterDescriptors[ 0 ] as FilterDescriptor)?.Value?.ToString();
}
} But what is the best guess in v4? - is the SearchBox value ALWAYS indicated as "OR" composite operator? - is the SearchBox value ALWAYS LAST in filters? - is there any other "tag" how to identify or get the value entered in searchbox? //this "should be" the girdsearchbox value var filter=request.FirstOrDefault(x=> x is CompositeFilterDescriptor && (x as CompositeFilterDescriptor).LogicalOperator==FilterCompositionLogicalOperator.Or); if (filter !=null )
{ return ((filter as CompositeFilterDescriptor).FilterDescriptors[ 0 ] as FilterDescriptor)?.Value?.ToString();
} I'd appreciate tips on how to get a single string value from a lookup field :)

### Response

**Hristian Stefanov** commented on 25 Jan 2023

Hi Michal, I copied the provided " GetRawFromSearchBox(...) " method and modified it a bit to work in the latest version (4.0). Please run and test this REPL sample to see the result. I left comments on the changed parts for better visibility. Let me know if I'm missing something. Now let me cover the remaining questions: " - is the SearchBox value ALWAYS indicated as "OR" composite operator? " The logical operator can be changed programmatically. Here is an example from our docs that shows one way to set it: Filter From Code. " - is the SearchBox value ALWAYS LAST in filters? " Yes, the SearchBox value is always last in the filters. You can use that to identify it.
