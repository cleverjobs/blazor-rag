# Custom Filter Row Template: FilterDescriptorCollection keeps only one FilterDescriptor

## Question

**Ray** asked on 01 Feb 2022

Hi, In reference to the "Custom Filter Row Template" example ( [https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template](https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template) ) I've found following issue: Every time when the function "SetupFilterRule()" is called the FilterDescriptorCollections contains only "theFilterContext.FilterDescriptor.FilterDescriptors[0]". Even when "filter2" is added to the collection... the next time the function is called the collection contains only filter1. Is there any way to keep added filters in the collection? Best regards, Rayko

## Answer

**Hristian Stefanov** answered on 04 Feb 2022

Hi Rayko, This can be indeed problematic behavior in some scenarios. That being said, we have a public item planned for a fix on our Public Feedback Portal regarding the problem: Custom Filter Row Template not updated by setting the Grid State You can subscribe to the above item to receive email notifications for status updates. Please keep an eye there for further updates. Regards, Hristian Stefanov
