# Menu not listed in Blazor theme builder?

## Question

**Bit** asked on 24 Oct 2019

I don't see it listed in the Blazor themebuilder, am I missing something? [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui)

## Answer

**BitShift** answered on 24 Oct 2019

How can I override the the colors of the bootstrap styles for the menu component, regarding the background color?

### Response

**BitShift** answered on 24 Oct 2019

looking at a dev console, its the .k-menu:not(.k-context-menu) style that is what I want to change. By default, with the bootstrap theme, it is background: #f8f9fa; but I want #ffffff

### Response

**BitShift** answered on 24 Oct 2019

Only way I can seem to do it now, is to override this value in my own css file eg. .k-menu:not(.k-context-menu) {<br> background-color:#ffffff;<br>}

### Response

**Marin Bratanov** answered on 25 Oct 2019

Hello, We are working on adding an example of the menu in the theme builder. It will be available as soon as possible. The general concept of themes is that all components follow the same theme (that is, color scheme), so changing the colors once styles all components without extra effort. If you want to alter a single component only, the correct way is, as you have found, to inspect the rendered HTML, review the current classes, structure and CSS rules, and to devise your own that override the built-in ones. You need to create an entire theme if you want to affect all (or most) components. For example, if you want to change the main background of the main element, here's how you could do this - this example showcases targeting a particular instance through a specific class as well <style>.specialMenu.k-menu:not(.k-context-menu) { background-color:red;
}
</style>

<TelerikMenu Data="@MenuItems ">
</TelerikMenu>
<div class="specialMenu">
<TelerikMenu Data="@MenuItems">
</TelerikMenu>
</div> Regards, Marin Bratanov

### Response

**JeffVisibilEDI** answered on 03 Nov 2021

I am a Bootstrap & MVC5 user that has recently begun working with Blazor. Our company has an MVC5-based application that uses a host of Telerik controls. These were developed by a contractor who no longer works with us. Whenever I search for demos, help, etc., for Blazor elements, Telerik pages are the first hits that come up. We have purchased a developer license so I can use the Telerik Blazor toolset for new development projects, as well as to update portions of the legacy app. I have created a color scheme based on our marketing materials and incorporated them into a Bootstrap-based theme using SCSS. The first building block of any GUI I create is to create a skeleton NavBar. There do not seem to be ways to use classes to elements in order to apply theme colors. I am looking for a way to add classes like "navbar navbar-expand-lg navbar-light bg-primary" to the navbar/menu element in order to use the theme's "primary" color. I am looking for a way to apply theme colors to a menu through SCSS.

### Response

**Marin Bratanov** commented on 04 Nov 2021

Jeff, the Telerik Theme targets only Telerik components on the page and does not aim to be another Bootstrap or similar site-wide styling solution. In fact, we take deliberate care to style only our own components and elements and not to pollute the rest of the page. If you want to use the same colors, I can suggest you use them in your own build process (e.g., customize bootstrap with the same color variables).

### Response

**JeffVisibilEDI** commented on 04 Nov 2021

Hi, Marin. I am not looking to apply bootstrap styles to any Telerik objects. The telerik website suggests that there are themes within the Blazor libraries that use or mimic bootstrap's color pallette of Primary, Secondary, Info, Success, etc. I created the Sass files to support such a theme, but I do not see any to apply thene colors to the Menu object. The only suggestions I found were to create css rules that force the background-color of the menu. This does not allow use of an scss variable to identify the color to be used. I would like to know if there's a pre-built theme that can used to customize all of the widgets in the Blazor toolset. I would also like to customize the color olir palette of that theme to match marketing materials of our company as well as our partners, for whom we rebrand our site with a number of color pallette themes. Thanks!

### Response

**Marin Bratanov** commented on 06 Nov 2021

We do not maintain public "API" (that is, classes, variables) for customizing such states through ready-made changes. Such specific customizations need to be done in the project (where you can also use sass, and variables you use in the Theme Builder app). I recommend you review the following resources to see how customizing themes works: [https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme](https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme) [https://docs.telerik.com/blazor-ui/styling-and-themes/theme-swatches](https://docs.telerik.com/blazor-ui/styling-and-themes/theme-swatches) [https://docs.telerik.com/blazor-ui/styling-and-themes/figma-ui-kits](https://docs.telerik.com/blazor-ui/styling-and-themes/figma-ui-kits) In the fist article, there is a section about modifying the theme source and building them from that source. This is perhaps the way you may want to consider if you do not want to use a separate stylesheet. Inspecting the source and the component rendering (with the browser tools) will let you see what is used, so you can see what rules you need to create. So, yes, you can use pre-made themes and swatches we have, and they will customize all Telerik components, and you can easily do so with a desired color palette (based on the exposed variables and options in the base theme of choice). The changes, however, depend on how themes are implemented and in case they do not change the exact elements you want, you will need to add your own stylesheet and rules to achieve the desired effect.

### Response

**JeffVisibilEDI** commented on 08 Nov 2021

Hi, Marin. I have reviewed these pages several times and have created a custom (Bootstrap-based) theme that has assigned the Bootstrap color names to hex codes of colors that appear in our company's marketing materials. My custom theme's css files contain no rules that can apply any styling to the Telerik Menu component. All of the other libraries I have ever used have provided css classes to apply theming to every element they can create. I am not a SASS or CSS expert. I asked my employer to purshase a Telerik developer's license in part because I understood that it would provide me with easy-to-apply (and create) methods to quickly develop Blazor content that uses consistent thematic styling. This conversation is hijacking a 2-year old thread - but I am obviously very disappointed in my initial results.

### Response

**Marin Bratanov** commented on 08 Nov 2021

Jeff, we have many customers who customize our theme to use their brand colors. Our HTML rendering also uses many classes you can cascade through to add custom touches in case a quick color customization does not change all you want it to change. If that does not work for you as expected, I suspect there is more at play than I am seeing here, and I recommend you open a private support ticket so you can describe the issue(s) and situation you have in detail. This will also let you provide more details than in a public thread, and will also come with the guaranteed response time from your license (24h for your current license).
