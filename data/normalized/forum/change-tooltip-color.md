# Change Tooltip color ?

## Question

**Rih** asked on 08 Jun 2020

Hello, I would like to change the color of my tooltip, and also of my buttons, as I understood, the whole UI is set with a single base Theme (Bootstrap or else). The problem is that the tooltip with bootstrap is blue, and if I add it on a primary button, it's blue on blue and not readable. An attribute letting us to set the Color of a tooltip or a button would be good. I can't but red warning buttons for example. I tried to set the class of a tooltip with a different background color, but only the rectangle is set not the whole tooltip (see pic). Thanks in advance

## Answer

**Marin Bratanov** answered on 08 Jun 2020

Hi, An alternative is to style the buttons explicitly: [https://docs.telerik.com/blazor-ui/components/button/overview#styling](https://docs.telerik.com/blazor-ui/components/button/overview#styling) You can also style the tooltips by inspecting their rendering and overriding rules from our classes. This blog post can help you do that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) Here's an example I made for you: <style>.k-tooltip { background-color: red;
} div.k-tooltip.k-callout { color: red;
} </style>

<TelerikButton Title=" the button title "> lorem ipsum </TelerikButton>

<TelerikTooltip TargetSelector=" p a [title],.k-button ">
</TelerikTooltip>

<p>
<a title=" what is ' lorem ipsum '?" href=" https:// lipsum.com /"> lorem </a> ipsum dolor <a title=" is this a real word?" href=" https:// en.wikipedia.org / wiki / SIT "> sit </a> amet.
</p> Regards, Marin Bratanov
