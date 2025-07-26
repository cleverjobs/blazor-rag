# How to create/download CSS files for new Blazor themes in 2.27?

## Question

**JoeJoe** asked on 15 Sep 2021

Hello, Thus far, I have only been able to use 3 themes: Default, Bootstrap, and Material. I see in the Demos that now there are various themes/swatches available. Can anyone advise the exact steps I need to take in order to create/download CSS files corresponding to each of these new themes? The application I'm currently working on allows users to select from the 3 standard themes, and so I have a CSS file corresponding to each of them that gets swapped out in the DOM dynamically. I'd like to use the same mechanism to allow users to select any of the new themes/swatches, and therefore I would need to have a separate CSS file for each. Thanks.

## Answer

**Nadezhda Tacheva** answered on 20 Sep 2021

Hi Joe, The built-in themes (Default, Bootstrap, and Material) provide various swatches that let you alter the default appearance of the Telerik components so they match the desired color scheme from your designers and fit with the rest of your site's coloring and style. As of version 2.27 we have included some of the swatches in our live demos. All the available swatches you can explore in the Sass Theme Builder for Blazor. In this article you can find details on how to work with the Theme Builder and the exact steps to include the custom theme in your application. I hope you will find the above information useful. If any further questions appear, please let us know, we will be happy to step in assist. Regards, Nadezhda Tacheva
