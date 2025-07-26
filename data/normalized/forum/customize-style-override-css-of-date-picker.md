# Customize Style / override CSS of date picker

## Question

**Rob** asked on 06 Nov 2019

Hi, we are evaluating the Blazor UI components. We didn't find any informations about overriding CSS. Is this possible at all on all components and specially on the datepicker? Greetings, Robert

## Answer

**Marin Bratanov** answered on 06 Nov 2019

Hello Robert, There are two general ways to change the appearance of a component: create a custom theme for all components: [https://docs.telerik.com/blazor-ui/themes/custom-theme](https://docs.telerik.com/blazor-ui/themes/custom-theme) inspect the rendered HTML to see the current classes and rules, and devise rules of your own that will produce the required effect. This blog post can help you in that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) If you want to target a specific instance and wrapping it in a div with a particular class/id does not suffice for you, you may want to vote for this feature: [https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.) For the time being you can use the ".k-calendar" and ".k-datepicker" classes as root selectors for, respectively the calendar (both the popup one in the pickers, and the standalone one) and for the main input+button. Regards, Marin Bratanov
