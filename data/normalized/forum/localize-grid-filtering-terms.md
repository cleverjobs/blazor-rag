# localize grid filtering terms

## Question

**Jos** asked on 19 Sep 2022

Hi, I want to localize "filter", "search","select all" and clear inside grid filtering. I have found this example, but this is intended more to create your own personalized filter. [https://demos.telerik.com/blazor-ui/grid/overview](https://demos.telerik.com/blazor-ui/grid/overview) Is it possible to just modify those elements?

## Answer

**Stamo Gochev** answered on 22 Sep 2022

Hello Jose, You can have a look at the documentation article about Localization, which provides information about how to use the .resx localization files to customize the text of various parts of the components. Judging from the screenshot, it looks like you are interested in using other messages for the CheckBoxList filter and the localization message keys that correspond to the mentioned elements are: "Filter_Filter" - for the header text (default value "Filter") "Filter_Search" - for the text of the search box (default value "Search") "Filter_SelectAll" - for the select all option (default value "Select all") "Filter_Clear" - for the clear button "Filter_Filter" - for the filter button Regards, Stamo Gochev Progress Telerik
