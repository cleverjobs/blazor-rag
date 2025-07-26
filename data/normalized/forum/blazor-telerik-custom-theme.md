# blazor telerik custom theme

## Question

**kha** asked on 16 Oct 2019

hi, i was wondering to know if there is a way to give custom style to each telerik component individually i have already tried using class and id but some of components do not accept class or id i also tried this [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui) but unfortunately there is a very big problem with colors and sometimes they don't match and will result in an awkward component which most parts has same color

## Answer

**Marin Bratanov** answered on 17 Oct 2019

Hello, The concept of our themes is that components always match each other, and to that end the themes use shared "components" that have the same classes and styling - for example headers, titlebars, buttons, etc. The theme builder operates by using a few base variables and extracts further colors from them. It is up to you to choose the initial colors and you can preview the results on the right hand side. You can then manually tweak things for better precision. If you want to implement tweaks per control, you can inspect the rendered HTML and see the available classes. Usually the component wrapping element has a class like k-treeview (for the treeview, for example) that you can cascade through. Most components have a Class attribute and if some doesn't, you can always cascade through a parent class from your layout. If you start implementing CSS overrides per component, you may find the following useful: general guidance on how to use the browser dev tools to do that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools) the following feature request: [https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance) Regards, Marin Bratanov

### Response

**khashayar** answered on 17 Oct 2019

thank you for your answer but i wanna know if inspecting an element to copy and use its class in code is a correct way or not i have always felt this is an awkward way to style an element

### Response

**Marin Bratanov** answered on 17 Oct 2019

Hi, Inspecting the elements and creating CSS rules that override our built-in appearance is the correct approach for small tweaks or per-instance alterations. For changing the overall look of all the components, I recommend creating a custom theme. You can still add tweaks to it. Regards, Marin Bratanov
