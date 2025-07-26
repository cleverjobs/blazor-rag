# Truncating Text in a Column not working

## Question

**Hen** asked on 14 Feb 2023

I would like to Tail-Truncate the Text in a Column to prevent having multiple lines in a row. I tried the sample: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-rows-text-ellipsis](https://docs.telerik.com/blazor-ui/knowledge-base/grid-rows-text-ellipsis) But even the sample is not working. How is this fixed ?

### Response

**Hendrik** commented on 14 Feb 2023

I figured out myself. This styling works as expected: .custom-ellipsis { overflow: hidden !important; max-height: 60px; text-overflow: ellipsis; white-space: nowrap !important; }

### Response

**Yanislav** commented on 17 Feb 2023

Hello Hendrik, Thank you for sharing your solution with the community, which will benefit others. Your contribution is appreciated.

## Answer

**Svetoslav Dimitrov** answered on 17 Feb 2023

Hi, Regards, Svetoslav Dimitrov
