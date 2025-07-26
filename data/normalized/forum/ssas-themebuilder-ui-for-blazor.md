# SSAS ThemeBuilder UI for Blazor

## Question

**Con** asked on 17 Sep 2021

I have created a custom theme with themebuilder but the result css is missing components like StackLayout and GridLayout. Why is that? Shouldn't the ThemeBuilder utility reflect the changed of the latest blazor components or should we do the process manually as described in Manual Alternative page?

## Answer

**Ivan Zhekov** answered on 21 Sep 2021

Hi, Constantinos. The short answer is that when you choose components in themebuilder, only those components get styled, which may not be the scenario you always want... As you can attest, there are some limitations to that approach, like certain styles for non visual components missing, and we will fix this issue in further iterations and following updates. For now, if you want to customize the theme, you can do so, but you should not deselect components, which in turn will download the entire theme. Regards, Ivan Zhekov

### Response

**Constantinos Petridis** commented on 21 Sep 2021

I have tried that and the downloaded theme is still missing styles, like GridLayout or StackLayout (no mention of .k-grid-layout in downloaded css file). I have not selected or deselected any components, just pressed Start Theming (in [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui) ) Scroll down the page and press Create Press Download button resulting zip file contains a css file that is missing GridLayout and StackLayout styles (not sure if other styles are missing too) I will try the manual SSAS custom theme creation until the theme builder is changed/updated Thank you for your time :)

### Response

**Ivan Zhekov** commented on 22 Sep 2021

Those are not yet present in themebuilder. They will be, once we update themebuilder post 2021 R3. That update should happen in the following days. Regards, Ivan Zhekov Progress Telerik
