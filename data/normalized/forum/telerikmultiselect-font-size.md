# TelerikMultiSelect font size

## Question

**gfk** asked on 09 Feb 2022

Hello, I've just started using the TelerikMultiSelect for the first time and it's working well, except I can't change the font size of the list of selected items. I've applied Class="MyStyle" which defines a font-size value, but it has no effect. The attached image shows the selected items with font-size 14px that I can't override and they are smaller than the surrounding elements. Inspecting the source I can see a nest of k-xxx styles which I tried overriding as an experiment, but nothing has any effect. Thanks, Greg

## Answer

**Matthias** answered on 09 Feb 2022

Hi Greg, give this a try: .k-chip-label { font-size: 16px;
}.k-list-item { font-size: 16px;
} regards Matthias

### Response

**gfkeogh** commented on 09 Feb 2022

Sadly, those styles have no effect. I put them in the page's css file, then in the top of the page, then appended them in a style block to the app's index.html page, then nested them inside the component's Class=style, but there is change. Greg
