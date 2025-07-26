# font awesome integration

## Question

**n/an/a** asked on 09 Mar 2022

Hello Could Font Awesome be used with Telerik Blazor? And if so, how do I integrate and use it into the project? Thank you. Kind regards

## Answer

**Dimo** answered on 11 Oct 2023

As of UI for Blazor 4.x, use FontAwesome with the Icon parameter of our components like this: <TelerikButton Icon=" @(" fa-solid fa-code ") " /> The main question is "how to set custom CSS classes" for icons and our documentation shows this: Button Icons Menu Icons TreeView Icons You can find similar articles for other components

### Response

**evadyyc** commented on 11 Oct 2023

Yes thank you... To be more clear it would be nice if you had a template/file (or even just a checkbox in themebuilder) to use that would replace all the button icons with fontawesome version also giving us strongly typed use of all their icons instead of just using strings. Recalling the challenge with FontAwesomes' last upgrade where fas -> fa-solid and bar-chart -> chart-bar. If we had ButtonIcons.BarChart it would be an easy change

### Response

**Doug** commented on 17 Oct 2023

In the links above (Button, Menu, TreeView) the FontIcons don't work. I changed my code to use Svg which works but I found this after reading the upgrade notes for 4.0, and the FontIcons change didn't work in my code.

### Response

**Dimo** commented on 18 Oct 2023

@Doug - since version 4.6.0 you need one more CSS file to use font icons. We haven't added it to the REPL tool by default yet. Sorry about the confusion.

### Response

**Marin Bratanov** answered on 12 Mar 2022

Hello, You can use the IconClass to set the desired custom classes from a third party solution, provided they set icon glyphs in the ::before element. You can find examples and more information here: [https://docs.telerik.com/blazor-ui/common-features/font-icons.](https://docs.telerik.com/blazor-ui/common-features/font-icons.) The same pattern that you see described there for the standalone icon component applies to all places we have icons. Also, you can add custom classes like that to add more CSS overrides as necessary to put in third party icons. Lastly, various templates likely let you replace some of the built-in rendering with custom code so that you can employ any approach you need/want. Regards, Marin Bratanov

### Response

**evadyyc** commented on 10 Oct 2023

As FontAwesome is such a popular icon class... a specific code sample on this would be very helpful!
