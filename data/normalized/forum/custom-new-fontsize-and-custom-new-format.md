# custom new FontSize() and custom new Format()

## Question

**Rol** asked on 20 Jan 2022

There is an example of new ForeColor() { Colors=new List<string> { ... }} How do I get a similar customization for FontSize? For example, I only want large, x-large and xx-large I would expect something like new FontSize() { ???=new List<string> {xx-large", "x-large", "large" } } For ???, I tried FontSizes and Sizes, which did not work. I have the same question ref new Format(). For example, I only want p, h1, h2 and h3

## Answer

**Dimo** answered on 20 Jan 2022

Hello Rollie, Yes, there is a similar customization for the font dropdowns too. All these have a Data property that you can set: FontSize FontFamily Format For example new FontSize() { Data=new List<EditorDropDownListItem>() { new EditorDropDownListItem( "my large", "32px" ) } } Regards, Dimo
