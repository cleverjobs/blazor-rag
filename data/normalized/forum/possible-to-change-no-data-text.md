# Possible to change "No data" text?

## Question

**And** asked on 23 Jul 2020

I did a bit of searching and couldn't find this in the documentation. Is there a way to change the text in the ComboBox dropdown when there is no data in the source collection? Thanks, Andrew

## Answer

**Marin Bratanov** answered on 23 Jul 2020

Hello Andrew, You can change it for all combo boxes through localization. You can see this in action here: [https://demos.telerik.com/blazor-ui/combobox/localization](https://demos.telerik.com/blazor-ui/combobox/localization) - just type some gibberish in the input so the filtering shows no results, then change the language and repeat. That said, I can understand how making this customizable per component instance could be useful, so I made the following enhancement idea page in our portal where you can track the implementation of a no-data template so you can put your own content there instead: [https://feedback.telerik.com/blazor/1477531-no-data-template-in-the-combobox.](https://feedback.telerik.com/blazor/1477531-no-data-template-in-the-combobox.) Regards, Marin Bratanov
