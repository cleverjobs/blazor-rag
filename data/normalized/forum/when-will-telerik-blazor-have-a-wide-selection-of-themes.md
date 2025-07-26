# When will Telerik Blazor have a wide selection of themes?

## Question

**JoeJoe** asked on 27 Jul 2021

Hello, I was wondering if/when you will offer a larger selection of themes for your Blazor components? Other vendors, e.g. DevExpress, have large theme selections, as seen here [https://demos.devexpress.com/blazor/GridColumnTypes](https://demos.devexpress.com/blazor/GridColumnTypes) Right
now, you only have three, which are very similar to one another. Users
commonly want to have a dark theme, for example, and you don't offer
any. Please advise. Thank you.

## Answer

**Matthias** answered on 27 Jul 2021

Hi Joe, With ThemeBuilder you have a great tool to use the themes and colors you need. By the way, I could mix this even with DevExpress. Best Regards Matthias

### Response

**Joe** commented on 27 Jul 2021

Hi Matthias, I did see ThemeBuilder, but I'm really looking for a selection of pre-built themes to choose from. Is there any kind of repository you're aware of?

### Response

**Matthias** commented on 27 Jul 2021

No, I use ThemeBuilder and have implemented a "theme switcher" for it. For this I use some variables for color, font etc.. Because I currently have to use other components, the base is bootstrap. What are you missing in ThemeBuilder?

### Response

**Joe** commented on 27 Jul 2021

It just looks way too time-consuming. I'd also like the flexibility of being able to easily integrate something like Bootswatch, e.g. [https://bootswatch.com/sketchy/.](https://bootswatch.com/sketchy/.) Do you know how this can be accomplished?

### Response

**Matthias** commented on 27 Jul 2021

Haha. Yes "Sketchy" is quite funny. But inappropriate for my customers or users. That's why I didn't investigate further. But "dark mode" etc., ultimately only need different colors and fonts. The effort for this is not really high and I'm pretty happy with ThemeBuilder. But I think it is quite possible to use "Sketchy". Greetings from Berlin Matthias

### Response

**Joe** commented on 27 Jul 2021

Yes, I wouldn't think to use Sketchy in one of my apps either, lol, but they do have other professional looking ones.

### Response

**Matthias** commented on 27 Jul 2021

a few months ago, Telerik had similar names for themes based on Bootstrap. For example, Flatly, as far as I remember. However, I may have a different goal. Colors are important to some of my users. Some can't or don't want to work with "dark mode", others actually want green or purple. Otherwise, I want my application to always have the same look. So no switching from flat to 3D. In other words, overall a more subtle layout that is not distracting. But as I said, it depends on the application.

### Response

**Joana** commented on 30 Jul 2021

Hey all, In the ThemeBuilder you could find all available swatches for every theme. Basically, the swatches offer different palettes/color variations of the themes. [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui) In addition, all Telerik themes are placed in kendo-themes repository and you could compile any existing swatches through `npm run sass:swatches` command. We invested time in synchronizing the ThemeBuilder and kendo-themes swatches, so these resources should be equivalent. [https://github.com/telerik/kendo-themes](https://github.com/telerik/kendo-themes)

### Response

**Joe** commented on 30 Jul 2021

Hi Joana, are there any step-by-step instructions for converting any of the Kendo Less themes to SASS and using them with Blazor? For example, how would I go about converting Moonlight?

### Response

**Joana** commented on 04 Aug 2021

Hi Joe, I believe my colleague Ivan covered the topic in the support thread that you have opened. For transparency, I am pasting the reply here as well:> More variety of swatches in our sass themes that are analogical to the known less themes in Kendo We are migrating the less themes to sass, as we are sunsetting them. Currently, we have covered blue opal, silver, default, bootstrap 3 (as bootstrap theme swatch) material and nova (as swatch for material).

We'll be adding the rest, minus fiori it the coming weeks for our september 2021 R3.> Is there a way to get early access to the swatches? We are still working on the infrastructure, but broadly speaking, themes will be available in our CDN and in our npm themes packages.

For a given version, the files are as follows:

CDN [https://cdn.kendostatic.com/themes/4.40.0/classic/classic-opal.css](https://cdn.kendostatic.com/themes/4.40.0/classic/classic-opal.css) NPM [https://unpkg.com/@progress/kendo-theme-classic@4.40.1/dist/classic-opal.scss](https://unpkg.com/@progress/kendo-theme-classic@4.40.1/dist/classic-opal.scss) I know I am sending you a two different URL's (4.40.0 and 4.40.1) but we are ironing the kinks and quirks of deployment. 4.40.0 is available on CDN but did not contain the source swatches. 4.40.1 has the swatches sources, but is not deployed (yet) to CDN.

With the next version of the themes, which will be available in early september, everything will be smooth.
