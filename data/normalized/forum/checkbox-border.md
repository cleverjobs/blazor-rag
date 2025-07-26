# Checkbox border

## Question

**Dou** asked on 11 Oct 2024

Whenever I add a TelerkiCheckBox to a page/component the testers complain that they can't see the border of the checkbox so I'm constantly adding the below css to my razor files: <style> .k-checkbox { /* Make the border a little darker than the default */ border-color: rgba(0, 0, 0, 0.4); } </style> If I add this to my app.css it doesn't get applied. Is there any way to apply this at a global level?

## Answer

**Dimo** answered on 15 Oct 2024

Hi Doug, In this case there are two concepts, which come into play: CSS Cascade (the origin of the CSS rules, which is their placement) CSS Specificity (the relevance of the CSS rules, which is the number of selectors ) Your CSS rule has the same specificity as ours - 1 CSS class (.k-checkbox ). So, the precedence depends only on the cascade. <style> tags take precedence over <link> tags. If you move your rule in a CSS file, then the order of the two <link> tags starts to matter. So the solution is to do one or both of the following: Reorder the <link> tags, so that app.css comes after our theme Add more selectors to your rule, for example input.k-checkbox or.k-checkbox-wrap .k-checkbox, etc. In such cases it is important to work with the browser's developer console in order to: See our theme rules. Come up with optimal combinator for the custom CSS rule. Verify or troubleshoot the outcome. Regards, Dimo Progress Telerik

### Response

**Doug** commented on 15 Oct 2024

Well I do admit to not being a css expert (one of the many reasons to use the Telerik controls). Thank you for educating me.
