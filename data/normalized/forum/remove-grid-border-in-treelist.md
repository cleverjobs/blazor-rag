# Remove grid border in TreeList

## Question

**Han** asked on 03 Nov 2022

Hi, I would like to remove the border that you can see in each row of a TreeList. I can only change the background color with CSS but not the border. About 1 pixel high, colored gray, below and above each row.

## Answer

**Dimo** answered on 08 Nov 2022

Hello Hans, The general approach is to use the browser's DOM inspector to see how the existing styles are applied. This will hint you how to override them with higher specificity. Borders can be removed by setting the border-color to transparent or setting the border-width to 0. div.my-custom-treelist-class td { border-bottom-color: transparent;
} Regards, Dimo Progress Telerik
