# Reliability of overriding kendo CSS classes

## Question

**Rya** asked on 26 Sep 2019

While I've been able to customize the Sass-based themes using variables ([https://docs.telerik.com/kendo-ui/styles-and-layout/sass-themes#using-variables),](https://docs.telerik.com/kendo-ui/styles-and-layout/sass-themes#using-variables),) there are some customizations I've only been able to do by modifying the Kendo css classes. For example, to remove the border from the grid pager, I had to override the .k-pager-wrap and .k-link classes: .k-pager-wrap { .k-link { border-style: none } } The alternative is to create custom css classes: <TelerikGrid Class="custom-class" /> However, I'd need to know the DOM structure to customize the pager element for that grid: .custom-class { .div[data-role="pager"] { border-style: none } } My question is, how reliable is it to customize Kendo css classes or DOM elements? Are there any guarantees that these css classes will not change and break our application with new Telerik releases? If this is not a reliable approach, what are your recommendations?

## Answer

**Marin Bratanov** answered on 27 Sep 2019

Hello Ryan, Such CSS overrides are the way to implement tweaks like that. Inspecting the DOM and the used classes/attributes/roles is the way to create overriding selectors with sufficient specificity. We try to change the HTML structure and the classes used as rarely as possible. The main types of classes (such as k-link, k-pager-wrap) are not something that is likely to change at all. Regards, Marin Bratanov

### Response

**Zhi Yuan** answered on 15 Jan 2021

Hello Marin, Can I know which is the preferred way of overriding CSS classes? I understand that in the upcoming release, all components will have a Class parameter. However, if overriding existing CSS classes gets the job done, in what scenarios then should we create custom classes? Thank you!

### Response

**Marin Bratanov** answered on 15 Jan 2021

Hi Zhi Yuan, Setting your own Class to a component makes sense when you want to target specific instances in your selectors - then you can cascade them through that class. If you only use classes that come in our rendering, you will target all instances of these selectors. Regards, Marin Bratanov
