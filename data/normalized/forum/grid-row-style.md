# Grid row style

## Question

**Rob** asked on 28 Nov 2019

How to apply style to a row (for example background color) inside a Grid? I've tried RowTemplate but the contents of a RowTemplate must be <td> elemets. If I wrap <td> elements inside a <div> the layout breaks.

## Answer

**Marin Bratanov** answered on 29 Nov 2019

Hello Robert, Adding the desired classes and rules to the td elements is the way to go. Here's one example that we have in a KB article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background.) If you don't need the rows colors to be dependent on the row data, you can simply inspect the classes and rules we have out-of-the-box, and add heavier selectors with the rules you want. This blog post can help you in doing that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) Regards, Marin Bratanov
