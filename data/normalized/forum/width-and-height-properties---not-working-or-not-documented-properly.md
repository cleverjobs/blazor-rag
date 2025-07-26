# Width and Height properties - not working or not documented properly

## Question

**And** asked on 28 May 2019

Regarding [https://docs.telerik.com/blazor-ui/common-features/dimensions](https://docs.telerik.com/blazor-ui/common-features/dimensions) in server-side Blazor. "dimensions and positions are simple string properties that are not parsed by our code. You can provide valid CSS values to them. For example, 100px or 50%are valid options" However when I use: Height="100px" or Height="100%" in many controls, including TelerikWindow and TelerikGrid, I get compile errors: The name 'px' does not exist in the current context and Invalid expression term ')' If I just use Height="100" then the Blazor app runs although I am still not sure the Height property is working properly. Can you please confirm how this is supposed to work?

## Answer

**Marin Bratanov** answered on 28 May 2019

Hello Andrew, Judging from your other thread, your project is still on the old 0.5.0 version that does not support this improvement. Please upgrade to 1.1.0 which is the current latest and is in the public docs (they are always about the latest official release). Regards, Marin Bratanov
